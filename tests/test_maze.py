import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
        self.assertEqual(
            len(m1._cells),
            num_cols
        )

    def test_0_rows(self):
        num_rows = 0
        num_cols = 12
        with self.assertRaises(IndexError):
            Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_0_columns(self):
        num_rows = 12
        num_cols = 0
        with self.assertRaises(IndexError):
            Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_invalid_input_type_string(self):
        with self.assertRaises(TypeError):
            Maze(0, 0, 5, 'f', 10, 10)

    def test_invalid_input_type_float(self):
        with self.assertRaises(TypeError):
            Maze(0, 0, 5, 7.9, 10, 10)

    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                m1._cells[i][j].visited = True
        m1._reset_cells_visited()
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertFalse(m1._cells[i][j].visited)



if __name__ == '__main__':
    unittest.main()