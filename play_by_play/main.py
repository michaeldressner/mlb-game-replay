import csv
import re
from player import Player
from team import Team
from game import Game

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
    # https://www.retrosheet.org/datause.txt
    game_file = open('data/EV/' + str(year) + team.abr + '.EV' + team.league)
    # curr_game will really hold a Game object soon, not a boolean
    curr_game = False

    for record in csv.reader(game_file):
        record_type = record[0]

        if record_type == 'id':
            if curr_game:
                # Fix start time if necessary (if it was missing that is)
                if curr_game.starttime == '':
                    curr_game.starttime = -1
                games.append(curr_game)
            curr_game = Game()
        elif record_type == 'info':
            info = record[1]
            value = record[2]

            if info == 'starttime':
                am_pm_format = re.search(r'^(\d{1,2}):(\d{2})([AP]M)$', value)
                ambiguous_format = re.search(r'^(\d{1,2}):(\d{2})$', value)

                if value == "0:00PM":
                    curr_game.ambtime = False
                    # Game time unknown
                    seconds = -1
                elif am_pm_format:
                    curr_game.ambtime = False
                    # e.g. 11:05AM, 7:41PM, etc.
                    hour = int(am_pm_format.group(1))
                    minute = int(am_pm_format.group(2))
                    am_pm = am_pm_format.group(3)

                    # Convert to seconds since midnight or noon
                    seconds = (hour % 12) * 60 + minute

                    if am_pm == 'PM':
                        seconds += 12 * 60
                elif ambiguous_format:
                    curr_game.ambtime = True
                    hour = int(ambiguous_format.group(1))
                    minute = int(ambiguous_format.group(2))

                    seconds = (hour % 12) * 60 + minute

                    # We will later adjust this value depending on if it's a
                    # night or day game
                else:
                    # An unhandled format
                    curr_game.ambtime = False
                    seconds = -1
                    print(value)
                    # pass

                curr_game.starttime = seconds
            elif info == 'daynight':
                # If it is a night game and time is ambiguous
                if value == 'night' and curr_game.ambtime:
                    # If game happened 6 AM or later we're going to have to make
                    # it a PM time
                    if curr_game.starttime >= 6 * 60:
                        curr_game.starttime += 12 * 60
            else:
                setattr(curr_game, info, value)

    game_file.close()
    return games

# MAIN PROGRAM

for year in range(1990, 2020):
    teams = get_teams(year)
    games = list()

    for team in teams:
        roster = get_roster(year, teams[team])
        teams[team].set_roster(roster)
        home_games = get_games(year, teams[team])
        games.extend(home_games)

    games.sort(key = lambda game: (game.date, game.starttime))
