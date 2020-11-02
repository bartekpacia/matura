#include <stdio.h>

int main() {
  int a = 1;

  printf("a: %i\n", a);
  printf("a << 1: %i\n", a << 1);
  printf("a << 2: %i\n", a << 2);
  printf("a & 1: %i\n", a & 1);
  printf("a & 2: %i\n", a & 2);
  printf("a ^ 1: %i\n", a ^ 1);
  printf("a ^ 2: %i\n", a ^ 2);
  printf("a ^ 3: %i\n", a ^ 3);

  getchar();
  return 0;
}