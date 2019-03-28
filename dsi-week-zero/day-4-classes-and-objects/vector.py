class VectorSegementor:
    def __init__(self.lst):
        self.lst = lst
        
    def segment(self,mask):
        new_list = []
        for m,x in zip(mask,self.lst):
            if m:
                new_list.append(x)
        return new_list

    def sum(self,mask):
        return sum(self.segment(mask))

    def avg(self,mask):
        return avg(self.segment(mask))
