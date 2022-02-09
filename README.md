# NotABug requirements tasks

Repository contains 3 project and one file with small exercises

## DjangoBlog

This is a small blog aplication. Site contains only landing, register, login, account pages. To run it, create .env file and fill with required data (in settings.py). Data required: 
* FLASK_APP=app.py
* SECRET_KEY
* DB_NAME
* DB_USER
* DB_PASSWORD
* DB_HOST

To run application use 
```
pip install -r requirements.txt
python manage.py runserver
```

## LocalStorageCars

Application wrote in Angular. App allows user to "create" a car with partials for buy. Data are stored in LocalStorage. To run application use 
```
npm install
ng serve
```

## Pokemons

Website wrote in Angular. Landing page shows cards with fetched pokemons from site: [PockemonApi](https://pokeapi.co). To run application use 
```
npm install
ng serve
```

## TodoApp

App wrote in Flask. This is just API with REST API convencion. To test it use for example Postman.

<br/>
<br/>

## How apps looks like?


![alt text](https://github.com/LukaszRemkowicz/NotBug-Recruitment-Tasks\pokemonApp.jpg)