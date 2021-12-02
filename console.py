import pdb

# import model classes to organise data
from models.league import League
from models.monster import Monster
from models.team import Team

# import repositories to send sql to db
import repositories.league_repository as league_repository
import repositories.monster_repository as monster_repository
import repositories.team_repository as team_repository

league = League("Top League")
team = Team("team test", league)
monster_1 = Monster("Jimbo", 3, team)

league_repository.save(league)
team_repository.save(team)
monster_repository.save(monster_1)

#pdb.set_trace()
