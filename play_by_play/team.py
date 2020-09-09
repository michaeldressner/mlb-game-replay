from team_status import TeamStatus

class Team():
    def __init__(self, abr, league, city, nickname):
        self.abr = abr
        self.league = league
        self.city = city
        self.nickname = nickname
        self.status = TeamStatus()

    def set_roster(self, roster):
        self.status.set_roster(roster)

    def __repr__(self):
        return self.city + ' ' + self.nickname
