from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Call(Page):
    form_model = 'player'
    form_fields = ['hasCalled']


class ResultsWaitPage(WaitPage):

    body_text = "참가자들이 결정을 할 때까지 기다려 주세요"

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        if self.player.hasCalled:
            my_decision = "전화를 걸었습니다."
        else:
            my_decision = "전화를 걸지 않았습니다."
        return{
            'my_decision':my_decision,
            'total_call':self.group.total_call,
            'dead':self.group.total_call==0,
            'total_members':self.group.get_num_members()
        }


page_sequence = [
    Call,
    ResultsWaitPage,
    Results
]
