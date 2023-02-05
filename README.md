# skoonUlator
## Model walls | calculate U-values and insulation requirements | save your results

### Setup
#### [Live Deployment Available](https://bencurriedev.pythonanywhere.com/)
#### Local install:
Prerequisites:
- pip
- Bash
- Python 3.*

Clone the repository:

```sh
$ git clone https://github.com/BenCurrieDev/SkoonAssignment.git
$ cd SkoonAssignment
```

Create a virtual environment to install dependencies and activate it:

```sh
$ python -m venv skoonulator_venv
$ . skoonulator_venv/Scripts/activate
```

Install the dependencies:

```sh
(skoonulator_venv)$ pip install -r requirements.txt
```

Once dependencies are installed - add local environmental variables:

```sh
(skoonulator_venv)$ echo -e "SECRET_KEY=NOT_THE_PRODUCTION_SECRET_KEYrqr_cjv4igscyu8&&(0ce\nDEBUG=True\nALLOWED_HOSTS=.localhost,127.0.0.1\nDATABASE_URL=sqlite:///db.sqlite3" > .env
```

Setup database:

```sh
(skoonulator_venv)$ python manage.py migrate
```

Run server:

```sh
(skoonulator_venv)$ python manage.py runserver
```

[Navigate to localhost](http://127.0.0.1:8000)


