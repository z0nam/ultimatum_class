from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Namun Cho'

doc = """
Volunteer Dilemma, 2018.9.28 작성
"""


class Constants(BaseConstants):
    name_in_url = 'volunteer'
    players_per_group = None
    num_rounds = 10

    live_payoff = c(1000)
    call_cost = c(200)
    live_call_payoff = live_payoff - call_cost
    death_payoff = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_call = models.IntegerField(min=0)

    def set_payoffs(self):
        self.total_call = 0
        for p in self.get_players():
            if p.hasCalled:
                self.total_call += 1

        if self.total_call > 0:
            for p in self.get_players():
                if p.hasCalled: # 전화한 경우: 코스트 빼주기
                    p.payoff = Constants.live_call_payoff
                else: # 남이 전화하고 나는 안한 경우
                    p.payoff = Constants.live_payoff
        else: # 아무도 전화하지 않은 경우
            for p in self.get_players():
                p.payoff = Constants.death_payoff

    def get_num_members(self):
        num_players=0
        for p in self.get_players():
            num_players += 1
        return num_players


class Player(BasePlayer):
    hasCalled = models.BooleanField(
        choices = [True, False],
        doc = """현재 경기자의 결정""",
        widget = widgets.RadioSelect()
    )
