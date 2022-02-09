# NotABug requirements tasks

Repository contains 3 projects and one file with small exercises (exercise2_4.py)

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

App wrote in Flask. This is API with REST convencion. 

<br/>
<br/>

## How apps looks like?


![alt text](pokemonApp.jpg?raw=true)
![alt text](blog.jpg?raw=true)
![alt text](cars.jpg?raw=true)

