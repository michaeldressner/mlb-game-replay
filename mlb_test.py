import sqlite3
from team import Team

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
cursor = conn.cursor()

teams = dict()

teamid_file = open('TEAMABR.TXT', 'r')
for line in teamid_file:
    fields = line[:-1].split(',')
    fields = [field.strip('"') for field in fields]
    print(fields)
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
for line in gl_file:
    fields = line[:-1].split(',')
    fields = [field.strip('"') for field in fields]
    date = fields[0]
    game_type = fields[1]
    day_of_week = fields[2]
    visiting_team = fields[3]
gl_file.close()
