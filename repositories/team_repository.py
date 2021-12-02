from db.run_sql import run_sql
from models.team import Team

# method to save team to the db
def save(team):
    # sql statement
    sql = "INSERT INTO teams(name, league_id) VALUES (%s, %s) RETURNING id"
    # values will replace the placeholders "%s" 
    values = [team.name, team.league.id]
    # send off to the db with sql runner
    results = run_sql(sql, values)
    # give our python class back the db asigned as its id
    team.id = results[0]['id']
    #now return amended team object
    return team

