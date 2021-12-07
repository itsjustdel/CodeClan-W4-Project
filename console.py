import pdb
import random

# # import model classes to organise data
from models.league import League
# from models.monster import Monster
from models.team import Team
from models.game import Game
from models.weather import weathers
# import repositories to send sql to db
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

team_list = [team_1,team_2,team_3,team_4,team_5,team_6,team_7,team_8,team_9]
# save first so we have id
for team in team_list:
    team_repository.save(team)

# create and add monsters
monsters_list = []
for team in team_list:
    monsters = monster_repository.add_monsters(team)
    
# monsters_1 = monster_repository.add_monsters(team_1)
# monsters_2 = monster_repository.add_monsters(team_2)
# monsters_3 = monster_repository.add_monsters(team_3)
# monsters_4 = monster_repository.add_monsters(team_4)


game_1 = Game(league_1, team_1, team_2)
game_2 = Game(league_1, team_2, team_3)
game_3 = Game(league_1, team_1, team_3)

game_1.play(monsters_1, monsters_2, random.choice(weathers))
game_2.play(monsters_2, monsters_3, random.choice(weathers))
game_3.play(monsters_1, monsters_3, random.choice(weathers))

game_repository.save(game_1)
game_repository.save(game_2)
game_repository.save(game_3)

games = game_repository.games_for_team(team_1)

# pdb.set_trace()
