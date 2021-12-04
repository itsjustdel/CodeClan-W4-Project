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

# EDIT
@teams_blueprint.route("/teams/<team_id>/edit")
def edit_team_form(team_id):
    team = team_repository.select(team_id)
    print(team.name)
    return render_template("/teams/edit.html", team=team)

# UPDATE
@teams_blueprint.route("/teams/<team_id>/edit", methods=['POST'])
def update_team(team_id):
    team = team_repository.select(team_id)
    # alter
    team.name = request.form['team_name']
    # update
    team_repository.update(team)
    # return to team page
    return show(team_id)

# NEW
@teams_blueprint.route("/teams/<league_id>/new", methods=['POST'])
def new_team(league_id):        
    team_name = request.form['team_name']
    league = league_repository.select(league_id)
    team = Team(team_name,league)
    team_repository.save(team)
    # show league we added team to
    teams = team_repository.teams(league)
    return render_template("leagues/show.html",league=league, teams=teams)

@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    # grab what league team was in, we will redirect back there after deletion
    league = league_repository.select(id)
    team_repository.delete(id)
    return redirect("/leagues/" + str(league.id)) #url_for TODO