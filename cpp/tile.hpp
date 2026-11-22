/* Header file for Tile class */

#include <tuple>

#pragma once

namespace sodoku {
class Tile {

public:
  Tile(int value, std::tuple<int, int> position);
  ~Tile();
  int Get_Value() const;
  std::tuple<int, int> Get_Position() const;

private:
  int Value;
  std::tuple<int, int> Position;


};

}
