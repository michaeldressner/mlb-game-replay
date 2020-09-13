class Game():
    def __init__(self):
        self.visteam = ''
        self.hometeam = ''
        self.site = ''
        self.date = ''
        self.number = ''
        self.starttime = ''
        # Ambiguous start time in file
        self.ambtime = ''
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
        result =  self.date + ' '

        if self.starttime != -1:
            hour = int(self.starttime / 60)
            minute = self.starttime % 60
            result += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ' '

        result += '- ' + self.visteam + '@' + self.hometeam
        
        return result
