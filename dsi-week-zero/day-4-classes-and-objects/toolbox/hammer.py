class Hammer(object):
    """A tool for pounding things."""

    def __init__(self, action=str.lower):
        """Create a new Hammer."""
        self.action = action

    def __str__(self):
        """Return a string representation of this Hammer."""
        return "THE MIGHTY HAMMER OF {}".format(self.action)

    def pound(self, thing):
        """Pound a thing.

        Arguments
        ---------
        thing : str
            The thing to pound.

        Run action on thing and return result.
        """
        return self.action(thing)
