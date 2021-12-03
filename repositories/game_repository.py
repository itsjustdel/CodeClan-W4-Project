from db.run_sql import run_sql
from models.game import Game

# method to save game to db
def save(game):
    # sql statement
    sql = "INSERT into games (home_team_id, away_team_id, draw, winning_team_id) VALUES (%s, %s, %s, %s) RETURNING ID"
    # values will replace the placeholders "%s" 
    values = [game.home_team.id, game.away_team.id, game.draw, game.winning_team.id]
    # send off to the db with sql runner
    results = run_sql(sql, values)
    # give our python class back the db asigned as its id
    game.id = results[0]['id']
    # now returned amended game object
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        game = Game(row['home_team_id'],row['away_team_id'],row['draw'],row['winning_team_id'])
        games.append(game)

    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['home_team_id'],result['away_team_id'],result['draw'],result['winning_team_id'])
    
    return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)