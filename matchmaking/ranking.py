"""
Methods for ranking players or teams
Currently implemented: Elo
To be implemented: TrueSkill https://proceedings.neurips.cc/paper/2006/file/f44ee263952e65b3610b8ba51229d1f9-Paper.pdf
"""
DEFAULT_SCORE_ELO = 1200

def compute_expected_score_elo(hero,villain):
    """
    Implementation of elo score expectation as defined in:
    https://en.wikipedia.org/wiki/Elo_rating_system
    :param hero: Player whose win expectation is being calculated
    :param villain: Opponent (has expectation 1- returned value)
    :return: Win probability [0.,1.]
    """
    assert hasattr(villain,'rating') and hasattr(hero,'rating')
    return 1. / (1 + pow(10,villain.rating-hero.rating/400))

def compute_score_update_elo(hero,expected_score,actual_score,K=32):
    """
    Implementation of score update equation following:
    https://en.wikipedia.org/wiki/Elo_rating_system

    :param hero: player whose score will be update
    :param expected_score: Expected score for a match or set of matches as computed by compute_expected_score_elo
    :param actual_score: Actual Score for a set of matches
        Note: This treats wins as worth 1 point and draws as worth 0.5
    :param K: Maximum per game score update
    :return:
    """
    assert hasattr(hero,'rating')
    hero.rating += K*(actual_score-expected_score)


