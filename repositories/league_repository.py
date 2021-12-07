from db.run_sql import run_sql
from models.league import League

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

def select_all():
    leagues = []

    sql = "SELECT * FROM leagues"
    results = run_sql(sql)

    for row in results:
        league = League(row['name'], row['id'])
        leagues.append(league)

    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['name'], result['id'])
    
    return league

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(league):        
    sql = "UPDATE leagues SET name = (%s) WHERE id = %s"
    # replace placeholders with these values
    values = [league.name, league.id]
    # send to db
    run_sql(sql, values)