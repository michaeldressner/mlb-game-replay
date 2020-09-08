import sqlite3

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
cursor = conn.cursor()

teams = dict()
year = 2019

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
teamid_file.close()

gl_file = open('GL' + str(year) + '.TXT', 'r')
for line in gl_file:
    fields = line[:-1].split(',')
    date = fields[0].strip('"')
    game_type = fields[1].strip('"')
    day_of_week = fields[2].strip('"')
    visiting_team = fields[3].strip('"')
gl_file.close()
