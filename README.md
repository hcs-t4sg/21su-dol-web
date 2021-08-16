## Content

- [Project Overview](#Project-Overview)
- [Installation & Setup](#Installation-and-Setup)
- [About Office of Disability Employment Policy (ODEP)](#About-ODEP)
- [About Ableist Language](#About-Ableist-Language)
- [About Harvard T4SG](#About-Harvard-Tech-For-Social-Good)
- [Questions?](#Questions?)


## Project Overview

The Office of Disability Employment Policy of the Department of Labor (DOL) is building out an [NLP algorithm](https://github.com/USDepartmentofLabor/ableist-language-detector) that analyzes job posts to understand how accessible they are to people with disabilities—checking whether text skews towards abilities instead of skills. This in an accessibility toolkit or checklist for employers to create awareness and actionable insights to ensure companies are being inclusive to people with disabilities. This project is be part of the Combating AI Bias Toolkit. 

[Harvard Computer Society (HCS) Tech for Social Good](https://socialgood.hcs.harvard.edu/) is tasked to develop a website wrapper so that users can copy/paste text into the browser which would then call the model that the DOL is building and would pass back the results that the model finds. The contributors for this projects are:
- Jamie Lu [Github](https://github.com/lujamie)
- Zad Chin [Github](https://github.com/Iwanttobeatuna)
- Kevin Tan [Github](https://github.com/kevintan250)

##  Installation and Setup

To install, Python Flask module and Docker is required. To install, run the following in your terminal: 
- `git clone https://github.com/lujamie/dol-web.git`

Create virtual environemnt: 

- `python3 -m venv [name of virtual environment]`
- `. [virtualenv]/bin/activate`
- `pip install -r requirements.txt`
- `python -m space download en_core_web_sm`
- `git clone https://github.com/USDepartmentofLabor/ableist-language-detector.git`
- `cd ableist-language-detector`
- `pip install -e .`

The detector module should be installed now! To check you can change back to the `dol-web` directory and run the following in a python prompt:

- [1] `import ableist_language_detector`
- [2] `ableist_language_detector.__version__`
- [Output] `'0.1.0'`

Running on Docker instead of `virtualenv`:
- Directory: `dol-web`
- Docker: `docker compose -f compose-django.yml up --build`

To install Docker, visit [Docker full documentation](https://docs.docker.com/engine/install/ubuntu/).

## About ODEP

The Office of Disability Employment Policy (ODEP) is the only non-regulatory federal agency that promotes policies and coordinates with employers and all levels of government to increase workplace success for people with disabilities.

For more infomation about ODEP, visit [ODEP website](https://www.dol.gov/agencies/odep).

## About Ableist Language

**What is ableist language?**

> Ableist language is language that is offensive to people with disability. It can also refer to language that is derogatory, abusive or negative about disability. Ableism is the systemic exclusion and oppression of people with disability, often expressed and reinforced through language. [[source]](https://pwd.org.au/resources/disability-info/language-guide/ableist-language/)

**Why is this tool important?**

Ableist language in job descriptions can cause people with disabilities to feel excluded from jobs that they are qualified for. This typically occurs when a description references [*abilities*](https://www.onetonline.org/find/descriptor/browse/Abilities/) or enduring attributes of an individual that are unnecessary for the job or for which [accommodations](https://askjan.org/) can be proactively offered instead of focusing on developed [*skills*](https://www.onetonline.org/skills/) that can be acquired to succeed in the role. By identifying ableist language and suggesting alternatives, this tool will support more inclusive hiring practices.

Source: [DOL Ableist Language Detector Github](https://github.com/USDepartmentofLabor/ableist-language-detector)

## About HCS Tech For Social Good

HCS Tech for Social Good is a student group dedicated to empowering student leaders to leverage technology to tackle the world’s big problems. As the hub of social impact tech at Harvard, T4SG’s flagship program provides technical consulting services to nonprofits, government agencies, and social enterprises in order to amplify the work of social impact organizations and provide a space for students to get involved with and inspired by mission-driven tech work. T4SG also engages the community in social impact tech through programs, workshops, events, courses, and more.

**Work With HCS Tech for Social Good**

For more information on how to collaborate and partner with us, please visit our [website](https://socialgood.hcs.harvard.edu/) or [email us](team@sg.hcs.harvard.edu.)


## Questions?
If you have any question trying to run the program, please do not hesitate to contact Harvard T4SG at: [team@sg.hcs.harvard.edu.] Thank you.

