# -*- coding: utf-8 -*-
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Namun Cho'

doc = """
최후통첩게임
"""


class Constants(BaseConstants):
    name_in_url = 'ult'
    players_per_group = 2
    num_rounds = 1

    endowment = c(1000)
    payoff_if_rejected=c(0)
    offer_increment = c(100)
    
    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choicese_count = len(offer_choices)
    
    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))

class Subsession(BaseSubsession):
	pass

class Group(BaseGroup):
    use_strategy = models.BooleanField(
        doc="""전략방식을 썼는지 여부"""
    )
    
    amount_offered = models.CurrencyField(choices=Constants.offer_choices)
    
    offer_accepted = models.BooleanField(
        doc="제안받은 금액이 수용되었는지 여부"
    )
    
    response_0 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_100 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_200 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_300 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_400 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_500 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_600 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_700 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_800 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_900 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_1000 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    
    def set_payoffs(self):
        p1,p2 = self.get_players()
        
        if self.use_strategy:
            self.offer_accepted = getattr(self, 'response_{}'.format(
                int(self.amount_offered)))
            
        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    pass
