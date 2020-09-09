class Team():
    def __init__(self, abr, league, city, nickname):
        self.abr = abr
        self.league = league
        self.city = city
        self.nickname = nickname

    def __repr__(self):
        return self.city + ' ' + self.nickname
