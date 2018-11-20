from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Namun Cho'

doc = """
Oligopoly Game (Equivalent to PDG 1 round)
"""


class Constants(BaseConstants):
    name_in_url = 'oligopoly'
    players_per_group = 2
    num_rounds = 1

    betray_payoff = c(2000)
    betrayed_payoff = c(1500)

    both_cooperate_payoff = c(1800)
    both_defect_payoff = c(1600)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices = ['담합', '담합파기'],
        doc = """현재 경기자의 결정""",
        widget = widgets.RadioSelect()
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        points_matrix = {
            '담합': {
                '담합': Constants.both_cooperate_payoff,
                '담합파기': Constants.betrayed_payoff
            },
            '담합파기': {
                '담합': Constants.betray_payoff,
                '담합파기': Constants.both_defect_payoff
            }
        }

        self.payoff = (points_matrix[self.decision][self.other_player().decision])
