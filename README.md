## Smart Resume

[![Build Status](https://travis-ci.com/meshack-mbuvi/resumeio.svg?branch=develop)](https://travis-ci.com/meshack-mbuvi/resumeio)
[![Coverage Status](https://coveralls.io/repos/github/meshack-mbuvi/resumeio/badge.svg?branch=develop)](https://coveralls.io/github/meshack-mbuvi/resumeio?branch=develop)

### Description
This is a personal project borne from the fact that people have to prepare and submit
resumes to companies and/or organisations whenever they are looking for employment.
This project aims to help job seekers a platform where they can generate pdf resumes quickly and conviniently, by providing them with well proven and market ready templates.

### Installation
To ensure smooth functioning of this project, ensure you have install python3 and postgresQL database engine in your machine.
Then follow these steps to have a working copy locally:
  - Clone this repository to your local machine
  - Change your workin directory to the project directory
  - Create a virtual environment in the current directory
  - Activate the above virtual environment
  - Run pip install -r requirements.txt
  - Copy .env-sample to .env and fill it with the database credentials
  - Run python manage.py migrate
  - Run python manage.py runserver
  - Open your browser and navigate to http://127.0.0.1:8000/dashboard/

Enjoy the features provided.

### Support
For any issue encountered that you are not able to resolve by your own, feel free to reach out to [me](meshmbuvi@gmail.com)

### Author
[Meshack Mbuvi](https://github.com/meshack-mbuvi)

### HOSTING
The application is hosted [here](https://smartresumes.herokuapp.com/dashboard/)
