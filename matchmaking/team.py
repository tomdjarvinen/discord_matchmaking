import matchmaking.ranking

class Team():
    def __init__(self,players = None, name = None):
        self.players = players
        self.name = name
        self.ranking = self.get_ranking()
        if players is not None:

            self.active_players = self.players[:3]



    def get_ranking(self):
        """

        :return: Average ranking among players on the team
        """
        if self.players is not None:
            return sum([i.ranking for i in self.players]) / len(self.players)
        else:
            return matchmaking.ranking.DEFAULT_SCORE_ELO

    def add_player(self,player):
        self.players.append(player)

    def is_valid(self):
        return len(self.active_players == 3)

    def set_active_players(self,ids):


class