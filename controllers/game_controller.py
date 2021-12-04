from flask import Flask, render_template, request, redirect, Blueprint
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

games_blueprint = Blueprint("games",__name__)

@games_blueprint.route("/games/")
def games():
    # show all games
    games = game_repository.select_all()    
    return render_template("games/index.html", games = games)

@games_blueprint.route("/games/teams/<id>")
def show_team_games(id):    
    # show all games for team
    team = team_repository.select(id)
    games = game_repository.games_for_team(team)
    return render_template("games/show.html", team=team, games=games)

@games_blueprint.route("/games/<league_id>")
def show_league_games(league_id):
    # show all games for for league
    league= league_repository.select(league_id)
    games = game_repository.games_for_league(league)
    return render_template("games/show.html", team=league, games=games)