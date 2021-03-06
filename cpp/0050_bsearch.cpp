#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  ifstream infile("test.txt");
  vector<int> nums;

  int a;
  while (infile >> a) {
    if (a == 0) {
      break;
    }

    nums.push_back(a);
  }

  auto min = min_element(nums.begin(), nums.end());
  auto max = max_element(nums.begin(), nums.end());
  cout << "max:" << *max << endl;
  cout << "min:" << *min << endl;

  for (int num : nums) {
    cout << num << endl;
  }

  return 0;
}
