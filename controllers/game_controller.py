from flask import Flask, render_template, request, redirect, Blueprint
import repositories.game_repository as game_repository
import repositories.team_repository as team_repository

games_blueprint = Blueprint("games",__name__)

@games_blueprint.route("/games/")
def games():
    # show all games
    games = game_repository.select_all()    
    return render_template("games/index.html", games = games)

@games_blueprint.route("/games/<id>")
def show(id):    
    # show all games for league
    team = team_repository.select(id)
    games = game_repository.games(team)
    return render_template("games/show.html", team=team, games=games)