from db.run_sql import run_sql
from models.team import Team

import repositories.league_repository as league_repository

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


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'],row['league_id'],row['id'])
        teams.append(team)

    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # get the league object
        league = league_repository.select(result['league_id']) 
        team = Team(result['name'], league , result['id'])
    
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):        
    sql = "UPDATE teams SET name = (%s) WHERE id = %s"
    # replace placeholders with these values
    values = [team.name, team.id]
    # send to db
    run_sql(sql, values)
    
def teams(league):
    teams = []    
    sql = "SELECT * FROM teams WHERE league_id = %s"    
    values = [league.id]
    results = run_sql(sql, values)

    for row in results:
        # league object from id
        league = league_repository.select(league.id)
        team = Team(row['name'],league, row['id'])
        teams.append(team)

    return teams

