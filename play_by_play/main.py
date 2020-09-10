import csv
from player import Player
from team import Team

def get_teams(year):
    """Takes in a year and returns a dictionary of the data from the csv file"""
    teams = dict()
    team_file = open('data/TEAM/TEAM' + str(year), 'r')

    for record in csv.reader(team_file):
        abr = record[0]
        league = record[1]
        city = record[2]
        nickname = record[3]

        teams[abr] = Team(abr, league, city, nickname)

    return teams

def get_roster(year, team):
    """Takes in a year and a team and returns a dictionary that maps the player
    id of each player on the team to their respective player objects. Reads from
    the appropriate csv file."""
    roster = dict()
    roster_file = open('data/ROS/' + team.abr + str(year) + '.ROS')

    for record in csv.reader(roster_file):
        player_id = record[0]
        last_name = record[1]
        first_name = record[2]
        bats = record[3]
        throws = record[4]
        team_abr = record[5]
        pos = record[6]

        roster[player_id] = Player(player_id, last_name, first_name, bats,
                throws, team_abr, pos)

    return roster

def get_games(year, team):
    """Takes in a year and a team and returns a list of game objects. Also
    'sets up' the games by initializing the fields"""
    games = list()
    game_file = open('data/EV/' + str(year) + team.abr + '.EV' + team.league)

    for record in csv.reader(game_file):
        pass

# MAIN PROGRAM

for year in range(2000, 2020):
    teams = get_teams(year)

    for team in teams:
        roster = get_roster(year, teams[team])
        teams[team].set_roster(roster)
