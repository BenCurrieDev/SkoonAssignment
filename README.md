# skoonUlator


### Setup
#### Live Deployment Available:
[skoonUlator](https://bencurriedev.pythonanywhere.com/)
#### Local install:
Prerequisite installs:
- Python 3.*
- Bash 
- pip
1. Clone the repository:
`$ git clone https://github.com/BenCurrieDev/SkoonAssignment.git`
`$ cd SkoonAssignment`
2. Create a virtual environment to install dependencies and activate it:
`$ python -m venv skoonulator_venv`
`$ . skoonulator_venv/Scripts/activate`
3. Install the dependencies:
`(skoonulator_venv)$ pip install -r requirements.txt`
4. Once dependencies are installed - add local environmental variables:
`(skoonulator_venv)$ echo -e "SECRET_KEY=NOT_THE_PRODUCTION_SECRET_KEYrqr_cjv4igscyu8&&(0ce\nDEBUG=True\nALLOWED_HOSTS=.localhost,127.0.0.1\nDATABASE_URL=sqlite:///db.sqlite3" > .env`
5. Setup database:
`(skoonulator_venv)$ python manage.py migrate`
6. Run server:
`(skoonulator_venv)$ python manage.py runserver`
7. Navigate to [localhost](http://127.0.0.1:8000)


