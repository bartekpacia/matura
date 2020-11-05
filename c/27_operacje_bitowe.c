#include <stdio.h>

int main() {
  int8_t num = 0b00001101;  // 13
  printf("num: %i\n", num);

  // setting a bit (bitwise AND – suma bitowa)
  num = num | (1 << 1);  // 15
  printf("num: %i\n", num);
  // 1101
  // 0010
  // AND
  // 1111

  // clearing a bit
  num = num & ~(1 << 1);
  printf("num: %i\n", num);
  // 1111
  // 1101
  // AND
  // 1101

  // i spowrotem do 15
  num |= (1 << 1);
  printf("num: %i\n", num);

  // Chcę wyzerować 2 najmłodsze bity
  // num = num & 0b00000011;
  num = num & ~(0b00000000);
  printf("num: %i\n", num);

  getchar();
  return 0;
}