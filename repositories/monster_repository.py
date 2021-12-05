from db.run_sql import run_sql
from models.monster import Monster
from models.team import Team
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
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM monster WHERE id = %s"
    values = [id]
    run_sql(sql, values)