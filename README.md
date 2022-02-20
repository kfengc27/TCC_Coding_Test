# TCC_Coding_Test


### Administrators Account
#### Account 1: chengbin  Password: test123123
#### Account 2: brice	Password: tcc123123

### A few questions

#### 1.	If you had more time, what would you change or focus more on?
- a.	Build API for patient to submit their measurement and access the historical information. 
- b.  Authorization permission for patient and clinician account
- c.  Drawing UML, Sequential, ER Model with better design pattern 
- d.  Doing more Unit Test and User Test 
- e.  Deploy to the server with Docker or Heroku.com
- f.	Documentation of the Project 

#### 2.	Which part of the solution consumed the most amount of time?

- uild account systems for patient and clinician cost me the most amount of time. 

#### 3.	What suggestions do you have for stakeholders in this context that they may not have thought of?
- a. Building Machine Learning Mode Predict based on the history of patient measurement and recommend patient what they should pay attention to?
- b. User a better visualization table to show patient’s information to the clinician 
- c. Integrate location-based service to the APP? 
- d. Online inquiry service for patient
- e. Doing enough user and user journal research, considering the UI UX element of making the APP

### Start process

- 0. git clone git@github.com:kfengc27/TCC_Coding_Test.git

- 1. source env/bin/activate

- 2. sudo pip3 install -r requirements.txt

- 3. cd /TCC_Interview

- 4. python3 manage.py runserver 

#### Create Admin Account

- python3 manage.py createsuperuser

- Admin login page: 127.0.0.1:8000/admin

#### Clinician Login Page 

- Clinician Login Page: http://127.0.0.1:8000/clinician/login

#### Patient Login Page

- Patient Login Page: http://127.0.0.1:8000/clinician/patient/login/


