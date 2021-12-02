from flask import Flask, render_template

from controllers.league_controller import league_blueprint
from controllers.team_controller import teams_blueprint
from controllers.monster_controller import monsters_blueprint

app = Flask(__name__)

app.register_blueprint(league_blueprint)
app.register_blueprint(team_blueprint)
app.register_blueprint(monster_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)