# Rayyan Deduplication

This file illustrates all decisions made by me when performing a manual
deduplication using Rayyan's duplicate detection

## Metrics

* order: PubMed > ACM > IEEE Xplore > Web of Science > APA PsycInfo > Google
  * if nothing else speaks against it, the match of the "lesser" database is removed in case of duplicates
* Trial Registration ID
  * if potential duplicates have the same trial registration id, they are most likely a duplicate
* Abstract Text almost identical
  * caseing: OBJECTIVE vs objective, PsycInfo vs PsycINFO
  * latex export: \chi vs X
  * end of abstract: Keywords section appended vs missing
  * start of abstract: Highlights section added vs missing
  * naming of authors: DA Daugherty vs Daugherty DA
  * abbreviations: Smartphone-based EMA ... vs Smartphone-based EMA in a blended therapy
  * if the title + abstract are almost identical, the potential duplicates are most likely duplicates
* Google Scholar marked multiple publications as versions of one another
  * if Google Scholar marks some potential duplicates as versions of one another, they are most likely duplicates

## Ressolved Duplicates

### Trivial

* Recurrent Neural Networks in Mobile Sampling and Intervention
  * 94%, pubmed vs GS
* Exploring the features of an app-based just-in-time intervention for depression
  * 95%, pubmed vs GS
* Ecological Momentary Assessments and Interventions in Alzheimer's Caregiving
  * 90%, pubmed vs GS
* Mobile services provide value by decoupling the time and location constraints in healthcare delivery
  * 97%, wos vs IEEE
* Disseminating cardiovascular disease risk assessment with a PAHO
  * 75%, wos vs pubmed
* The Efficacy of Internet-based Intervention on Quality of Life for Patients with Chronic Post-surgical Pain
  * 87%, wos vs pubmed
* A mobile intervention for core needle biopsy related pain and anxiety: A usability study
  * 90%, wos vs apa
* A Mobile Just-in-Time Adaptive Intervention for Smoking Cessation: Pilot Randomized Controlled Trial
  * 95%, pubmed vs GS
