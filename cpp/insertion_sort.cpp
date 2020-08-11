#include <algorithm>
#include <iostream>
#include <vector>

#include "vector_print.cpp"

// Insertion sort
int main(int argc, char *argv[]) {
  std::vector<int> candidates{5, 2, 4, 6, 1, 3};
      
  for ( std::size_t j = 1; j < candidates.size(); ++j ) {
    int key = candidates[j];
    // Insert candidates[j] into the sorted sequence candidates[1..j-1]
    std::size_t i = j - 1;
    while (i >= 0 and i < candidates.size() and key < candidates[i]) {
      candidates[i + 1] = candidates[i];
      --i;
    }
    candidates[i + 1] = key;
  }

  std::cout << candidates;
}
