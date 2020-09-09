class Player():
    def __init__(self, player_id, last_name, first_name, bats, throws, team,
            pos):
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.bats = bats
        self.throws = throws
        self.team = team
        self.pos = pos

    def __repr__(self):
        return self.pos + ": " + self.first_name + " " + self.last_name + " " \
                + self.bats + "/" + self.throws
