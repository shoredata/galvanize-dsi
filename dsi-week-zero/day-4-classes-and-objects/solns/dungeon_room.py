class DungeonRoom:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.rectangles = []
        self.room = self._make_empty_room()

    def add_rectangle(self, x0, y0, x1, y1):
        new_rectangle = ((x0, y0), (x1, y1))
        self._add_walls(new_rectangle)
        for rectange in self.rectangles:
            self._remove_intersection(new_rectangle, rectange)
        self.rectangles.append(new_rectangle)

    def print_room(self):
        for row in self.room:
            print(' '.join(row))

    def _make_empty_room(self):
        room = []
        for row_idx in range(self.height):
            room.append(['.' for _ in range(self.width)])
        return room

    def _add_walls(self, rectange):
        for coordinate in self._get_wall_idxs(rectange):
            x, y = coordinate
            self.room[x][y] = '#'

    def _remove_intersection(self, new_rectangle, rectangle):
        new_walls = self._get_wall_idxs(new_rectangle)
        old_walls = self._get_wall_idxs(rectangle)
        for coordinate in new_walls:
            if self.is_in_interior_and_not_corner(coordinate, rectangle):
                x, y = coordinate
                self.room[x][y] = '.'
        for coordinate in old_walls:
            if self.is_in_interior_and_not_corner(coordinate, new_rectangle):
                x, y = coordinate
                self.room[x][y] = '.'

    def is_in_interior_and_not_corner(self, coordinates, new_rectangle):
        (rx0, ry0), (rx1, ry1) = new_rectangle
        corner_points = {
            (rx0, ry0), (rx1, ry1), (rx0, ry1), (rx1, ry0)
        }
        x, y = coordinates
        is_in_rectangle = (rx0 <= x < rx1) and (ry0 <= y < ry1)
        is_not_corner = coordinates not in corner_points
        return is_in_rectangle and is_not_corner

    def _get_wall_idxs(self, rectangle):
        (x0, y0), (x1, y1) = rectangle
        wall_idxs = []
        for col_idx in range(y0, y1):
            wall_idxs.append((x0, col_idx))
            wall_idxs.append((x1 - 1, col_idx))
        for row_idx in range(x0, x1):
            wall_idxs.append((row_idx, y0))
            wall_idxs.append((row_idx, y1 - 1))
        return wall_idxs
