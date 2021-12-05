from flask import Flask, render_template, request, redirect, Blueprint
from models.league import League, sort_teams_by_wins
from models.team import Team
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

leagues_blueprint = Blueprint("leagues",__name__)

@leagues_blueprint.route("/leagues")
def leagues():    
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)

@leagues_blueprint.route("/leagues/<id>")
def show(id):    
    league = league_repository.select(id)
    teams = team_repository.teams(league)
    games = game_repository.games_for_league(league)
    teams_and_wins = sort_teams_by_wins(teams, games)
    return render_template("leagues/show.html",league=league, teams_and_wins=teams_and_wins)


@leagues_blueprint.route("/leagues/new")
def new_league_form():
    return render_template("/leagues/new.html")

@leagues_blueprint.route("/leagues/new", methods=['POST'])
def new_league():        
    league_name = request.form['league_name']
    league = League(league_name)
    league_repository.save(league)    
    return leagues()

# DELETE
@leagues_blueprint.route("/leagues/<id>/delete", methods=['POST'])
def delete_team(id):
    league_repository.delete(id)
    return leagues()


# EDIT
@leagues_blueprint.route("/leagues/<league_id>/edit")
def edit_league_form(league_id):
    league = league_repository.select(league_id)    
    return render_template("/leagues/edit.html", league=league)

# UPDATE
@leagues_blueprint.route("/leagues/<league_id>/edit", methods=['POST'])
def update_league(league_id):
    league = league_repository.select(league_id)
    # alter
    league.name = request.form['league_name']
    # update
    league_repository.update(league)
    # return to team page
    return show(league_id)
