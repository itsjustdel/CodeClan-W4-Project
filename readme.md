# Sports Scoring App

My brief was to design and build a full stack app which allowed the user to create, edit and remove teams in a league, create and play games and show the results and also show a league table.

Technologies used:  
[Psycopg2](https://github.com/psycopg/psycopg) - PostgreSQL Database Adapter   
[Flask](https://github.com/pallets/flask) - Web app framework

The project brief stipulated that no javascript was to be used.

## Usage
From terminal
```python
# create database
createdb monster_db
psql -d monster_db -f db/monster_db.sql

# seed database
python3 console.py

# run web webserver 
flask run
```

From browser
```html
http://localhost:5000/
```

## License
[MIT](https://choosealicense.com/licenses/mit/)