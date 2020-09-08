from csv import reader

def convert_to_int(field):
    if field != "":
        return int(field)
    else:
        return -1

class Game():
    def __init__(self, fields):
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
        self.attendance = convert_to_int(fields[17])
        self.duration = convert_to_int(fields[18])
        self.v_line = fields[19]
        self.h_line = fields[20]
        self.v_ab = int(fields[21])
        self.v_h = int(fields[22])
        self.v_d = int(fields[23])
        self.v_t = int(fields[24])
        self.v_hr = int(fields[25])
        self.v_rbi = int(fields[26])
        self.v_sh = int(fields[27])
        self.v_sf = int(fields[28])
        self.v_hbp = int(fields[29])
        self.v_w = int(fields[30])
        self.v_iw = int(fields[31])
        self.v_so = int(fields[32])
        self.v_sb = int(fields[33])
        self.v_cs = int(fields[34])
        self.v_gidp = int(fields[35])
        self.v_ci = int(fields[36]) # Catcher interference
        self.v_lob = int(fields[37])
        self.v_pu = int(fields[38]) # Pitchers used
        self.v_ier = int(fields[39]) # Individual earned runs
        self.v_er = int(fields[40]) # Team earned runs
        self.v_wp = int(fields[41])
        self.v_bk = int(fields[42]) # Balks
        self.v_po = int(fields[43])
        self.v_ass = int(fields[44]) # Assists
        self.v_err = int(fields[45])
        self.v_pb = int(fields[46]) # Passed balls
        self.v_dp = int(fields[47])
        self.v_tp = int(fields[48])
        self.h_ab = int(fields[49])
        self.h_h = int(fields[50])
        self.h_d = int(fields[51])
        self.h_t = int(fields[52])
        self.h_hr = int(fields[53])
        self.h_rbi = int(fields[54])
        self.h_sh = int(fields[55])
        self.h_sf = int(fields[56])
        self.h_hbp = int(fields[57])
        self.h_w = int(fields[58])
        self.h_iw = int(fields[59])
        self.h_so = int(fields[60])
        self.h_sb = int(fields[61])
        self.h_cs = int(fields[62])
        self.h_gidp = int(fields[63])
        self.h_ci = int(fields[64]) # Catcher interference
        self.h_lob = int(fields[65])
        self.h_pu = int(fields[66])
        self.h_ier = int(fields[67]) # Individual earned runs
        self.h_er = int(fields[68]) # Team earned runs
        self.h_wp = int(fields[69])
        self.h_bk = int(fields[70]) # Balks
        self.h_po = int(fields[71])
        self.h_ass = int(fields[72]) # Assists
        self.h_err = int(fields[73])
        self.h_pb = int(fields[74]) # Passed balls
        self.h_dp = int(fields[75])
        self.h_tp = int(fields[76])
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
            self.v_starters_pos.append(int(fields[i + 2]))

        self.h_starters_id = [None]
        self.h_starters_name = [None]
        self.h_starters_pos = [None]

        for i in range(132, 159, 3):
            self.h_starters_id.append(fields[i])
            self.h_starters_name.append(fields[i + 1])
            self.h_starters_pos.append(int(fields[i + 2]))

        self.additional_info = fields[159]
        self.acquisition = fields[160]
