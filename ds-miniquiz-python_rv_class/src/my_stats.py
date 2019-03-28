

class PMF(object):

    def __init__(self, d={1: .5, 0: .5}):
        self.d = d

    def prob(self, val):
        return self.d[val]

    def set(self, key_val):

        key, val = key_val

        self.d[key] = val

        factor = 1. / sum(self.d.values())

        # Iterate PMF and normalize
        for key, val in self.d.iteritems():
            self.d[key] = val * factor

    def __str__(self):
        return str(self.d.items())


class RV(object):

    def __init__(self, pmf):
        pass

    def sample(self):
        pass

    def pmf(self):
        pass

    def all_outcomes(self):
        pass

