#include <string>
#include <iostream>
#include <cstdint>


int main() {

  std::string t,p;

  std::cout << "Enter the string: ";
  std::getline(std::cin, t);
  
  std::cout << std::endl << "Enter the substring: ";
  std::getline(std::cin, p);

  uint16_t t_len = t.size();
  uint16_t p_len = p.size();
  

  for (uint16_t i = {0}; i <= (t_len - p_len); ++i) {
    uint16_t j = 0;

    while ( (j < p_len) && (t[i+j] == p[j]) )
      ++j;
    if ( j == p_len )
      std::cout << "Found match at position " << i << std::endl;
  }
  

  return 0;
}
