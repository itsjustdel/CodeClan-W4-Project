from flask import Flask, render_template, request, redirect, Blueprint
from models.league import League
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository
from models.team import Team
teams_blueprint = Blueprint("teams",__name__)

@teams_blueprint.route("/teams/")
def teams():
    # show all teams
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show(id):    
    # show teams from league
    team = team_repository.select(id)
    # find which league the team is in
    league = league_repository.select(team.league.id)
    # monsters to go here
    return render_template("teams/show.html",team=team, league=league)


@teams_blueprint.route("/teams/<league_id>/new")
def new_team_form(league_id):
    league = league_repository.select(league_id)
    return render_template("/teams/new.html", league=league)

@teams_blueprint.route("/teams/<league_id>/new", methods=['POST'])
def new_team(league_id):        
    team_name = request.form['team_name']
    league = league_repository.select(league_id)
    team = Team(team_name,league)
    team_repository.save(team)
    # show league we added team to
    teams = team_repository.teams(league)
    return render_template("leagues/show.html",league=league, teams=teams)