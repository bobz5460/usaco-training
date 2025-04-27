#include <iostream>
#include <vector>
#include <set>
using namespace std;
int time(vector<pair<int, int>> shifts) {
  set<int> amt;
  for (int i{}; i < size(shifts); i++) {
    for (int j{shifts[i].first}; j < shifts[i].second; j++) {
      amt.insert(j);
    }
  }
  return size(amt);
}
int main() {
  freopen("lifeguards.in", "r", stdin);
  freopen("lifeguards.out", "w", stdout);
  int N;
  cin >> N;
  vector<pair<int, int>> shifts;
  for (int i{}; i<N; i++) {
    pair<int, int> temps;
    int temp;
    cin >> temp;
    temps.first = temp;
    cin >> temp;
    temps.second = temp;
    shifts.push_back(temps);
  }
  int max{};
  for (int i{}; i<N; i++) {
    vector<pair<int, int>> shiftsFired;
    for (int j{}; j<N; j++) {
      if (i==j){continue;}
      shiftsFired.push_back(shifts[j]);
    }
    int cur{time(shiftsFired)};
    if (cur>max){max = cur;}
  }
  cout << max;
}