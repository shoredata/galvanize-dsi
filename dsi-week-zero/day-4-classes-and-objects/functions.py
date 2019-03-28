import numpy as np
import collections

class PrefixAndSuffixStamper:
    def __init__(self,prefix,suffix):
        self.prefix=prefix
        self.suffix=suffix
    def prestamp(self,tostamp):
        return self.prefix + " " + tostamp
    def poststamp(self,tostamp):
        return tostamp + " " + self.suffix
    def stamp(self,tostamp):
        return self.prefix + " " + tostamp + " " + self.suffix

class ReverseList:
    def __init__(self,lstin):
        self.mylist=lstin
    def index(self,idx):
        return mylist[len(mylist)-idx-1]
