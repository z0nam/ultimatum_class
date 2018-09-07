from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    body_text = '상대 참가자가 결정을 할때까지 기다려 주세요'

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        self.player.set_payoff()

        return{
            'my_decision': self.player.decision.lower(),
            'other_player_decision': self.player.other_player().decision.lower(),
            'same_choice': self.player.decision == self.player.other_player().decision,
        }


page_sequence = [
    Decision,
    ResultsWaitPage,
    Results
]
