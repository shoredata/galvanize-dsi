
class DungeonRoom:

    def __init__(self,xmax,ymax):
        self.max_x = ymax
        self.max_y = xmax
        self.tiles=[['.' for _ in range(xmax)] for _ in range(ymax)]

    # def add_rectangle(self,ulx,uly,lrx,lry):
    #     self.tiles=[['#' for _ in range(ulx, lrx)] for _ in range(uly,lry)]
    #     return None

    def print_room(self):
        for row in self.tiles:
            print(' '.join(row))
