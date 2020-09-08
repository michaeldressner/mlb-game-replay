class TeamStatus():
    def __init__(self):
        self.h = 0
    def increase_attr(self, attr, amount):
        curr = getattr(self, attr)
        setattr(self, attr, curr + amount)
