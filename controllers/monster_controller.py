from flask import Flask, render_template, request, redirect, Blueprint
import repositories.monster_repository as monster_repository
import repositories.team_repository as team_repository
import repositories.league_repository as league_repository
monsters_blueprint = Blueprint("monsters",__name__)

@monsters_blueprint.route("/monsters/")
def monsters():
    # show all monsters
    monsters = monster_repository.select_all()
    return render_template("monsters/index.html", monsters=monsters)

@monsters_blueprint.route("/monsters/<id>")
def show(id):    
    # show monster info
    monster = monster_repository.select(id)
    # find team by monster
    team = team_repository.select(monster.team.id)
    # find which team the monster is in
    league = league_repository.select(monster.team.league.id)
    # monsters to go here
    return render_template("monsters/show.html",monster=monster, team=team, league=league)


# @teams_blueprint.route("/<league_id>/teams/new")
# def new_team_form(league_id):
#     league = league_repository.select(league_id)
#     return render_template("/teams/new.html", league=league)

# # EDIT
# @teams_blueprint.route("/teams/<team_id>/edit")
# def edit_team_form(team_id):
#     team = team_repository.select(team_id)
#     return render_template("/teams/edit.html", team=team)

# # UPDATE
# @teams_blueprint.route("/teams/<team_id>/edit", methods=['POST'])
# def update_team(team_id):
#     team = team_repository.select(team_id)
#     # alter
#     team.name = request.form['team_name']
#     # update
#     team_repository.update(team)
#     # return to team page
#     return show(team_id)

# # NEW
# @teams_blueprint.route("/<league_id>/teams/new", methods=['POST'])
# def new_team(league_id):        
#     team_name = request.form['team_name']
#     league = league_repository.select(league_id)
#     team = Team(team_name,league)
#     team_repository.save(team)
#     # show league we added team to
#     teams = team_repository.teams(league)
#     return render_template("leagues/show.html",league=league, teams=teams)

# # DELETE
# @teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
# def delete_team(id):
#     # get league id from the team we about to delete so we can redirect back to league
#     team = team_repository.select(id)
#     team_repository.delete(id)
#     return redirect("/leagues/" + str(team.league.id)) #url_for TODO