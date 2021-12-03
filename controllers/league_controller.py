from flask import Flask, render_template, request, redirect, Blueprint
import repositories.team_repository as team_repository

league_blueprint = Blueprint("league",__name__)

@league_blueprint.route("/league")
def league():
    # show all teams when we get to league page
    teams = team_repository.select_all()
    return render_template("league/index.html", teams=teams)