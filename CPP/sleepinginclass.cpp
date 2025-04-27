#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> const &list) {
  for (int i{}; i < size(list); i++) {
    bool works{true};
    int addTo{};
    vector<int> newList;
    for (int j{}; j <= i; j++) {
      addTo += list[j];
    }
    newList.push_back(addTo);
    int cur{};
    for (int k{i+1}; k < size(list); k++) {
      cur += list[k];
      if (cur > addTo) {
        works = false;
        break;
      }
      if (cur == addTo) {
        newList.push_back(cur);
        cur = 0;
      }
    }
    if (not works){continue;}
    return size(list)-size(newList);
  }
}

int main() {
  int T;
  cin >> T;
  vector<int> solutions;
  for (int i{}; i < T; i++) {
    int n;
    cin >> n;
    vector<int> list;
    for (int j{}; j < n; j++) {
      int tmp;
      cin >> tmp;
      list.push_back(tmp);
    }
    solutions.push_back(solve(list));
  }
  for (int i{}; i < size(solutions); i++) {
    cout << solutions[i] << "\n";
  }
}