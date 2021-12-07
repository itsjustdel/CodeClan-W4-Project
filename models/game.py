import repositories.monster_repository as monster_repository
import random

class Game:    
    def __init__(self, league, home_team, away_team, winning_team = None):        
        self.league = league
        self.home_team = home_team
        self.away_team = away_team
        self.winning_team = winning_team                

    def play(self, home_team_monsters,away_team_monsters,weather):
        
        #work out power for each team
        home_team_power = team_power(weather, home_team_monsters)
        away_team_power = team_power(weather, away_team_monsters)

        #home teams wins if there's a draw
        if home_team_power >= away_team_power:
            # save to this instance of the class (self)
            self.winning_team = self.home_team
        else:
            self.winning_team = self.away_team

# helper function for team power
def team_power(weather, monsters):
    power = 0
    for monster in monsters:
        # monsters get double points if they like the weather
        # power is equal to how many limbs they have
        if monster.fav_weather == weather:
            power += monster.limbs * 2
        else:                
            power += monster.limbs

    return power