* Don't go there - zero permission...
  * forgot to track this one :(
* Real-time demonstration of a mHealth app designed to reduce college students hazardous drinking
  * 94%, pubmed vs GS
* A Smartphone-Delivered Ecological Momentary Intervention for Problem Gambling (GamblingLess: Curb Your Urge): Single-Arm Acceptability and Feasibility Trial
  * 90%, pubmed vs GS
* Is a brief mindfulness ecological momentary intervention more efficacious than a self-monitoring app for social anxiety disorder? A randomized controlled trial
  * 91%, pubmed vs GS
* An Ecological Momentary Intervention Study of Emotional Responses to Smartphone-Prompted CBT Skills Practice and the Relationship to Clinical Outcomes
  * 90%, pubmed vs GS vs wos
* Exploring Pasifika wellbeing: findings from a large cluster randomised controlled trial of a mobile health intervention programme
  * 85%, wos vs pubmed
* Acceptability and Preliminary Effects of a Mindfulness Mobile Application for Ruminative Adolescents
  * 85%, wos vs pubmed
* Smartphone delivery of a hope intervention: Another way to flourish
  * 94%, pubmed vs GS
* An ecological momentary intervention incorporating personalised feedback to improve symptoms and social functioning in schizophrenia spectrum disorders
  * 95%, pubmed vs GS
* Characterizing Breakthrough Cancer Pain Using Ecological Momentary Assessment with a Smartphone App: Feasibility and Clinical Findings
  * 96%, pubmed vs GS vs GS
  * Google Scholar found 2 versions of the same paper
* Iterative development of Vegethon: A theory-based mobile app intervention to increase vegetable consumption.
  * 96%, pubmed vs apa
* The EMPOWER blended digital intervention for relapse prevention in schizophrenia: A feasibility cluster randomised controlled trial in Scotland and Australia.
  * 90%, wos vs apa vs pubmed
* Delivering a media literacy intervention for body dissatisfaction using an app-based intervention: A feasibility and pilot trial
  * 91%, pubmed vs GS
* Development of Mobile Contingency Management for Cannabis Use Reduction
  * 89%, wos vs pubmed
* Symptom Reduction and Engagement in a Cognitive-Behavioral Mobile Phone App: A Study of User Profiling to Determine Prognostic Indicators
  * 84%, wos vs pubmed
* A Pilot Implementation-Effectiveness Trial of a Single-Session Telehealth Workshop and Smartphone-Based Cognitive Behavioral Intervention for Managing Emotions Among College Students
  * 92%, pubmed vs GS
* An ecological momentary intervention for smoking cessation: the associations of just-in-time, tailored messages with lapse risk factors
  * 94%, pubmed vs GS
* An open trial of a smartphone-assisted, adjunctive intervention to improve treatment adherence in bipolar disorder
  * 93%, pubmed vs GS
* Experience Sampling and Programmed Intervention Method and System for Planning, Authoring, and Deploying Mobile Health Interventions: Design and Case Reports
  * 90%, pubmed vs GS
* A Digital Companion, the Emma App, for Ecological Momentary Assessment and Prevention of Suicide: Quantitative Case Series Study
  * 95%, pubmed vs GS
* Treatment condition as a moderator and change in trait mindfulness as a mediator of a brief mindfulness ecological momentary intervention for generalized anxiety disorder
  * 86%, pubmed vs GS
* Feasibility of the HEAR-aware App for Hearing Loss Self-Management: A Nonrandomized Intervention Study to Examine Intervention Acceptability and the Stages-of-Change Concept
  * 94%, pubmed vs GS
* Examining the Effects of a Brief, Fully Self-Guided Mindfulness Ecological Momentary Intervention on Empathy and Theory-of-Mind for Generalized Anxiety Disorder: Randomized Controlled Trial
  * 85%, pubmed vs GS
* Personalized prediction of smartphone-based psychotherapeutic micro-intervention success using machine learning
  * 96%, pubmed vs GS
* An Ecological Momentary Intervention for Smoking Cessation: Evaluation of Feasibility and Effectiveness
  * 92%, pubmed vs GS
* The Future of Psychotherapy in Turkey: Predictions for the Next 10 Years
  * 86%, pubmed vs apa
* Improvements in Health Might Contradict Adherence to Mobile Health Interventions: Findings from a Self-Care Cancer App Study
  * 95%, pubmed vs apa
* The Effects of Continuous Usage of a Diabetes Management App on Glycemic Control in Real-world Clinical Practice: Retrospective Analysis
  * 96%, pubmed vs apa
* Successful Organizational Strategies to Sustain Use of A-CHESS: A Mobile Intervention for Individuals With Alcohol Use Disorders
  * 93%, pubmed vs apa
* Pilot Testing in the Wild: Feasibility, Acceptability, Usage Patterns, and Efficacy of an Integrated Web and Smartphone Platform for Bipolar II Disorder
  * 95%, pubmed vs GS
* Client experiences of blending a coping-focused therapy for auditory verbal hallucinations with smartphone-based ecological momentary assessment and intervention
  * 91%, pubmed vs GS
* Virtues, ecological momentary assessment/intervention and smartphone technology
  * 96%, pubmed vs apa
* Mobile Phone Access and Implications for Digital Health Interventions Among Adolescents and Young Adults in Zimbabwe: Cross-Sectional Survey
  * 92%, pubmed vs apa
* Use of the Smoking Cessation App Ex-Smokers iCoach and Associations With Smoking-Related Outcomes Over Time in a Large Sample of European Smokers: Retrospective Observational Study
  * 92%, pubmed vs apa
* Delivering Mindfulness-Based Interventions for Insomnia, Pain, and Dysfunctional Eating Through a Text Messaging App: Three Randomized Controlled Trials Investigating the Effectiveness and Mediating Mechanisms
  * 95%, pubmed vs apa
* Harnessing context sensing to develop a mobile intervention for depression
  * 94%, pubmed vs GS
* A randomized controlled trial of a 14-day mindfulness ecological momentary intervention (MEMI) for generalized anxiety disorder
  * 90%, pubmed vs GS
* Mobile Health Technology Using a Wearable Sensorband for Female College Students With Problem Drinking: An Acceptability and Feasibility Study
  * 95%, pubmed vs GS
* Use of the experience sampling method in the context of clinical trials
  * 93%, pubmed vs GS
* Efficacy of a Just-in-Time Adaptive Intervention to Promote HIV Risk Reduction Behaviors Among Young Adults Experiencing Homelessness: Pilot Randomized Controlled Trial
  * 93%, pubmed vs apa vs GS
* Transdiagnostic Ecological Momentary Intervention for Improving Self-Esteem in Youth Exposed to Childhood Adversity: The SELFIE Randomized Clinical Trial
  * 97%, pubmed vs GS
* A Just-In-Time Adaptive intervention (JITAI) for smoking cessation: Feasibility and acceptability findings
  * 93%, pubmed vs GS
  * this is a F&A study to another study above in this same section
* Mobile Ecological Momentary Assessment and Intervention and Health Behavior Change Among Adults in Rakai, Uganda: Pilot Randomized Controlled Trial
  * 95%, pubmed vs GS
* Preliminary Outcomes of an Ecological Momentary Intervention for Social Functioning in Schizophrenia: Pre-Post Study of the Motivation and Skills Support App
  * 93%, pubmed vs GS
* Mobile Phone-Based Ecological Momentary Intervention to Reduce Young Adults' Alcohol Use in the Event: A Three-Armed Randomized Controlled Trial
  * 95%, pubmed vs GS
* Using smartphone-based ecological momentary assessment and personalized feedback for patients with chronic cancer-related fatigue: A proof-of-concept study
  * 92%, pubmed vs GS
* Efficacy of a Theory-Based Cognitive Behavioral Technique App-Based Intervention for Patients With Insomnia: Randomized Controlled Trial
  * 91%, pubmed vs apa
* Pilot randomized trial of MOMENT, a motivational counseling-plus-ecological momentary intervention to reduce marijuana use in youth
  * 93%, pubmed vs GS
* Assessing Real-Time Moderation for Developing Adaptive Mobile Health Interventions for Medical Interns: Micro-Randomized Trial
  * 94%, pubmed vs GS
* Feasibility and Acceptability of Smartphone-Based Ecological Momentary Assessment of Alcohol Use Among African American Men Who Have Sex With Men in Baltimore
  * 94%, pubmed vs GS
* A Compassion-Focused Ecological Momentary Intervention for Enhancing Resilience in Help-Seeking Youth: Uncontrolled Pilot Study
  * 96%, pubmed vs GS
* Smartphone-based ecological momentary assessment and intervention in a blended coping-focused therapy for distressing voices: Development and case illustration
  * 92%, pubmed vs GS
* Feasibility, Acceptability, and Design of a Mobile Ecological Momentary Assessment for High-Risk Men Who Have Sex With Men in Hanoi, Vietnam: Qualitative Study
  * 91%, pubmed vs GS
* Testing the Efficacy of a Brief, Self-Guided Mindfulness Ecological Momentary Intervention on Emotion Regulation and Self-Compassion in Social Anxiety Disorder: Randomized Controlled Trial
  * 84%, pubmed vs GS
* Challenges of and Solutions for Developing Tailored Video Interventions That Integrate Multiple Digital Assets to Promote Engagement and Improve Health Outcomes: Tutorial
  * 91%, pubmed vs apa
* A web-based program improves physical activity outcomes in a primary care angina population: randomized controlled trial
  * 96%, pubmed vs apa
* Love My Body: Pilot Study to Understand Reproductive Health Vulnerabilities in Adolescent Girls
  * 94%, pubmed vs apa
* A counsellor-supported 'PTSD Coach' intervention versus enhanced Treatment-as-Usual in a resource-constrained setting: A randomised controlled trial
  * 94%, pubmed vs apa
* Certified Peer Specialists' Perspective of the Barriers and Facilitators to Mobile Health Engagement
  * 93%, pubmed vs apa
* Ownership, Use of, and Interest in Digital Mental Health Technologies Among Clinicians and Young People Across a Spectrum of Clinical Care Needs: Cross-sectional Survey
  * 95%, pubmed vs apa
* The design of ecological momentary assessment technologies
  * 88%, GS vs IEEE
* Adaptive symptom monitoring using hidden markov models–an application in ecological momentary assessment
  * 87%, GS vs IEEE
* Examination of nutrition monitoring through ecological momentary assessment during an internet-based, self-directed weight loss intervention
  * 91%, GS vs apa
* Alleviating the Harm: A Media Literacy Intervention for Body Dissatisfaction Using Ecological Momentary Intervention
  * 91%, GS vs apa

### Non-Trivial

* Personalized adherence activity recognition via model-driven sensor data assessment
  * 87%, wos vs pubmed
  * pubmed site shows article is of same year, volume, issue and page
* Usefulness of Feedback in e-Learning From the Students' Perspective
  * 93%, both on wos
  * one has no DOI
  * both are marked as different versions of the same paper in Goolge Scholar
    * keeping the newer one
* A Mobile-Based Intervention to Increase Self-esteem in Students With Depressive Symptoms: Randomized Controlled Trial
  * 88%, both on pubmed
  * one is a "Correction" of the other, but only lists the errors and not the full text
  * keeping old/faulty version
* An alternative goal-setting technique for addictive behaviour interventions: The Chronos Approach
  * 98%, both on wos
  * everything is the same, except DOIs
  * both are marked as different versions of the same paper in Goolge Scholar
    * keeping the newer one
* Multi-Modal Methodology for Adapting Digital Health Tools to New Populations: Adaptation of the Video Information Provider (VIP) for Persons Living with HIV with HIV-Associated Non-AIDS (HANA) Conditions
  * 84%, wos vs pubmed
  * everything same, except DOI
    * 10.3233/shtii90446.
    * 10.3233/shti190446.
  * assuming this is a type on wos, as the article in pubmed shows the exact same conference, with the exact same page number and everything else
* Connecting domains-Ecological momentary assessment in a mobile sensing framework.
  * 94%, wos vs apa
  * almost everything the same, two different DOIs
    * 10.1007/978-3-030-31620-4_12.
    * 10.1007/978-3-030-31620-4.
  * both DOIs point to the same book but one links to the exact chapter
* Rationale, Theoretical Underpinnings, and Design of HEAR-aware: Providing Adults With Hearing Loss With Tailored Support to Self-Manage Their Hearing Problems via a Smartphone App, as an Alternative to Hearing Aids
  * 89%, wos vs pubmed
  * everything same, except DOI
    * 10.1044/2020_aja-19-00079.
    * 10.1044/2020.
  * both DOIs reference the same publication, one just specifies the chapter
* mHealth Intervention to Improve Cardiometabolic Health in Rural Hispanic Adults: A Pilot Study
  * 71%, wos vs pubmed
  * almost everything the same, two different DOIs
    * 10.1097/kn.0000000000000882.
    * 10.1097/jcn.0000000000000882.
  * the DOIs indicate that these are indeed the same publication, but published in different journals by the same publisher
    * jcn? = Journal of Clinical Neurology
    * kn? = Journal of Cardiovascular Nursing
  * assume that they are indeed the same paper, as even the full text looks similar
* Assessment of e-aushadhi program (drug inventory e-health initiative in Rajasthan) using benefit evaluation framework
  * 85%, wos vs pubmed
  * almost everything the same, two different DOIs
    * 10.4103/jfmpc.jfmpc_2047_21.
    * 10.4103/jfmpc.jfmpc_2047.
  * both DOIs point to the same journal but one links to the exact place
* An evaluation of the efficacy of two add-on ecological momentary intervention modules for depression in a pragmatic randomized controlled trial (ZELF-i)
  * 88%, wos vs GS
  * GS has no DOI, abbreviates authors and misses a lot of metadata
  * title, abstract and author surnames all are identical
  * full-text also looks identical
* Challenges and Opportunities for Designing Technology-Based Ecological Momentary Interventions (EMIs) in Mental Health
  * 81%, wos vs GS
  * almost dentical metadata, abstract and title
    * one has proceeding name appended to it
  * different DOIs
    * 10.1007/978-3-031-21333-5_88
    * 10.1007/978-3-031-21333-5
  * both DOIs point to the same proceeding but one links to the exact chapter
* Enhancing type 2 diabetes treatment through digital plans of care. Patterns of access to a care-planning app over the first 3 months of a digital health intervention
  * 70%, wos vs pubmed
  * identical authors and title
  * both are missing the abstract => publication is found only as PDF file without any HTML-friendly abstract text
    * this is also the case in other databases such as Google Scholar
  * but the linked PDF is identical
* A Web-Based and Mobile Intervention Program Using a Spaced Education Approach for Workplace Mental Health Literacy: Cluster Randomized Controlled Trial
  * 89%, wos vs pubmed
  * almost everything is identical
  * two different DOIs
    * 10.2024/1/e51791.
    * 10.2196/51791.
  * this publication has the second DOI listed on most databases, but the URL of the first DOI links to the same resource
* Cell phone intervention for you (CITY): A randomized, controlled trial of behavioral weight loss intervention for young adults using mobile technology
  * 84%, pubmed vs apa
  * the one on apa is an erratum to the original
    * only reports the error, the match does not contain the body text
    * the error was a misspelling of one of the authors' names
  * keeping the original article on pubmed
* A decision framework for an adaptive behavioral intervention for physical activity using hybrid model predictive control
  * 67%, pubmed vs ieee
  * identical authors and abstract, different titles and DOIs
  * the version on pubmed has an English abstract, but the body is in Spanish
    * the version on IEEE is newer and has the same contents but in English
      * slight differences: instead of showing the Just Walk App they describe it in text
      * the main points look to be the same, but I am not well versed in Spanish
        * the numbers are identical
* Exploring the Effect of the Dynamics of Behavioral Phenotypes on Health Outcomes in an mHealth Intervention for Childhood Obesity: Longitudinal Observational Study
  * 89%, pubmed vs apa
  * the one on apa is a correction, but once again it only reports the errors and doesn't contain the fully corrected version
* HowNutsAreTheDutch (HoeGekIsNL): A crowdsourcing study of mental symptoms and strengths
  * 85%, pubmed vs apa
  * one is a corrigendum, only states the errors and does not provide the full text
    * the error was a too conservative estimation in prevelance of depression levels due to the used data
* m-Path: An easy-to-use and flexible platform for ecological momentary assessment and intervention in behavioral research and clinical practice
  * didn't note similarity
  * identical authors, abstract and title
  * one is missing a DOI
  * different release dates
  * every site shows release 2023 (even other databases not included in search like Frontiers in Science)
    * Google Scholar lists the version from 2023 as version of its own match from 2022
  * these are versions of the same paper, the newer one is kept
* Addressing Discrimination and Violence against Lesbian, Gay, Bisexual, Transgender, and Queer (LGBTQ) persons from Brazil: A mobile Health intervention
  * 98%, both on pubmed
  * different DOIs:
    * 10.21203/rs.3.rs-2034975/v1.
    * 10.1186/s12889-023-16857-4.
  * the first DOI is marked as preprint on pubmed => keeping the other, newer one
* MedLink: A Mobile Intervention to Address Failure Points in the Treatment of Depression in General Medicine
  * 76%, pubmed vs acm
  * same authors, same title but one has "Proceedings of ..." appended
  * identical abstract
  * one is missing a DOI, the other's DOI links to the same proceeding that the other has in its name (Proceedings of the 9th International Conference on Pervasive Computing Technologies for Healthcare, p. 100-107)
    * also links to the same page numbers p. 100-107
* Pilot Randomized Controlled Trial of Feasibility, Acceptability, and Preliminary Efficacy of a Web-Based Physical Activity and Sedentary Time Intervention for Survivors of Physical Inactivity-Related Cancers
  * 70%, pubmed vs apa
  * one is an author correction to the other, but only reports the error
    * error was that a statement in Acknowledgements was missing
  * keeping the full-text one
* Increasing cardiovascular medication adherence: A medical research council complex mhealth intervention mixed-methods feasibility study to inform global practice
  * 91%, pubmed vs apa
  * the one in apa is a corrigendum, again only mentioning the errors
    * errors were some mistranslations in the MMAS-8 scale from Persian for Iran
    * other errors were missing text in Acknowledgements and some tables
* Evaluating The Effectiveness Of An Ecological Momentary Intervention Targeting Body Checking Behaviors
  * 83%, both on GS
  * identical title, almost identical abstract
  * one entry is a thesis whereas the other is a journal publication
  * keeping the one in a journal as it most likely is a publication based on the thesis after dissertation
* Assessment and intervention in the wild: Possibilities for redeeming the smartphone
  * 95%, GS vs apa
  * identical title, GS skipps many authors, abstract is very different
  * GS has the apa match in the versions of its own match, but is of the same date (Spring 2016)
    * both versions are Vol.35, Iss. 1, p. 77-82 in Journal of Psychology and Christianity
    * keeping APA PsycInfo match as I do not have access to the other one's PDF
* A smartphone application of “Family Connections” to increase the use of skills and improve psychological symptoms in relatives of people with borderline personality disorder
  * 87%, both on GS
  * identical paper, not listed in each others' versions, but GS does find it twice
    * the full-text seems to be identical
* A Pilot Study to Reduce Intimate Partner Violence in Kenia: Usability of a Mobile-based Ecological Momentary Intervention and Assessment
  * 95%, both on GS
  * both articles link to the same paper, which is a study performed in a Bachelor's Thesis
* A digital companion for ecological momentary assessment and prevention of suicide: A case series on the use of the emma app
  * 86%, both on GS
  * one is a preprint of the other according to the full-text
* Combined Motivational Interviewing and Ecological Momentary Intervention to Reduce Hazardous Alcohol Use Among Sexual Minority Cisgender Men and
  * 76%, both on GS
  * same story: different links but full text looks identical
* Event-level risk for negative alcohol consequences in emerging adults: The role of affect, motivation, and context.
  * 100%, both on apa
  * everything is identical except the DOI and abstract
    * 10.1037/adb0000969.
    * 10.1037/adb0000866.
  * the second article states that there is a retraction happening and that the article would be re-submitted
  * the first article states in the full-text, that the other is the final version
    * keeping 10.1037/adb0000866.
* Digital phenotyping with mobile and wearable devices: Advanced symptom measurement in child and adolescent depression.
  * 86%, both on apa
  * one is a correction to the other, only naming the errors
    * error was wrong citation of a passage
* Tools for eMental-health: A coping processor for adaptive and interactive mobile systems for stress management.
  * 79%, both on apa
  * different DOIs
    * 10.4018/978-1-5225-0778-9.ch014.
    * 10.4018/978-1-4666-9986-1.ch006.
  * articles look the same, but just published in another journal
    * Gaming and technology addiction: Breakthroughs in research and practice
    * Integrating technology in positive pychology practice
  * keeping the first one, as it is newer
* Designing messaging to engage patients in an online suicide prevention intervention: Survey results from patients with current suicidal ideation.
  * 96%, both on apa
  * one is a correction, only stating the errors
    * error was that an image was added twice and one image was missing
* Lunch line: using public displays and mobile devices to encourage healthy eating in an organization - Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing
  * 98%, both on acm
  * same title, same abstract, same authors, different DOIs
    * 10.1145/2632048.2636086.
    * 10.1145/632048.2636086.
  * DOIs linkt to different resources, but both of them are UbiComp'14 Proceedings of 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing, September 2014
    * one was released in 2014
    * the other was released in 2018
    * both link to pp. 823-834
  * keeping the newer one, as these are most likely versions of one another

## Unclear

## Kept All

* Usage and Daily Attrition of a Smartphone-Based Health Behavior Intervention: Randomized Controlled Trial
  * Usage and Weekly Attrition in a Smartphone-Based Health Behavior Intervention for Adolescents: Pilot Randomized Controlled Trial
  * 64%, both on pubmed
  * same authors, similar title, different DOIs and different abstracts
* Community-Based, Cluster-Randomized Pilot Trial of a Cardiovascular Mobile Health Intervention: Preliminary Findings of the FAITH! Trial
  * Community-based, cluster-randomized pilot trial of a cardiovascular mHealth intervention: Rationale, design, and baseline findings of the FAITH! Trial
  * 63%, both on pubmed
  * same authors, similar title, different DOIs and different abstracts
    * it looks like one is a rushed release to display preliminary findings and the other the rationale, design and final findings of the same study
* An Ecological Mobile Momentary Intervention to Support Dynamic Goal Pursuit: Feasibility and Acceptability Study: Feasibility and Acceptability Study
  * An ecological momentary intervention to support dynamic goal pursuit: pilot study.
  * 80%, pubmed vs GS
  * the pilot study was released 1 year before the F&A study, indicating these are two different publications
    * also: different DOIs, titles and abstracts
  * another duplicate of the first paper was found on GS
    * so pubmed only has the F&A study, GS both
* A smartphone-based intervention with diaries and therapist-feedback to reduce catastrophizing and increase functioning in women with chronic widespread pain: randomized controlled trial
  * A smartphone-based intervention with diaries and therapist feedback to reduce catastrophizing and increase functioning in women with chronic widespread pain. part 2: 11-month follow-up results of a randomized trial
  * 89%, both on pubmed
  * one is marked as being the second part i.e. a follow-up study to the first one
* Feasibility and Acceptability of a Mobile Technology Intervention to Support Postabortion Care in British Columbia: Phase I
  * Feasibility and Acceptability of a Mobile Technology Intervention to Support Postabortion Care (The FACTS Study Phase II) After Surgical Abortion: User-Centered Design
  * these are phase 1 and 2 of the same study
* Inhibitory control and mood in relation to psychological resilience: an ecological momentary assessment study
  * 87%, both on GS
  * GS finds 2 copies of this, identical information
  * abstract is heavily different
  * both versions are shown in GS, both have the same system ID in GS
  * both have the same Trial Registration ID (MOH_2018-0-13_002451)
    * likely same publication, but keeping both to be safe
