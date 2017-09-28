from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a 2-player 2-strategy coordination game. The name and story originated
from
<a href="http://books.google.ch/books?id=uqDDAgAAQBAJ&lpg=PP1&ots=S-DC4LemnS&lr&pg=PP1#v=onepage&q&f=false" target="_blank">
    Luce and Raiffa (1957)
</a>.

This code is written by contributers of otree at github (sa​mple game)
"""


class Constants(BaseConstants):
    name_in_url = 'battleSex'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'battleSex/Instructions.html'

    # """Amount rewarded to husband if baseball is chosen"""
    baseball_husband_payoff = cinema_wife_payoff = c(300)

    # Amount rewarded to wife if baseball is chosen
    baseball_wife_payoff = cinema_husband_payoff = c(200)

    # amount rewarded to either if the choices don't match
    mismatch_payoff = c(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        husband = self.get_player_by_role('남편')
        wife = self.get_player_by_role('아내')

        if husband.decision != wife.decision:
            husband.payoff = Constants.mismatch_payoff
            wife.payoff = Constants.mismatch_payoff

        else:
            if husband.decision == '야구':
                husband.payoff = Constants.baseball_husband_payoff
                wife.payoff = Constants.baseball_wife_payoff
            else:
                husband.payoff = Constants.cinema_husband_payoff
                wife.payoff = Constants.cinema_wife_payoff


class Player(BasePlayer):
    decision = models.CharField(
        choices=['야구', '영화'],
        doc="""Either 야구 or 영화""",
        widget=widgets.RadioSelect()
    )

    def other_player(self):
        """Returns other player in group"""
        return self.get_others_in_group()[0]

    def role(self):
        if self.id_in_group == 1:
            return '남편'
        if self.id_in_group == 2:
            return '아내'
