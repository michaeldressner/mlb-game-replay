import csv
from team import Team

def get_teams(year):
    """Takes in a year and returns a dictionary of the data from the csv file"""
    teams = dict()
    team_file = open('data/TEAM/TEAM' + str(year), 'r')

    for team in csv.reader(team_file):
        abr = team[0]
        league = team[1]
        city = team[2]
        nickname = team[3]

        teams[abr] = Team(abr, league, city, nickname)

    return teams

def get_roster(year, team):
    """Takes in a year and a team and returns a dictionary that maps the player
    id of each player on the team to their respective player objects. Reads from
    the appropriate csv file."""
    pass

# MAIN PROGRAM

for year in range(2019, 2020):
    teams = get_teams(year)
