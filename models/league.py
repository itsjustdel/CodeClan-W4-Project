class League:
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

def sort_teams_by_wins(teams, games):
    # for each team, loop through games and find winning_id matches
    # keep a count of wins per team in a dictionary
    teams_and_wins = []
    for team in teams:
        wins = 0
        for game in games:
            if team.id == game.winning_team.id:
                wins += 1
        # once we have finished goign through all games for this team,
        # save to team and win to list
        teams_and_wins.append((team,wins))
    
    # now sort this list of tuples by wins value 
    teams_and_wins.sort(key=lambda x:x[1], reverse=True)

    return teams_and_wins
