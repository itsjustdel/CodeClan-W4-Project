from flask import Flask, render_template, request, redirect, Blueprint
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository

teams_blueprint = Blueprint("teams",__name__)

@teams_blueprint.route("/teams/")
def teams():
    # show all teams when we get to league page
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show(id):    
    team = team_repository.select(id)
    # find which league the team is in
    league = league_repository.select(team.league.id)
    # monsters to go here
    return render_template("teams/show.html",team=team, league=league)