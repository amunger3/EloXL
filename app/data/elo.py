import mpmath as mp

# mpmath init
mp.dps = 15
mp.pretty = True


class Elo:

    def __init__(self, R_tup=(1500, 1500), S_tup=(0.5, 0.5)):
        self.K = 32
        self.R_tup = R_tup
        self.S_tup = S_tup
        self.Q_tup = tuple(map(lambda x: mp.power(10, (x / 400)), self.R_tup))
        self.E_tup = tuple(mp.fdiv(Q_ab, sum(self.Q_tup)) for Q_ab in self.Q_tup)
        self.Rnew = tuple(self.R_tup[i] + self.K * (self.S_tup[i] - self.E_tup[i]) for i in range(2))


# New Expected Scores
def exp_score(R_tup):
    Q_tup = tuple(map(lambda x: mp.power(10, (x / 400)), R_tup))
    E_tup = tuple(mp.fdiv(Q_ab, sum(Q_tup)) for Q_ab in Q_tup)
    return E_tup


# New Rating Updates
def up_rating(R_tup, S_tup):
    K = 32
    E_tup = exp_score(R_tup)
    Rnew = tuple(R_tup[ix] + K * (S_tup[ix] - E_tup[ix]) for ix in range(2))
    return Rnew
