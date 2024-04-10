# Raising Minds

### Web Application Preview :
  
<!-- ABOUT THE PROJECT -->
## About The Project :

## Link :
<a href ="https://raisingminds.pythonanywhere.com/">https://raisingminds.pythonanywhere.com/</a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Built-with">Built With</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#Installation">Installation</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#Contact">Contact</a></li>
  </ol>
</details>

## Built-with

#### These are the frameworks/libraries used in our project.

* HTML
* CSS
* JavaScript [https://www.javascript.com/]
* Bootstrap [https://www.Bootstrap.com]
* Django [https://www.djangoproject.com/]
* python [https://www.python.org/]


<!-- Features -->
## Features


## Prerequisites

Make sure you have the following software installed before setting up the project:
Python (https://www.python.org/)
Django (https://www.djangoproject.com/)
Web browser (Chrome, Firefox, Safari, etc.)

## Installation

1. Create Virtual Environment
    ```sh
   python -m venv venv
   ```
2. Activate Virtual Environment
   * On Windows
    ```sh
   venv\Scripts\activate
   ```
   * On macOS/Linux
    ```sh
   source venv\bin\activate
   ```
3. Clone the repository to your local machine:
   ```sh
   https://github.com/Coding-Hamsters/RaisingMinds
   ```
4. Find path of Requirement.txt file:
    ```sh
   RaisingMinds/RaisingMinds
   ```
5. Use to following command to install dependencies:
    ```sh
   pip install -r requirements.txt
   ```
6. Install PostgreSQL and Go to the pgadmin and create the database as 'RaisingMinds'

7. Find the location of settings.py
   ```sh
   RaisingMinds/RaisingMinds/RaisingMinds/Settings.py
   ```
8. Update django settings:
   In your Django project's settings('settings.py'),update the 'DATABASES' configuration to use 
   postgreSQL.Repalce 'yourpassword'and Change the USER as 'postgres'.
   
   ```sh
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'RaisingMinds',
        'USER': 'postgres',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
   }
    ```
9. Make Migrations:
   ```sh
   python manage.py makemigrations
   ```
10. Migrate Database:
   ```sh
   python manage.py migrate
   ```
11. Start the Django development server:
  * find path as RaisingMinds/RaisingMinds
   ```sh
   python manage.py runserver
   ```

<!-- CONTRIBUTING -->

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a request.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

<!-- LICENSE -->
## License

Distributed under the MIT License See `LICENSE.txt` for more information.




