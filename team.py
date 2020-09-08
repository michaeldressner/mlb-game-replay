from team_status import TeamStatus

class Team():
    def __init__(self, team_id, league, city, nickname, first_year, last_year):
        self.id = team_id
        self.league = league
        self.city = city
        self.nickname = nickname
        self.first_year = first_year
        self.last_year = last_year
        self.season = TeamStatus()
        self.career = TeamStatus()
