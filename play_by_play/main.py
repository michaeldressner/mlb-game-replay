import csv
import re
from player import Player
from team import Team
from game import Game

def fix_start_time(game):
    if game.starttime == '':
        game.starttime = -1
        return

    am_pm_format = re.search(r'^(\d{1,2}):(\d{2})([AP]M)$', game.starttime)
    ambiguous_format = re.search(r'^(\d{1,2}):(\d{2})$', game.starttime)

    if game.starttime == "0:00PM":
        game.ambtime = False
        # Game time unknown
        seconds = -1
    elif am_pm_format:
        game.ambtime = False
        # e.g. 11:05AM, 7:41PM, etc.
        hour = int(am_pm_format.group(1))
        minute = int(am_pm_format.group(2))
        am_pm = am_pm_format.group(3)

        # Convert to seconds since midnight or noon
        seconds = (hour % 12) * 60 + minute

        if am_pm == 'PM':
            seconds += 12 * 60
    elif ambiguous_format:
        game.ambtime = True
        hour = int(ambiguous_format.group(1))
        minute = int(ambiguous_format.group(2))

        seconds = (hour % 12) * 60 + minute
    else:
        # An unhandled format
        game.ambtime = False
        seconds = -1
        print(game.starttime)
        # pass
    
    game.starttime = seconds
    # If it is a night game and time is ambiguous
    if game.daynight == 'night' and game.ambtime:
        # If game happened 6 AM or later we're going to have to make
        # it a PM time
        if game.starttime >= 6 * 60:
            game.starttime += 12 * 60


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

# MAIN PROGRAM

for year in range(1990, 2020):
    teams = get_teams(year)
    games = list()

    # Assemble 'master' list of games for the current year
    for team in teams:
        roster = get_roster(year, teams[team])
        teams[team].set_roster(roster)

        # Get all home games for the team from the appropriate file
        home_games = list()
        # https://www.retrosheet.org/datause.txt
        # https://www.retrosheet.org/eventfile.htm
        game_file = open('data/EV/' + str(year) + teams[team].abr + '.EV' + \
                teams[team].league)
        # curr_game will really hold a Game object soon, not a boolean
        curr_game = False

        for record in csv.reader(game_file):
            record_type = record[0]

            if record_type == 'id':
                if curr_game:
                    fix_start_time(curr_game)
                    home_games.append(curr_game)
                curr_game = Game()
            elif record_type == 'info':
                info = record[1]
                value = record[2]

                setattr(curr_game, info, value)
            elif record_type == 'start':
                pid = record[1]
                name = record[2]
                home_team = True if int(record[3]) == 1 else False
                batting_pos = record[4]
                fielding_pos = record[5]
                print(record)

        # Close the file to avoid memory leak
        game_file.close()
    
        games.extend(home_games)
    # Sort all games by date (primary key) and start time (secondary key)
    games.sort(key = lambda game: (game.date, game.starttime))
