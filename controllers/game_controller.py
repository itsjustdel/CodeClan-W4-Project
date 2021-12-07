from flask import Flask, render_template, request, redirect, Blueprint
from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository
import repositories.monster_repository as monster_repository
games_blueprint = Blueprint("games",__name__)

@games_blueprint.route("/games/")
def games():
    # show all games
    games = game_repository.select_all()    
    return render_template("games/index.html", games = games)

@games_blueprint.route("/teams/<id>/games/")
def show_team_games(id):    
    # show all games for team
    team = team_repository.select(id)    
    games = game_repository.games_for_team(team)
    route = "teams"
    return render_template("games/show.html",games=games)

@games_blueprint.route("/leagues/<league_id>/games")
def show_league_games(league_id):
    # show all games for for league
    league= league_repository.select(league_id)
    games = game_repository.games_for_league(league)
    route = "leagues"
    return render_template("games/show.html", games=games)

@games_blueprint.route("/leagues/<league_id>/games/new")
def new_game_select_home_team(league_id):
    # to create a new game we need
    # a list of all teams in the league
    league = league_repository.select(league_id)
    teams = team_repository.teams(league)
    
    return render_template("games/new_game_select_home_team.html", teams=teams, league=league)

@games_blueprint.route("/leagues/<league_id>/games/new/next", methods=['POST'])
def new_game_select_away_team(league_id):
    # get league
    league = league_repository.select(league_id)  
    teams = team_repository.teams(league)  
    # retreive info from form
    home_team = team_repository.select(request.form['team_id'])
    return render_template("games/new_game_select_away_team.html", teams=teams, league=league, home_team=home_team)


@games_blueprint.route("/leagues/<league_id>/games/<home_team_id>/result", methods=['POST'])
def new_game_results(league_id,home_team_id):
    # get league
    league = league_repository.select(league_id)        
    # retreive info from url and get from db
    home_team = team_repository.select(home_team_id)
    # retreive info from form    
    away_team = team_repository.select(request.form['team_id'])    
    # create a Game object
    game = Game(league,home_team,away_team)   

    home_team_monsters = monster_repository.monsters_from_team(home_team)
    away_team_monsters =  monster_repository.monsters_from_team(away_team)

    game.play(home_team_monsters,away_team_monsters)
    # save to db
    game_repository.save(game)
    
    return render_template("games/result.html", game=game, league=league)