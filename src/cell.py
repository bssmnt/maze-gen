from line import Line
from point import Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.window = window
    
    def draw(self, x1, y1, x2, y2, fill_colour="black"):
        if self.window is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.window.draw_line(line, fill_colour)
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.window.draw_line(line, fill_colour)
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.window.draw_line(line, fill_colour)
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.window.draw_line(line, fill_colour)
        
    def draw_move(self, to_cell, undo=False):
        if not undo:
            line_colour = "red"
        else:
            line_colour = "grey"
        
        center_x = ((self.x1 + self.x2) // 2)
        center_y = ((self.y1 + self.y2) // 2)
        center_x_to_cell = ((to_cell.x1 + to_cell.x2) // 2)
        center_y_to_cell= ((to_cell.y1 + to_cell.y2) // 2)

        start = (center_x, center_y)
        end = (center_x_to_cell, center_y_to_cell)

        self.window.draw_line(start, end, line_colour)