from flask import Flask, render_template, request, redirect, Blueprint
from models.league import League, sort_teams_by_wins
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository
import repositories.monster_repository as monster_repository
import repositories.game_repository as game_repository
from models.team import Team
teams_blueprint = Blueprint("teams",__name__)

@teams_blueprint.route("/teams/")
def teams():
    # show all teams
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>")
def show(id):    
    # show team
    team = team_repository.select(id)
    # find which league the team is in
    league = league_repository.select(team.league.id)
    # monsters to go here
    monsters = monster_repository.monsters_from_team(team)
    return render_template("teams/show.html",team=team, league=league, monsters=monsters)


# NEW
@teams_blueprint.route("/leagues/<league_id>/new")
def new_team_form(league_id):
    league = league_repository.select(league_id)
    teams = team_repository.teams(league)
    games = game_repository.games_for_league(league)
    # get a list of team names sorted by wins, including wins
    teams_and_wins = sort_teams_by_wins(teams, games)    
    print("route a")
    return render_template("/teams/new.html", league=league, teams_and_wins=teams_and_wins)

@teams_blueprint.route("/leagues/<league_id>/new", methods=['POST'])
def new_team(league_id):  
    print("route b")
    team_name = request.form['team_name']
    league = league_repository.select(league_id)
    team = Team(team_name,league)
    # save this team to db
    team_repository.save(team)
    # now the team has an id, populate team with monsters
    monster_repository.add_monsters(team)
    
    # to show league we need all the teams from league (after we saved the new team to the league)
    teams = team_repository.teams(league)
    # we need all games that have been played
    games = game_repository.games_for_league(league)
    # sort the list
    teams_and_wins = sort_teams_by_wins(teams, games)    
    # and show the sorted league 
    return render_template("leagues/show.html",league=league, teams_and_wins=teams_and_wins)

# EDIT
@teams_blueprint.route("/teams/<team_id>/edit")
def edit_team_form(team_id):
    team = team_repository.select(team_id)
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



# DELETE
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    # get league id from the team we about to delete so we can redirect back to league
    team = team_repository.select(id)
    team_repository.delete(id)
    return redirect("/leagues/" + str(team.league.id)) #url_for TODO