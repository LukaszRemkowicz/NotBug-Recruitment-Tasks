# NotABug requirements tasks

Repository contains 3 projects and one file with small exercises (exercise2_4.py). Notice that every command below have to be use in main project folder.

## DjangoBlog

This is blog app. Site contains landing, register, login, account and article detail pages. In order to run the app, create on your project folder .env file, and fill with required data:

* FLASK_APP=app.py
* SECRET_KEY=**YOUR_SECRET_KEY**
* DB_NAME=**YOUR_DB_NAME**
* DB_USER=**YOUR_DB_USER**
* DB_PASSWORD=**YOUR_DB_PASS**
* DB_HOST=**YOUR_DB_HOSTNAME**


To run application use:
```
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

<br/>

## LocalStorageCars

Application was written in Angular. App allows user to "create" a car with partials for buy. Data are stored in LocalStorage. To run use:

```
npm install
ng serve
```

## Pokemons

Next Angular application. Landing page shows cards with fetched pokemons from site: [PokemonApi](https://pokeapi.co). To run application use:

```
npm install
ng serve
```

## TodoApp

App written in Flask. This is API with REST convencion. Endpoints:

* /task - create task, method: POST, 
* /task?filters=**[args: all | completed | not_completed]**&page_size=**[int]**&current_page=**[int]** - all tasks, method GET, 
* /task/**[id]** - update task, method PUT
* /task/**[id]** - update, method PATCH
* /task/**[id]** - get one task, method: GET
* /task/**[id]** - delete task, method: DELETE

To run app use:
```
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
```

<br/>
<br/>

## How apps looks like?


![alt text](pokemonApp.jpg?raw=true)
![alt text](blog.jpg?raw=true)
![alt text](cars.jpg?raw=true)

