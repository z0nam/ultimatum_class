from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Namun Cho'

doc = """
Simple Chicken Game (HDG) (1 rounds)
"""


class Constants(BaseConstants):
    name_in_url = 'hd_1r'
    players_per_group = 2
    num_rounds = 1

    hawk_payoff = c(100)
    dove_payoff = c(10)

    both_hawk_payoff = c(0)
    both_dove_payoff = c(30)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices = ['겁쟁이', '돌진'],
        doc = """현재 경기자의 결정""",
        widget = widgets.RadioSelect()
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        points_matrix = {
            '겁쟁이': {
                '겁쟁이': Constants.both_dove_payoff,
                '돌진': Constants.dove_payoff
            },
            '돌진': {
                '겁쟁이': Constants.hawk_payoff,
                '돌진': Constants.both_hawk_payoff
            }
        }

        self.payoff = (points_matrix[self.decision][self.other_player().decision])
