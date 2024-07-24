import logging
from .language import *
import requests
from datetime import datetime
import time
from urllib.parse import urlencode
import pandas as pd
import re
import base64
import chardet


class GitHubSearch:
  '''
  Class that is responsible for the GitHub API search of repositories.
  '''

  def __init__(self, pat: str = None):
    self.logger = logging.getLogger('search_logger')
    self.is_authenticated: bool = (pat is not None)
    self._lang: LinguistData = LinguistData()
    # set up urls for the 2 needed endpoints
    self._repo_path: str = 'https://api.github.com/search/repositories'
    self._rate_limit_path: str = 'https://api.github.com/rate_limit'
    # set up keep-alive session for the HTTP connection
    self._session = self._create_session(pat)

  # region session
  def _create_session(self, pat: str = None) -> requests.Session:
    session_headers: dict = {'Accept': 'application/vnd.github+json',
                             'X-GitHub-Api-Version': '2022-11-28'}
    if pat is not None:
      session_headers['Authorization'] = f'Bearer {pat}'
    session: requests.Session = requests.Session()
    session.headers.update(session_headers)
    self.logger.info('Session opened')
    return session

  def dispose(self):
    '''
    Closes the keep-alive HTTP session. Do not use this object after this
    method is called.
    '''
    self._session.close()
    self.logger.info('Session closed')
  # endregion

  # region rate limit
  def get_repo_rate_limit(self, resource: str = 'search') -> tuple[int, float]:
    '''
    Returns the remaining searches on the repositories endpoints of the current
    time frame as well as the time left until the next time frame begins.

    This call does not use up any rate limits.

    In case of an error, this assumes 0 tries are left and a wait time of 60
    seconds until the next frame begins.

    Parameters
    ----------
    resource: str
      The name of the resource the rate limit is to be retrieved from. Must be
      "core", "search" or any other valid GitHub resource. For keyword search
      "search" is the correct one, which is the default value. For other calls
      such as link calls the correct choice is "core".

    Returns
    -------
    tuple[int, float]
      A tuple containing the number of remaining API calls of the current time
      frame as first component, and the seconds until the next time frame starts
      as last component.
    '''
    # API call
    r: requests.Response = self._session.get(self._rate_limit_path)
    # response parsing
    if r.status_code == 200 or r.status_code == 304:
      body: dict = r.json()
      n_tries: int = body.get('resources').get(resource).get('remaining')
      reset_timestamp: int = body.get('resources').get(resource).get('reset')
      now_timestamp: int = datetime.timestamp(datetime.now())
      return n_tries, reset_timestamp - now_timestamp
    else:
      # if something went wrong, assume no tries are left and wait 1 minute
      self.logger.error(f'HTTP {r.status_code} assume 0 tries are left and '
                        'wait 60 seconds.')
      return 0, 60

  def _handle_rate_limit(self, min_limit: int = 0,
                         resource: str = 'search') -> int:
    n, waits = self.get_repo_rate_limit(resource)
    refreshed: bool = False
    if n <= min_limit:
      self.logger.info(f'Waiting {waits}s...')
      time.sleep(int(waits) + 1)
      n = 30 if self.is_authenticated else 10  # rate limits of GitHub REST API
    msg: str = f'Remaining searches = {n}'
    if not refreshed:
      msg += f', next window starts in {waits}s'
    else:
      msg += f', new window has started'
    self.logger.debug(msg)
    return n
  # endregion

  # region keyword search
  def get_all_search_results(self, keywords: list,
                             filter_out_non_programming: bool = False,
                             check_limit: bool = True) -> pd.DataFrame:
    '''
    Returns all parsable search results from the API search using the provided
    keywords.

    Parameters
    ----------
    keywords: list
      List of string keywords to use for the search. This must include all
      qualifiers as well as operators and the concatenated string must not
      exceed 255 characters (excluding length of qualifiers and operators).
    check_limit: bool
      Flag that states if rate limit checking is to be done before doint the
      initial search. Default value is True.
    filter_out_non_programming: bool
      Flag that states if repositories in the search that are labeled as using
      a non-programming language as main content language are to be skipped
      when storing the data. Default is True i.e. repositories containing
      mainly TeX, Markdown, etc. files will not be parsed and will therefore
      also not be found in the resulting DataFrame. 

    Returns
    -------
    pd.DataFrame
      DataFrame containing all results as feature vector row. The columns of
      this DataFrame are set by _create_empty_df_of_interest.
    '''
    # creating search string and setting up max pagination
    query: str = ' '.join(keywords)
    params: dict = {'q': query, 'per_page': 100}
    params_str: str = urlencode(params, safe=':+"')
    # wait for reset if remaining searches = 0 before request
    if check_limit:
      n: int = self._handle_rate_limit()
    # request loop
    url: str = self._repo_path
    cont: bool = True
    df_search, _ = self._create_empty_df_of_interest()
    error_count: int = 0
    max_error_count: int = 10
    while cont:
      if n > 0:
        r: requests.Response = self._session.get(url, params=params_str)
        n = n - 1
        self.logger.debug(f'API call done, {n} remaining searches this window')
        # handling data
        if r.status_code == 200:
          df = self._parse_page(r.json(), filter_out_non_programming)
          df_search = pd.concat([df_search, df], axis=0, ignore_index=True)
          # handling pagination
          if 'next' not in r.links.keys():
            cont = False
            self.logger.debug('Reached last page')
          else:
            url = r.links.get('next').get('url')  # set up url for next iter
        else:
          error_count += 1
          self.logger.error(f'HTTP {r.status_code}, retrying...')
          if error_count >= max_error_count:
            error_count = 0
            cont = False
            self.logger.error(f'Tried {max_error_count} times without'
                                 'success. Skipping page')
      else:
        n = self._handle_rate_limit()
    self.logger.info(f'Done searching, got {len(df_search)} results')
    return df_search

  def _create_empty_df_of_interest(self) -> tuple[pd.DataFrame, list]:
    fields_of_interest: list = ['id', 'url', 'name', 'description',
                                'owner', 'owner_type', 'owner_image_url',
                                'created_at', 'updated_at',
                                'homepage_url', 'repo_size_kb', 'license',
                                'num_stars', 'num_forks', 'is_fork',
                                'topics', 'is_archived', 'default_branch',
                                'main_language', 'has_projects', 'has_wiki',
                                'has_pages', 'has_discussions', 'has_issues',
                                'info_url']
    df = pd.DataFrame(columns=fields_of_interest)
    return df, fields_of_interest

  def _parse_page(self, page_body: dict,
                  filter_out_non_programming: bool = False) -> pd.DataFrame:
    df, _ = self._create_empty_df_of_interest()
    i: int = 0
    items: list = page_body.get('items')
    for repo in items:
      # filter out all non-programming related repositories
      if filter_out_non_programming:
        if not self._lang.is_programming_language(repo.get('language')):
          continue
      # everything else is accepted as passable data
      vector: list = []
      vector.append(repo.get('id'))  # id (int)
      vector.append(repo.get('html_url'))  # url (str)
      vector.append(repo.get('name'))  # name (str)
      vector.append(repo.get('description'))  # description (str?)
      vector.append(repo.get('owner').get('login'))  # owner (str)
      vector.append(repo.get('owner').get('type'))  # owner_type (str)
      # owner_image_url (str?)
      vector.append(repo.get('owner').get('avatar_url'))
      vector.append(repo.get('created_at'))  # created_at (str)
      vector.append(repo.get('updated_at'))  # updated_at (str)
      vector.append(repo.get('homepage'))  # homepage_url (str?)
      vector.append(repo.get('size'))  # repo_size_kb (int)
      license_dict: dict = repo.get('license')
      vector.append((None if (license_dict is None)
                     else license_dict.get('name')))  # license (str?)
      vector.append(repo.get('stargazers_count'))  # num_stars (int?)
      vector.append(repo.get('forks_count'))  # num_forks (int?)
      vector.append(repo.get('fork'))  # is_fork (bool)
      vector.append(repo.get('topics'))  # topics (list[str]?)
      vector.append(repo.get('archived'))  # is_archived (bool)
      vector.append(repo.get('default_branch'))  # default_branch (str)
      vector.append(repo.get('language'))  # main_language (str)
      vector.append(repo.get('has_projects'))  # has_projects (bool)
      vector.append(repo.get('has_wiki'))  # has_wiki (bool)
      vector.append(repo.get('has_pages'))  # has_pages (bool)
      vector.append(repo.get('has_discussions'))  # has_discussions (bool)
      vector.append(repo.get('has_issues'))  # has_discussions (bool)
      # tmp for number of subscribers (int), open issues (int),
      # contributors (int), commits (int) and languages ([str])
      vector.append(repo.get('url'))
      df.loc[i] = vector
      i += 1
    return df

  def get_result_count(self, keywords: list, check_limit: bool = True) -> int:
    '''
    Returns the number of repositories found when using the provided keywords.

    This does the GitHub API search using the given keywords and returns the
    total count of found repositories. If the number is greater than 1000 the
    GitHub API does not allow to retrieve all repositories using this search
    and the search has to be split up into multiple small searches e.g. by
    using date ranges to only fetch repositories from a specific time frame.

    Parameters
    ----------
    keywords: list
      The list of keywords to use for the initial search. This list must
      include everything that is needed for the search e.g. `AND`s, `topic:XYZ`
      or `"flutter` & 'app"` must be given as element.
    check_limit: bool
      Flag that states if rate limit checking is to be done before doint the
      initial search. Default value is True.

    Returns
    -------
    int
      Number of repositories that are found for the given keywords. If this is
      greater than 1000 the search must be split up into smaller sub-searches.
      In case of error this returns -1.
    '''
    # creating search string and setting up max pagination
    query: str = ' '.join(keywords)
    params: dict = {'q': query, 'per_page': 100}
    params_str: str = urlencode(params, safe=':+"')
    # wait for reset if remaining searches = 0 before request
    if check_limit:
      _ = self._handle_rate_limit()
    # do initial search
    url: str = self._repo_path
    r: requests.Response = self._session.get(url, params=params_str)
    if r.status_code == 200:
      return r.json().get('total_count')
    else:
      self.logger.error(f'HTTP {r.status_code}, {r.url}')
      return -1

  def _datetime_to_github_str(self, date: datetime) -> str:
    return str(date).split(' ')[0]

  def get_date_params(self, keywords: list, check_limit: bool = True,
                      start_date: datetime = None) -> tuple[int, str]:
    '''
    Finds the number of results for the first search qualifier that results in
    an API response with less than 1000 elements in it together with the
    qualifier string itself.

    Parameters
    ----------
    keywords: list
      The list of keywords to use for the initial search. This list must
      include everything that is needed for the search e.g. `AND`s, `topic:XYZ`
      or `"flutter` & 'app"` must be given as element.
    check_limit: bool
      Flag that states if rate limit checking is to be done before doint the
      initial search. Default value is True.

    Returns
    -------
    int
      Number of repositories that are found for the given keywords with the
      first found sub 1000 results creating qualifier.
    str
      The qualifier as string that results in a sub-search for the keywords
      with less than 1000 results.
    '''
    if start_date is None:
      start_date = datetime.now()
    # rate limit check
    if check_limit:
      n = self._handle_rate_limit()
    # from here on n must always be >0 (that's given if check_limit == True)
    max_results: int = 1000
    start_year: datetime = start_date - pd.DateOffset(years=1)  # last year
    start_month: datetime = start_date - pd.DateOffset(months=1)  # last month
    start_week: datetime = start_date - pd.DateOffset(weeks=1)  # last week
    start_day: datetime = start_date - pd.DateOffset(days=1)  # yesterday
    # create qualifiers for the creation date using the ranges
    # all repositories until start_date, start_date to start_date - 1 year,
    # start_date to start_date - 1 month, start_date to start_date - 1 week,
    # and start_date to start_date - 1 day
    # e.g. 'created:2023.01.01..2024.01.01'
    created_qualifiers: list = [
      f'created:<={self._datetime_to_github_str(start_date)}',
      f'created:{self._datetime_to_github_str(start_year)}..{
          self._datetime_to_github_str(start_date)}',
      f'created:{self._datetime_to_github_str(start_month)}..{
          self._datetime_to_github_str(start_date)}',
      f'created:{self._datetime_to_github_str(start_week)}..{
          self._datetime_to_github_str(start_date)}',
      f'created:{self._datetime_to_github_str(start_day)}..{
          self._datetime_to_github_str(start_date)}'
    ]
    # each qualifier is then used to get the repository count
    iter: int = 0  # current iteration index of the loop
    tries: int = 0  # number of tries for this iteration
    max_tries: int = 5  # number of tries per iteration until it is skipped
    while iter < len(created_qualifiers):
      created_qualifier = created_qualifiers[iter]
      self.logger.info(f'Looking for the keywords "{keywords}" with the'
                       f'qualifier "{created_qualifier}"')
      new_keywords = keywords + [created_qualifier]
      if n <= 0:
        n = self._handle_rate_limit()
      num_results: int = self.get_result_count(new_keywords, False)
      n -= 1
      if num_results < 0:  # error occurred while counting
        if tries >= max_tries:
          self.logger.error(f'Search using "{new_keywords}" was unsuccessful'
                            f'{max_tries} times. Skipping this qualifier')
          tries = 0
          iter += 1
        else:
          self.logger.warning('Qualifier led to -1 results, retrying...')
          tries += 1
      else:  # data successfully fetched
        if num_results <= max_results:
          self.logger.debug(f'Found {num_results} <= {max_results} results'
                            f'using "{new_keywords}" as search parameters')
          return num_results, created_qualifier
        tries = 0
        iter += 1
    # if all qualifiers are looked at, there were more than 1000 repositories
    # created in one week => anomaly
    self.logger.info(f'More than {max_results} repositories created in the '
                     f'week of {start_week} to {start_date}, '
                     'which is an anomaly')
    return num_results, created_qualifier

  def get_all_date_params(self, keywords: list,
                          date: datetime = datetime(2024, 1, 1)):
    num_results, qualifier = self.get_date_params(keywords,
                                                  start_date=date)
    qualifiers: list = [qualifier]
    while num_results != 0 and not qualifier.split(':')[1].startswith('<='):
      date_str: str = qualifier.split(r':')[1]  # remove 'created:'
      date_str = date_str.split(r'..')[0]  # remove '..YYYY-MM-DD'
      search_date: datetime = datetime.strptime(date_str, '%Y-%m-%d')
      num_results, qualifier = self.get_date_params(keywords,
                                                    start_date=search_date)
      qualifiers.append(qualifier)
    return qualifiers
  # endregion

  # region additional search
  def get_additional_data_for_row(self,
                                  name: str, owner: str) -> tuple[int, int, int,
                                                                  list, str]:
    '''
    Gathers additional information of interest for a given repository url.

    The results of this could be appended to a DataFrame for better analysis
    options.

    This performs 4-6 new API calls on the `core` resource.
      * 1 call to get the number of open issues and subscribers on api_url
      * 1-2 calls to get the number of contributors. If less than 30 this is
        only 1 API call. If more than 30 then this needs exactly 2 calls
      * 1 call to get the list of languages used in this repository
      * 1-2 calls to get the README contents of this repository. If no README
        is found in the repository this only uses 1 call

    Parameters
    ----------
    name: str
      Name of the repository. This is used to build the api url
      `https://api.github.com/repos/{owner}/{name}`.
    owner: str
      Name of the repository owner. This is used to build the api url
      `https://api.github.com/repos/{owner}/{name}`.

    Returns
    -------
    num_issues: int
      The number of open issues in this repository.
    num_subscribers: int
      The number of people that subscribed to this repository.
    num_contributors: int
      The number of contributors that helped out in this repository.
    languages: list
      List of language keys that are used in this repository's codebase. This
      includes the main_language as well as all other languages associated
      with files in this repository.
    readme: str
      Text content of the README file of this repository. This is only
      successful if there is a readme.md or readme.txt file (case-insensitive)
      in the root of the repository.
    '''
    api_url: str = f'https://api.github.com/repos/{owner}/{name}'
    per_page: int = 30  # limit for some of the queries
    n: int = self._handle_rate_limit(resource='core')

    # reading open_issues and subscribers_count from the details api_url
    r: requests.Response = self._session.get(api_url)
    n -= 1
    if r.status_code == 200:
      num_issues = r.json()['open_issues']
      num_subscribers = r.json()['subscribers_count']
      languages_url = r.json()['languages_url']
      contributors_url = r.json()['contributors_url']
    else:
      self.logger.error(f'HTTP {r.status_code}, {r.url}')
      # if initial search fails, the following calls will fail as-well
      return (-1, -1, -1, -1, [])

    # reading the number of contributors from the paginated contributors_url
    if n < 2:
      n: int = self._handle_rate_limit(min_limit=2, resource='core')
    r: requests.Response = self._session.get(contributors_url)
    n -= 1
    if r.status_code == 200:
      if 'last' in r.links:
        last_url: str = r.links.get('last').get('url')
        r: requests.Response = self._session.get(last_url)
        n -= 1
        if r.status_code == 200:
          pattern = r'page=(\d+)'
          match = re.search(pattern, last_url)
          last_page_number: int = int(match.group(1))  # ? must be there
          num_contributors = per_page * (last_page_number - 1) + len(r.json())
        else:
          self.logger.error(f'HTTP {r.status_code}, {r.url}')
          num_contributors = -1
      else:
        num_contributors = len(r.json())
    else:
      self.logger.error(f'HTTP {r.status_code}, {r.url}')
      num_contributors = -1

    # reading all used languages in the repository from languages_url
    if n < 1:
      n: int = self._handle_rate_limit(resource='core')
    r: requests.Response = self._session.get(languages_url)
    n -= 1
    if r.status_code == 200:
      body: dict = r.json()
      languages = list(body.keys())
    else:
      languages = []

    # reading out README contents from /contents
    if n < 2:
      n: int = self._handle_rate_limit(resource='core')
    contents_url: str = f'{api_url}/contents'
    contents_url = re.sub(r'//contents', r'/contents', contents_url)
    r: requests.Response = self._session.get(contents_url)
    n -= 1
    if r.status_code == 200:
      files: list = r.json()
      readme: str = ''  # ? in case no README found
      for repo_file in files:
        fname: str = str(repo_file.get('name')).lower()
        if fname.startswith('readme.'):
          readme_url: str = repo_file.get('url')
          r: requests.Response = self._session.get(readme_url)
          n -= 1
          if r.status_code == 200:
            readme_dict: dict = r.json()
            readme_bytes: bytes = base64.b64decode(readme_dict.get('content'))
            encoding_detection = chardet.detect(readme_bytes)
            encoding: str = encoding_detection.get('encoding')
            if encoding:
              readme = readme_bytes.decode(encoding, 'ignore')
            else:
              readme = 'Invalid Encoding'
            break
          else:
            readme = 'ERROR'
    else:
      readme = 'ERROR'

    return num_issues, num_subscribers, num_contributors, languages, readme
  # endregion
