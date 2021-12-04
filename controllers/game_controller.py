from flask import Flask, render_template, request, redirect, Blueprint
from models.game import Game
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

games_blueprint = Blueprint("games",__name__)

@games_blueprint.route("/games/")
def games():
    # show all games
    games = game_repository.select_all()    
    return render_template("games/index.html", games = games)

@games_blueprint.route("/teams/<id>/games")
def show_team_games(id):    
    # show all games for team
    team = team_repository.select(id)
    games = game_repository.games_for_team(team)
    route = "teams"
    return render_template("games/show.html",route=route, object=team, games=games)

@games_blueprint.route("/leagues/<league_id>/games")
def show_league_games(league_id):
    # show all games for for league
    league= league_repository.select(league_id)
    games = game_repository.games_for_league(league)
    route = "leagues"
    return render_template("games/show.html",route=route, object=league, games=games)

@games_blueprint.route("/leagues/<league_id>/games/new")
def new_game(league_id):
    # to create a new game we need
    # a list of all teams in the league
    league = league_repository.select(league_id)
    teams = team_repository.teams(league)
    
    return render_template("games/new.html", teams=teams, league=league)


@games_blueprint.route("/leagues/<league_id>/games/new", methods=['POST'])
def play_game(league_id):
    # get league
    league = league_repository.select(league_id)    
    # retreive info from form
    home_team = team_repository.select(request.form['home_team_id'])
    away_team = team_repository.select(request.form['away_team_id'])    
    # create a Game object
    game = Game(league,home_team,away_team)
    # play the game and find out who won!
    game.play()
    # save to db
    game_repository.save(game)
    
    return render_template("games/result.html", game=game)