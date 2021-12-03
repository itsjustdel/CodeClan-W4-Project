from flask import Flask, render_template, request, redirect, Blueprint
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

leagues_blueprint = Blueprint("leagues",__name__)

@leagues_blueprint.route("/leagues")
def leagues():    
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)

@leagues_blueprint.route("/leagues/<id>")
def show(id):    
    teams = team_repository.select_all()
    return render_template("leagues/show.html", teams=teams)