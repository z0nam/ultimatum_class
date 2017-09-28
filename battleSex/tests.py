from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    cases = ['both_baseball', 'mismatch']

    def play_round(self):
        yield (views.Introduction)

        if self.case == 'both_baseball':
            yield (views.Decide, {"decision": 'baseball'})
            if self.player.role() == 'husband':
                assert self.player.payoff == Constants.baseball_husband_payoff
            else:
                assert self.player.payoff == Constants.baseball_wife_payoff

        if self.case == 'mismatch':
            if self.player.role() == 'husband':
                yield (views.Decide, {"decision": 'baseball'})
            else:
                yield (views.Decide, {"decision": 'cinema'})
            assert self.player.payoff == Constants.mismatch_payoff

        yield (views.Results)
