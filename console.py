import pdb

# # import model classes to organise data
from models.league import League
# from models.monster import Monster
from models.team import Team
from models.game import Game
# import repositories to send sql to db
import repositories.league_repository as league_repository
import repositories.monster_repository as monster_repository
import repositories.team_repository as team_repository
import repositories.game_repository as game_repository

league_repository.delete_all()
monster_repository.delete_all()
team_repository.delete_all()
game_repository.delete_all()

league = League("Top League")

league_repository.save(league)

team_1 = Team("Roy and the Ravers", league)
team_2 = Team("Ltnt Tarzan and the Mongrels", league)
team_3 = Team("Crepescule", league)

# save first so we have id
team_repository.save(team_1)
team_repository.save(team_2)
team_repository.save(team_3)

monster_repository.add_monsters(team_1)
monster_repository.add_monsters(team_2)
monster_repository.add_monsters(team_3)

game_1 = Game(league, team_1, team_2)
game_2 = Game(league, team_2, team_3)
game_3 = Game(league, team_1, team_3)
game_1.play()
game_2.play()
game_3.play()

game_repository.save(game_1)
game_repository.save(game_2)
game_repository.save(game_3)

games = game_repository.games_for_team(team_1)

pdb.set_trace()
