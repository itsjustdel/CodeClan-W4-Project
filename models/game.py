from models.team import Team
class Game:    
    def __init__(self, league, home_team, away_team, draw = None, winning_team = None):        
        self.league = league
        self.home_team = home_team
        self.away_team = away_team        
        self.draw = draw
        self.winning_team = winning_team
        # play game as soon as we create 
        # if we want to create fixtures, need a solution for None type winning_team being saved
        self.play()

    def play(self):
        self.winning_team = self.home_team # GAME LOGIC TO GO HERE TODO
        self.draw = False