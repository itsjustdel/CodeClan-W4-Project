import pdb

# import model classes to organise data
from models.league import League
from models.monster import Monster
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
team_1 = Team("Roy and the Ravers", league)
team_2 = Team("Ltnt Tarzan and the Mongrels", league)
monster_1 = Monster("Jimbo", 3, team_1)
monster_2 = Monster("Keano", 6, team_2)
game_1 = Game(team_1, team_2,False, team_1)

league_repository.save(league)
team_repository.save(team_1)
team_repository.save(team_2)
monster_repository.save(monster_1)
monster_repository.save(monster_2)
game_repository.save(game_1)

#pdb.set_trace()
