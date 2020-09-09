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

for year in range(2019, 2020):
    teams = get_teams(year)
    print(teams)
