class Player:

    def __init__(self, id,first,last,team,pos,im):
        self.identifier = id
        self.first_name=first
        self.last_name=last
        self.team=team
        self.position = pos
        self.image=im

    def __repr__(self):
        return f"player: {self.first_name} {self.last_name}"