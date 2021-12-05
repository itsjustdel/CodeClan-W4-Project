import random
from models.weather import weathers
from models.name_gen import random_name
from db.run_sql import run_sql
from models.monster import Monster
import repositories.team_repository as team_repository

def save(monster):
    # sql statement
    sql = "INSERT INTO monsters (name, limbs, fav_weather, team_id) VALUES (%s, %s, %s, %s) RETURNING id"
     # values will replace the placeholders "%s" 
    values = [monster.name, monster.limbs, monster.fav_weather, monster.team.id]
    # send off to the db with sql runner
    results = run_sql(sql, values)
    # give our python class back the db asigned as its id
    monster.id = results[0]['id']
    #now return amended league object
    return monster

def select_all():
    monsters = []

    sql = "SELECT * FROM monsters"
    results = run_sql(sql)

    for row in results:
        monster = Monster(row['name'], row['limbs'],row['fav_weather'], row['team_id'], row['id'])
        monsters.append(monster)

    return monsters

def select(id):
    monster = None
    sql = "SELECT * FROM monsters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # create class instance for monster class
        team = team_repository.select(result['team_id'])
        monster = Monster(result['name'], result['limbs'], result['fav_weather'], team, result['id'])
    
    return monster

def delete_all():
    sql = "DELETE FROM monsters"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM monster WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def monsters_from_team(team):
    monsters = []    
    sql = "SELECT * FROM monsters WHERE team_id = %s"    
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        # we can use passed team object in the constructor
        monster = Monster(row['name'], row['limbs'], row['fav_weather'], team, row['id'])
        monsters.append(monster)

    return monsters

def add_monsters(team):
        # 3 monsters per team
        for i in range(3):
            name = random_name()
            limbs = random.randrange(2,10)
            fav_weather = random.choice(weathers)
            monster = Monster(name, limbs, fav_weather, team)
            save(monster)