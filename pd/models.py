from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Namun Cho'

doc = """
Continuous Prisoner's Dilemma (fixed partner, 10 rounds)
"""


class Constants(BaseConstants):
    name_in_url = 'pd'
    players_per_group = 2
    num_rounds = 1

    betray_payoff = c(40)
    betrayed_payoff = c(10)

    both_cooperate_payoff = c(30)
    both_defect_payoff = c(20)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices = ['Cooperate', 'Defect'],
        doc = """현재 경기자의 결정""",
        widget = widgets.RadioSelect()
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        points_matrix = {
            'Cooperate': {
                'Cooperate': Constants.both_cooperate_payoff,
                'Defect': Constants.betrayed_payoff
            },
            'Defect': {
                'Cooperate': Constants.betray_payoff,
                'Defect': Constants.both_defect_payoff
            }
        }

        self.payoff = (points_matrix[self.decision][self.other_player().decision])
