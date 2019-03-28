from __future__ import division
import unittest as unittest
from collections import defaultdict
from src.my_stats import PMF, RV


class TestProblems(unittest.TestCase):

    def test_all_outcomes(self):

        die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })
        die_rv = RV(die)
        self.assertEqual(sorted(die_rv.all_outcomes()), ["1", "2", "3", "4", "5", "6"])

    def test_pmf(self):

        die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })
        die_rv = RV(die)
        self.assertEqual(type(die_rv.pmf()), PMF)

    def test_sample(self):

        n = 50000

        outcomes = defaultdict(lambda: 0)

        die = PMF({"1": 1./12, "2": 3./12, "3": 1./6, "4": 1./6, "5": 2./6})
        die_rv = RV(die)

        for i in range(n):
            self.assertIsNotNone(die_rv.sample())
            outcomes[die_rv.sample()] += 1

        for k, v in outcomes.iteritems():
            self.assertAlmostEqual(die.prob(k), v/n, places=2,
                                   msg="Frequency of outcomes seems to be incorrect.  However, "
                                       "this is a probabilistic test.")
