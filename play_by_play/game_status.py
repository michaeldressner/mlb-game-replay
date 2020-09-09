class GameStatus():
    def __init__(self):
        self.inning = 1
        self.inning_top = True
        self.outs = 0
        self.batter = None
        self.bat_slot = 1 # The current batter position in the batting order
        self.v_fielders = [None] * 9
        self.h_fielders = [None] * 9
        self.v_batters = [None] * 9
        self.h_batters = [None] * 9
        self.v_score = 0
        self.h_score = 0
