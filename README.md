# FlaskAppTemplate Deployment GUIDE
Created By :  Bharat Sharma

Date : 29/12/2020

_

### Prerequesites
1. Python3
2. Git
3. Virtualenv

### Setting up the environment

clone FlaskAppTemplate workspace from git into $PROJECT_DIR.

git clone https://github.com/bhrt-sharma/FlaskAppTemplate.git


Change directory to FlaskAppTemplate.

`cd FlaskAppTemplate`

make virtual environment

`virtualenv venv -p python3.8`

activate virtual environment

`source venv/bin/activate`

install required packages

`pip install -r requirements.txt`

make start and stop shell scripts executable

`chmod +x start.sh`


`chmod +x shutdown.sh`

run the app

`./start.sh`

stop the app

`shutdown.sh`
