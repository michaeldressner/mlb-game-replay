import sqlite3
from team import Team

conn = sqlite3.connect('lahmansbaseballdb.sqlite')
cursor = conn.cursor()

teams = dict()

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
for line in gl_file:
    fields = line[:-1].split(',')
    fields = [field.strip('"') for field in fields]

    # https://www.retrosheet.org/gamelogs/glfields.txt
    date = fields[0]
    game_type = fields[1]
    day_of_week = fields[2]
    visiting_team = fields[3]
    visiting_league = fields[4]
    visiting_game = int(fields[5])
    home_team = fields[6]
    home_league = fields[7]
    home_game = int(fields[8])
    visiting_score = int(fields[9])
    home_score = int(fields[10])
    outs = int(fields[11])
    day_night = fields[12]
    completion = fields[13]
    forfeit = fields[14]
    protest = fields[15]
    park_id = fields[16]
    attendance = fields[17]
    duration = fields[18]
    visiting_line = fields[19]
    home_line = fields[20]
    visiting_AB = fields[21]
    visiting_H = fields[22]
    visiting_D = fields[23]
    visiting_T = fields[24]
    visiting_HR = fields[25]
    visiting_RBI = fields[26]
    visiting_SH = fields[27]
    visiting_SF = fields[28]
    visiting_HBP = fields[29]
    visiting_W = fields[30]
    visiting_IW = fields[31]
    visiting_SO = fields[32]
    visiting_SB = fields[33]
    visiting_CS = fields[34]
    visiting_GIDP = fields[35]
    visiting_CI = fields[36] # Catcher interference
    visiting_LOB = fields[37]
    visiting_PU = fields[38]
    visiting_IER = fields[39] # Individual earned runs
    visiting_ER = fields[40] # Team earned runs
    visiting_WP = fields[41]
    visiting_BK = fields[42] # Balks
    visiting_PO = fields[43]
    visiting_AS = fields[44] # Assists
    visiting_ERR = fields[45]
    visiting_PB = fields[46] # Passed balls
    visiting_DP = fields[47]
    visiting_TP = fields[48]
    home_AB = fields[49]
    home_H = fields[50]
    home_D = fields[51]
    home_T = fields[52]
    home_HR = fields[53]
    home_RBI = fields[54]
    home_SH = fields[55]
    home_SF = fields[56]
    home_HBP = fields[57]
    home_W = fields[58]
    home_IW = fields[59]
    home_SO = fields[60]
    home_SB = fields[61]
    home_CS = fields[62]
    home_GIDP = fields[63]
    home_CI = fields[64] # Catcher interference
    home_LOB = fields[65]
    home_PU = fields[66]
    home_IER = fields[67] # Individual earned runs
    home_ER = fields[68] # Team earned runs
    home_WP = fields[69]
    home_BK = fields[70] # Balks
    home_PO = fields[71]
    home_AS = fields[72] # Assists
    home_ERR = fields[73]
    home_PB = fields[74] # Passed balls
    home_DP = fields[75]
    home_TP = fields[76]
    home_umpire_id = fields[77]
    home_umpire_name = fields[78]
    fb_umpire_id = fields[79]
    fb_umpire_name = fields[80]
    sb_umpire_id = fields[81]
    sb_umpire_name = fields[82]
    tb_umpire_id = fields[83]
    tb_umpire_name = fields[84]
    lf_umpire_id = fields[85]
    lf_umpire_name = fields[86]
    rf_umpire_id = fields[87]
    rf_umpire_name = fields[88]
    visiting_manager_id = fields[89]
    visiting_manager_name = fields[90]
    home_manager_id = fields[91]
    home_manager_name = fields[92]
    winning_pitcher_id = fields[93]
    winning_pitcher_name = fields[94]
    losing_pitcher_id = fields[95]
    losing_pitcher_name = fields[96]
    saving_pitcher_id = fields[97]
    saving_pitcher_name = fields[98]
    gw_rbi_batter_id = fields[99]
    gw_rbi_batter_name = fields[100]
    visiting_sp_id = fields[101]
    visiting_sp_name = fields[102]
    home_sp_id = fields[103]
    home_sp_name = fields[104]

    visiting_starters_id = [None]
    visiting_starters_name = [None]
    visiting_starters_pos = [None]

    for i in range(105, 132, 3):
        visiting_starters_id.append(fields[i])
        visiting_starters_name.append(fields[i + 1])
        visiting_starters_pos.append(fields[i + 2])

    home_starters_id = [None]
    home_starters_name = [None]
    home_starters_pos = [None]

    for i in range(132, 159, 3):
        home_starters_id.append(fields[i])
        home_starters_name.append(fields[i + 1])
        home_starters_pos.append(fields[i + 2])

    additional_info = fields[159]
    acquisition = fields[160]
    
gl_file.close()
