from db.run_sql import run_sql
from models.monster import Monster

# method to save monster to db
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