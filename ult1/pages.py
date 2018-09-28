# -*- coding: utf-8 -*-
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']
    
    def is_displayed(self):
        return self.player.id_in_group ==1
        
class WaitForProposer(WaitPage):
    pass
    

class Accept(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']
    
    def is_displayed(self):
        return self.player.id_in_group == 2


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Offer,
    WaitForProposer,
    Accept,
    ResultsWaitPage,
    Results
]
