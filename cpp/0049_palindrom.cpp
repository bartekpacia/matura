#include <iostream>

using namespace std;

int main() {
  string s;

  cin >> s;

  int n = s.length();

  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 2; j <= n; j++) {
      int leftIndex = i;
      int rightIndex = j - 1;
      bool is_palindrome = true;

      while (leftIndex < rightIndex) {
        if (s.at(leftIndex++) != s.at(rightIndex--)) {
          is_palindrome = false;
          break;
        }
      }

      if (is_palindrome) {
        cout << s.substr(i, j - i) << endl;
      }
    }
  }

  cout << endl;

  getchar();
  return 0;
}
