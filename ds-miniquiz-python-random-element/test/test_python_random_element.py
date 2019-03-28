from __future__ import division
from collections import defaultdict
import unittest as unittest
from src.python_random_element import random_element


class TestProblems(unittest.TestCase):

    def test_1_random_element(self):

        n = 50000

        samples = defaultdict(lambda: 0)

        gen_size = 17
        gen = range(gen_size)

        for i in range(n):
            sample = random_element(gen, k=1)
            samples[sample] += 1

        for k, v in samples.items():
            self.assertAlmostEqual(samples[k]/n, 1/gen_size, places=2,
                                   msg="Frequency of outcomes seems to be incorrect.  However, "
                                       "this is a probabilistic test.")
