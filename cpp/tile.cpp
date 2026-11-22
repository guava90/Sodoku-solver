/* Implementation file for Tile class */

#include "tile.hpp"

namespace sodoku {

Tile::Tile(int value, std::tuple<int, int> position) :
  Value(value),
  Position(position) {}

Tile::~Tile() {}

int Tile::Get_Value() const {
  return this->Value;
}

std::tuple<int, int> Tile::Get_Position() const {
  return this->Position;
}

} // namespace sodoku
