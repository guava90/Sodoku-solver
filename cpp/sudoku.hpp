/* Header file for Sudoku class */

#pragma once

#include "tile.hpp"

namespace sodoku {
class Sudoku {
public:
  Sudoku(int board[9][9]);
  ~Sudoku();

  void Print() const;

private:
  Tile* Board[9][9];

};
}
