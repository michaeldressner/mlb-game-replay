class Game():
    def __init__(self):
        self.visteam = ''
        self.hometeam = ''
        self.site = ''
        self.date = ''
        self.number = ''
        self.starttime = ''
        self.day = ''
        self.usedh = ''
        self.umphome = ''
        self.ump1b = ''
        self.ump2b = ''
        self.ump3b = ''
        self.pitches = ''
        self.oscorer = ''
        self.temp = ''
        self.winddir = ''
        self.windspeed = ''
        self.fieldcond = ''
        self.precip = ''
        self.sky = ''
        self.timeofgame = ''
        self.attendance = ''
        self.wp = ''
        self.lp = ''
        self.save = ''
        self.v_starters = list()
        self.h_starters = list()

    def __repr__(self):
        return self.date + ' - ' + self.visteam + '@' + self.hometeam
