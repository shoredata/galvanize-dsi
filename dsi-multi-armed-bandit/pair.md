## Multi-Armed Bandt

**Include your code and answers in** `src/pair.py`.

1. Fill in the code stubs in `banditstrategy.py`. The `Bandits` class (completed) is in `bandits.py`. You can simulate running the multi-arm bandit with the following code. We are creating three versions of the site with conversion rates of 5%, 3% and 6%. So hopefully we learn that the last one is the best!

    ```python
    from bandits import Bandits
    from banditstrategy import BanditStrategy

    bandits = Bandits([0.05, 0.03, 0.06])
    strat = BanditStrategy(bandits, 'random_choice')
    strat.sample_bandits(1000)
    print("Number of trials: ", strat.trials)
    print("Number of wins: ", strat.wins)
    print("Conversion rates: ", strat.wins / strat.trials)
    print("A total of %d wins of %d trials." % \
        (strat.wins.sum(), strat.trials.sum()))
    ```

    Fill in the code stubs to implement the four strategies: epsilon-greedy, softmax, ucb1 and bayesian bandits. Take a look at the lecture notes if you need a reminder of any of the strategies.

    If you need a reminder of how any of the algorithms work, take a look at the [lecture notes](https://github.com/gschool/DSI_Lectures/blob/master/multi-armed-bandit/bayesian_ab_testing_slides.pdf). 

2. See how many wins you have of the 1000 trials using each of the six strategies (two already implemented) with the starting bandits given above.

    Try running it again with all of these values and see how different each algorithm does with respect to total number of wins in 1000 rounds.

    ```
    [0.1, 0.1, 0.1, 0.1, 0.9]
    [0.1, 0.1, 0.1, 0.1, 0.12]
    [0.1, 0.2, 0.3, 0.4, 0.5]
    ```

3. Here is a function to calculate the regret after each iteration.

    ```python
    import numpy as np

    def regret(probabilities, choices):
        '''
        INPUT: array of floats (0 to 1), array of ints
        OUTPUT: array of floats

        Take an array of the true probabilities for each machine and an
        array of the indices of the machine played at each round.
        Return an array giving the total regret after each round.
        '''
        p_opt = np.max(probabilities)
        return np.cumsum(p_opt - probabilities[choices])
    ```

    Make sure that you give `probabilities` as a *numpy array* and `choices` as a numpy array *of ints*.

    Use matplotlib to plot the total regret over time of each algorithm. Use the Bandits with these hidden probabilities: `[0.05, 0.03, 0.06]`

4. Now plot the percentage of time the optimal bandit was chosen over time.

5. ***[Extra Credit]*** Experiment with the number of trials and hidden probabilities to compare the four strategies you implemented:
    * epsilon-greedy
    * softmax
    * ucb1
    * bayesian bandits

Given a variety of situations (number of trials, difference in conversion rate) which one performs better? Why?
