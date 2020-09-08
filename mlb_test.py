import csv
import sqlite3
from game import Game
from team import Team

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
cursor = conn.cursor()

teams = dict()
team_states = dict()

teamid_file = open('TEAMABR.TXT', 'r')
for line in teamid_file:
    fields = line[:-1].split(',')
    fields = [field.strip('"') for field in fields]
    
    # https://www.retrosheet.org/TEAMABR.TXT
    abr = fields[0]
    league = fields[1]
    city = fields[2]
    nickname = fields[3]
    first_year = fields[4]
    last_year = fields[5]
    teams[abr] = Team(abr, league, city, nickname, first_year, last_year)
teamid_file.close()

year = 2019 # Fixed year for now
gl_file = open('GL' + str(year) + '.TXT', 'r')
for line in csv.reader(gl_file, delimiter = ","):
    game = Game(line)
    if game.attendance == 0:
        print(game.date + ":", game.v_team + "@" + game.h_team)

gl_file.close()
