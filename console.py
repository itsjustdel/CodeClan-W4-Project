import pdb
import random

from models.league import League
from models.team import Team
from models.game import Game
from models.weather import weathers

import repositories.league_repository as league_repository
import repositories.monster_repository as monster_repository
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

league_repository.delete_all()
monster_repository.delete_all()
team_repository.delete_all()
game_repository.delete_all()

league_1 = League("Monster's Mega League")
league_2 = League("Sunday League")

league_repository.save(league_1)
league_repository.save(league_2)

team_1 = Team("The Vlurpon 3", league_1)
team_2 = Team("The Horrendious Howlers", league_1)
team_3 = Team("Wamdazzlers", league_1)

team_4 = Team("Snout Disguisers", league_2)
team_5 = Team("Godzilla's Corpse", league_2)
team_6 = Team("From Small to Big", league_2)
team_7 = Team("Captain Munch's Famous Bozos", league_2)
team_8 = Team("Terrific Flinch", league_2)
team_9 = Team("Spare Incisor", league_2)

teams = [team_1,team_2,team_3,team_4,team_5,team_6,team_7,team_8,team_9]
# save first so we have id
for team in teams:
    team_repository.save(team)

# create and add monsters
monsters = []
for team in teams:
    monsters.append( monster_repository.add_monsters(team))

# seed some games - league 1
game_1 = Game(league_1, teams[0], teams[1])
game_1.play(monsters[0], monsters[1], random.choice(weathers))
game_2 = Game(league_1, teams[1], teams[2])
game_2.play(monsters[1], monsters[2], random.choice(weathers))
game_3 = Game(league_1, teams[0], teams[2])
game_3.play(monsters[0], monsters[2], random.choice(weathers))
game_repository.save(game_1)
game_repository.save(game_2)
game_repository.save(game_3)

# league 2
game_4 = Game(league_2, teams[3], teams[4])
game_4.play(monsters[3], monsters[4], random.choice(weathers))
game_5 = Game(league_2, teams[4], teams[5])
game_5.play(monsters[4], monsters[5], random.choice(weathers))
game_6 = Game(league_2, teams[6], teams[7])
game_6.play(monsters[6], monsters[7], random.choice(weathers))
game_repository.save(game_4)
game_repository.save(game_5)
game_repository.save(game_6)
