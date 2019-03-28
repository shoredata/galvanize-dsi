class SymmetricDict:
    def __init__(self):
        self.mydict = {}
    def __setitem__(self,key,value):
        self.mydict[key]=value
        self.mydict[value]=key
    def __getitem__(self,key):
        return self.mydict[key]
