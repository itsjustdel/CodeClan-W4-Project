from db.run_sql import run_sql
from models.league import League

# method to save league to db
def save(league):
    # sql statement
    sql = "INSERT INTO leagues (name) VALUES (%s) RETURNING id"
     # values will replace the placeholders "%s" 
    values = [league.name]
    # send off to the db with sql runner
    results = run_sql(sql, values)
    # give our python class back the db asigned as its id
    league.id = results[0]['id']
    #now return amended league object
    return league
