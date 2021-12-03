from models.team import Team
class Game:
    def __init__(self, home_team, away_team, draw, winning_team = None):        
        self.home_team = home_team
        self.away_team = away_team        
        self.draw = draw
        self.winning_team = winning_team

def play_game(home_team, away_team):
    # game logic!
    pass