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
    v_team = fields[3]
    v_league = fields[4]
    v_game = int(fields[5])
    h_team = fields[6]
    h_league = fields[7]
    h_game = int(fields[8])
    v_score = int(fields[9])
    h_score = int(fields[10])
    outs = int(fields[11])
    day_night = fields[12]
    completion = fields[13]
    forfeit = fields[14]
    protest = fields[15]
    park_id = fields[16]
    attendance = fields[17]
    duration = fields[18]
    v_line = fields[19]
    h_line = fields[20]
    v_AB = fields[21]
    v_H = fields[22]
    v_D = fields[23]
    v_T = fields[24]
    v_HR = fields[25]
    v_RBI = fields[26]
    v_SH = fields[27]
    v_SF = fields[28]
    v_HBP = fields[29]
    v_W = fields[30]
    v_IW = fields[31]
    v_SO = fields[32]
    v_SB = fields[33]
    v_CS = fields[34]
    v_GIDP = fields[35]
    v_CI = fields[36] # Catcher interference
    v_LOB = fields[37]
    v_PU = fields[38] # Pitchers used
    v_IER = fields[39] # Individual earned runs
    v_ER = fields[40] # Team earned runs
    v_WP = fields[41]
    v_BK = fields[42] # Balks
    v_PO = fields[43]
    v_AS = fields[44] # Assists
    v_ERR = fields[45]
    v_PB = fields[46] # Passed balls
    v_DP = fields[47]
    v_TP = fields[48]
    h_AB = fields[49]
    h_H = fields[50]
    h_D = fields[51]
    h_T = fields[52]
    h_HR = fields[53]
    h_RBI = fields[54]
    h_SH = fields[55]
    h_SF = fields[56]
    h_HBP = fields[57]
    h_W = fields[58]
    h_IW = fields[59]
    h_SO = fields[60]
    h_SB = fields[61]
    h_CS = fields[62]
    h_GIDP = fields[63]
    h_CI = fields[64] # Catcher interference
    h_LOB = fields[65]
    h_PU = fields[66]
    h_IER = fields[67] # Individual earned runs
    h_ER = fields[68] # Team earned runs
    h_WP = fields[69]
    h_BK = fields[70] # Balks
    h_PO = fields[71]
    h_AS = fields[72] # Assists
    h_ERR = fields[73]
    h_PB = fields[74] # Passed balls
    h_DP = fields[75]
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
    v_manager_id = fields[89]
    v_manager_name = fields[90]
    h_manager_id = fields[91]
    h_manager_name = fields[92]
    winning_pitcher_id = fields[93]
    winning_pitcher_name = fields[94]
    losing_pitcher_id = fields[95]
    losing_pitcher_name = fields[96]
    saving_pitcher_id = fields[97]
    saving_pitcher_name = fields[98]
    gw_rbi_batter_id = fields[99]
    gw_rbi_batter_name = fields[100]
    v_sp_id = fields[101]
    v_sp_name = fields[102]
    h_sp_id = fields[103]
    h_sp_name = fields[104]

    v_starters_id = [None]
    v_starters_name = [None]
    v_starters_pos = [None]

    for i in range(105, 132, 3):
        v_starters_id.append(fields[i])
        v_starters_name.append(fields[i + 1])
        v_starters_pos.append(fields[i + 2])

    h_starters_id = [None]
    h_starters_name = [None]
    h_starters_pos = [None]

    for i in range(132, 159, 3):
        h_starters_id.append(fields[i])
        h_starters_name.append(fields[i + 1])
        h_starters_pos.append(fields[i + 2])

    additional_info = fields[159]
    acquisition = fields[160]
    
gl_file.close()
