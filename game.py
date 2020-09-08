class Game():
    def __init__(self, line):
        fields = line[:-1].split(',')
        fields = [field.strip('"') for field in fields]

        # https://www.retrosheet.org/gamelogs/glfields.txt
        self.date = fields[0]
        self.game_type = fields[1]
        self.day_of_week = fields[2]
        self.v_team = fields[3]
        self.v_league = fields[4]
        self.v_game = int(fields[5])
        self.h_team = fields[6]
        self.h_league = fields[7]
        self.h_game = int(fields[8])
        self.v_score = int(fields[9])
        self.h_score = int(fields[10])
        self.outs = int(fields[11])
        self.day_night = fields[12]
        self.completion = fields[13]
        self.forfeit = fields[14]
        self.protest = fields[15]
        self.park_id = fields[16]
        self.attendance = int(fields[17])
        self.duration = int(fields[18])
        self.v_line = fields[19]
        self.h_line = fields[20]
        self.v_AB = int(fields[21])
        self.v_H = int(fields[22])
        self.v_D = int(fields[23])
        self.v_T = int(fields[24])
        self.v_HR = int(fields[25])
        self.v_RBI = int(fields[26])
        self.v_SH = int(fields[27])
        self.v_SF = int(fields[28])
        self.v_HBP = int(fields[29])
        self.v_W = int(fields[30])
        self.v_IW = int(fields[31])
        self.v_SO = int(fields[32])
        self.v_SB = int(fields[33])
        self.v_CS = int(fields[34])
        self.v_GIDP = int(fields[35])
        self.v_CI = int(fields[36]) # Catcher interference
        self.v_LOB = int(fields[37])
        self.v_PU = int(fields[38]) # Pitchers used
        self.v_IER = int(fields[39]) # Individual earned runs
        self.v_ER = int(fields[40]) # Team earned runs
        self.v_WP = int(fields[41])
        self.v_BK = int(fields[42]) # Balks
        self.v_PO = int(fields[43])
        self.v_AS = int(fields[44]) # Assists
        self.v_ERR = int(fields[45])
        self.v_PB = int(fields[46]) # Passed balls
        self.v_DP = int(fields[47])
        self.v_TP = int(fields[48])
        self.h_AB = int(fields[49])
        self.h_H = int(fields[50])
        self.h_D = int(fields[51])
        self.h_T = int(fields[52])
        self.h_HR = int(fields[53])
        self.h_RBI = int(fields[54])
        self.h_SH = int(fields[55])
        self.h_SF = int(fields[56])
        self.h_HBP = int(fields[57])
        self.h_W = int(fields[58])
        self.h_IW = int(fields[59])
        self.h_SO = int(fields[60])
        self.h_SB = int(fields[61])
        self.h_CS = int(fields[62])
        self.h_GIDP = int(fields[63])
        self.h_CI = int(fields[64]) # Catcher interference
        self.h_LOB = int(fields[65])
        self.h_PU = int(fields[66])
        self.h_IER = int(fields[67]) # Individual earned runs
        self.h_ER = int(fields[68]) # Team earned runs
        self.h_WP = int(fields[69])
        self.h_BK = int(fields[70]) # Balks
        self.h_PO = int(fields[71])
        self.h_AS = int(fields[72]) # Assists
        self.h_ERR = int(fields[73])
        self.h_PB = int(fields[74]) # Passed balls
        self.h_DP = int(fields[75])
        self.h_TP = int(fields[76])
        self.home_umpire_id = fields[77]
        self.home_umpire_name = fields[78]
        self.fb_umpire_id = fields[79]
        self.fb_umpire_name = fields[80]
        self.sb_umpire_id = fields[81]
        self.sb_umpire_name = fields[82]
        self.tb_umpire_id = fields[83]
        self.tb_umpire_name = fields[84]
        self.lf_umpire_id = fields[85]
        self.lf_umpire_name = fields[86]
        self.rf_umpire_id = fields[87]
        self.rf_umpire_name = fields[88]
        self.v_manager_id = fields[89]
        self.v_manager_name = fields[90]
        self.h_manager_id = fields[91]
        self.h_manager_name = fields[92]
        self.winning_pitcher_id = fields[93]
        self.winning_pitcher_name = fields[94]
        self.losing_pitcher_id = fields[95]
        self.losing_pitcher_name = fields[96]
        self.saving_pitcher_id = fields[97]
        self.saving_pitcher_name = fields[98]
        self.gw_rbi_batter_id = fields[99]
        self.gw_rbi_batter_name = fields[100]
        self.v_sp_id = fields[101]
        self.v_sp_name = fields[102]
        self.h_sp_id = fields[103]
        self.h_sp_name = fields[104]

        self.v_starters_id = [None]
        self.v_starters_name = [None]
        self.v_starters_pos = [None]

        for i in range(105, 132, 3):
            self.v_starters_id.append(fields[i])
            self.v_starters_name.append(fields[i + 1])
            self.v_starters_pos.append(fields[i + 2])

        self.h_starters_id = [None]
        self.h_starters_name = [None]
        self.h_starters_pos = [None]

        for i in range(132, 159, 3):
            self.h_starters_id.append(fields[i])
            self.h_starters_name.append(fields[i + 1])
            self.h_starters_pos.append(int(fields[i + 2]))

        self.additional_info = fields[159]
        self.acquisition = fields[160]
