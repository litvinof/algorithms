#pragma once

#include <iostream>
#include <vector>

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::vector<T> vec) {

  os << "[";
  bool is_first = true;

  for ( const auto& el : vec ) {

    if ( !is_first ) {
      os << ", ";
    }
    is_first = false;

    os << el;
  }
  return os << "]" << std::endl;


}
