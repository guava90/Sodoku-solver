/* header */

#include "sudoku.hpp"
#include <iostream>
#include <string>

namespace sodoku {

Sudoku::Sudoku(int board[9][9]) :
  Board()
{
  for (int i = 0; i < 9; ++i) {
    for (int j = 0; j < 9; ++j) {
      this->Board[i][j] = new Tile(board[i][j], std::make_tuple(i, j));
    }
  }
}

Sudoku::~Sudoku() {}

void Sudoku::Print() const {
  if (this->Board == nullptr) {
    std::cout << "The board is empty." << std::endl;
    return;
  }
  for (int i = 0; i < 9; ++i) {
    if (i % 3 == 0) {
      std::cout << "||===|===|===||===|===|===||===|===|===||\n";
    } else {
      std::cout << "||---|---|---||---|---|---||---|---|---||\n";
    }
    std::cout << "||";
    for (int j = 0; j < 9; ++j) {
      std::cout << (this->Board[i][j]->Get_Value() == 0 ? " " :
      std::to_string(this->Board[i][j]->Get_Value())) << ((j) % 3 == 2 ? "||" : "|");
    }
    std::cout << std::endl;
  }

}
}
