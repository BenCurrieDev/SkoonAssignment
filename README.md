# skoonUlator

## Simple calculation of U-values and insultation requirements

skoonUlator aims to speed up the assessment of insulation requirements. By equiping users with the ability to quickly and easily model the thermal properties of walls, accurate and bespoke insulation requirements can be calculated on the fly.

skoonUlator hopes to provide an improved user experience, eventually leading to lower installment costs for consumers, with the ultimate goal of reducing greenhouse emissions.

## Setup
### [Live Deployment Available](https://bencurriedev.pythonanywhere.com/)
### Installation
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
1. Sign up at:
- Web deployment [signup](https://bencurriedev.pythonanywhere.com/signup/)
- Local installment [signup](http://127.0.0.1:8000/signup/) *(ensure server is running)*

2. Sign in

3. Start calculating *(more information on full feature set below)*

## Features
Admin:

Model instance CRUD operations
- Materials
- Components
- Composites
- Users

Authentication:
- User creation (signup or admin controlled)
- User deletion (admin controlled)
- Login
- Authentication required for app use
- User data not accessible to other users

Calculator:
- Create components
- View components *(graphical and tabular representations)*
- View component R-values
- View U-Values
- Calculate insulation requirements
- Clear components
- Load composites
- Save / create composites
- Close composites

Database:
- View tabulated materials and their respective K-values
- View your saved comoposites *(tabulated)* total depth and U-value
- Delete your saved composites

## Design
### Assumptions

#### User Requirement Assumptions
- User needs to have easy access to app whilst on site
    - Mobile / tablet design first approach preferable
    - Simple UI preferred
- User needs to be able to build up a composite
- User needs to recieve U-values
- User needs to be able to calculate insulation requirements for specific target U-values
- User would benefit greatly from being able to edit their existing composites
    - This feature is not critical and has therefore not yet been implemented due to time constraints

#### Technical Assumptions

Some technical assumptions were made to reduce complexity due to time constraints:
- Effect of thermal bridging (i.e. mortar) negligible *(holds true in majority of cases)*
- No construction defects present (i.e. cold bridging or air gaps)
- No complex geometries (only vertical walls)

### User Interface
- Implemented a mobile first, responsive design
    - No scrolling, aiming to make usage easier, especially when on the move
    - Calculation critical buttons positioned near bottom of the screen to enable easy 1 handed mobile use
    - Automatic U-value updates reduce user input requirements
    - Sleek [skoon](https://skoon.energy/) inspired design

![Image of responsive layout](https://raw.githubusercontent.com/bencurriedev/SkoonAssignment/master/readmeAssets/responsive.jpg?raw=true])

### Models
![Model diagram](https://raw.githubusercontent.com/bencurriedev/SkoonAssignment/master/readmeAssets/models.jpg?raw=true])

## Technology and Learning
### Technologies Used
- Python
- Django *(new to)*
- HTML
- CSS
- Bootstrap (removed from current iteration to give greater control over styles) *(new to)*
- SQLite *(new to)*
- MySQL *(new to)*
- JavaScript

### Main Learnings
- Django
    - Models / views / templates
    - Django template lanquage
    - Authentication and administration
    - Database setup, migrations and querys
    - Back-end development
    - Full-stack deployment

## Planned Features and Improvements
### Planned Features
- Comprehensive test suite
- Enable user to easily edit / delete components from within the calculator page
    - Will require collaboration with designer to find a way to add functionality whilst keeping simplicity
- Enable calculations for more complex geometries i.e. roof to wall joint
- Add greater variety of materials, and enable users to add their own
- Enable savings calculations (financial and emissions)
- Improved save functionality (i.e. introduce save as)

### Planned Improvements
- Use dynamic viewport units to remiove need for JavaScript
- Improve media queries
- Improve database page layout and table sizes at larger screen sizes
- Provide individual browser tab names
- Adjust flex properties currently leading to slight changes in size of calculator graphical and table displays at smaller screen sizes

## Credits
Plans provided by [skoon](https://skoon.energy/)

Logo and favicon owned by [skoon](https://skoon.energy/)
