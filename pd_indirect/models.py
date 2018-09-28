from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Namun Cho'

doc = """
Continuous Prisoner's Dilemma (random partner, 5 rounds)
"""


class Constants(BaseConstants):
    name_in_url = 'pd_indirect'
    players_per_group = 2
    num_rounds = 5

    betray_payoff = c(40)
    betrayed_payoff = c(10)

    both_cooperate_payoff = c(30)
    both_defect_payoff = c(20)




class Subsession(BaseSubsession):
    """매 라운드마다 랜덤으로 섞는다"""
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
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
    
    def get_coop(self):
        """이전 라운드까지의 협조 횟수를 돌려준다."""
        num_coop = 0
        for p in self.in_previous_rounds():
            if p.decision=="Cooperate":
                num_coop+=1
        return num_coop
