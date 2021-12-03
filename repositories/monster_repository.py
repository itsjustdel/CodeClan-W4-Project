from db.run_sql import run_sql
from models.monster import Monster

def save(monster):
    # sql statement
    sql = "INSERT INTO monsters (name, limbs, team_id) VALUES (%s, %s, %s) RETURNING id"
     # values will replace the placeholders "%s" 
    values = [monster.name, monster.limbs, monster.team.id]
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
        monster = Monster(row['name'], row['limbs'],row['team'],row['id]'])
        monsters.append(monster)

    return monster

def select(id):
    monster = None
    sql = "SELECT * FROM monsters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        monster = Monster(result['name'], result['limbs'], result['team'],result['id'])
    
    return monster

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM monster WHERE id = %s"
    values = [id]
    run_sql(sql, values)
