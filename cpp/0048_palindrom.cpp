#include <iostream>

using namespace std;

int main() {
  string word;
  cin >> word;

  bool is_palindrome = true;
  for (int i = 0; i < word.length(); i++) {
    if (word.at(i) != word.at(word.length() - i - 1)) {
      is_palindrome = false;
    }
  }

  if (is_palindrome) {
    cout << "tak to palindrom" << endl;
  } else {
    cout << "nie to nie palindrom" << endl;
  }

  getchar();
  return 0;
}
