from flask import Flask, render_template, request, redirect, Blueprint
import repositories.game_repository as game_repository

games_blueprint = Blueprint("games",__name__)

@games_blueprint.route("/games/")
def games():
    # show all teams when we get to league page
    games = game_repository.select_all()
    for game in games:
        print(game.home_team.name)
    return render_template("games/index.html", games = games)