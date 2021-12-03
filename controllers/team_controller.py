from flask import Flask, render_template, request, redirect, Blueprint
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams",__name__)

@teams_blueprint.route("/teams/")
def teams():
    # show all teams when we get to league page
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)