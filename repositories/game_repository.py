from db.run_sql import run_sql
from models.game import Game

# method to save game to db
def save(game):
    # sql statement
    sql = "INSERT into games (result, home_team_id, away_team_id) VALUES (%s, %s, %s) RETURNING ID"
    # values will replace the placeholders "%s" 
    values = [game.result, game.home_team.id, game.away_team.id]
    # send off to the db with sql runner
    results = run_sql(sql, values)
    # give our python class back the db asigned as its id
    game.id = results[0]['id']
    # now returned amended game object
    return game