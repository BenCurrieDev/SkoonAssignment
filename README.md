# [skoonUlator](https://bencurriedev.pythonanywhere.com/)

## Simple calculation of U-values and insultation requirements

skoonUlator aims to speed up the assessment of insulation requirements. By equiping users with the ability to quickly and easily model the thermal properties of walls, accurate and bespoke insulation requirements can be calculated on the fly.

skoonUlator hopes to provide an improved user experience, eventually leading to lower installment costs for consumers, with the ultimate goal of reducing greenhouse emissions.

## Setup
### [Live Deployment Available](https://bencurriedev.pythonanywhere.com/)
### Installation:
Requirements:
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

Navigate to [127.0.0.1:8000](http://127.0.0.1:8000)


## Usage
Sign up at:
- Web deployment [signup](https://bencurriedev.pythonanywhere.com/signup/)
- Local installment [signup](http://127.0.0.1:8000/signup/) *ensure server is running*

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```

## Credits
Plans provided by [skoon](https://skoon.energy/)
Logo and favicon owned by [skoon](https://skoon.energy/)

## Features
If your project has a lot of features, list them here.


## Tests


