#include <cstdint>
#include <iostream>
#include <string>
#include <map>
#include <utility>

using namespace std;
int main() {
  freopen("tracing.in", "r", stdin);
  freopen("tracing.out", "w", stdout);
  map<int, pair<int, int>> interactions;
  int N;
  cin >> N;
  int T;
  cin >> T;
  int final[N];
  string temp;
  cin >> temp;
  for (int i{}; i < N; i++) {
    final[i] = temp[i] - '0';
  }

  for (int i{}; i < T; i++) {
    int tmp;
    cin >> tmp;
    int tmp2;
    cin >> tmp2;
    int tmp3;
    cin >> tmp3;
    interactions[tmp-1] = make_pair(tmp2-1, tmp3-1);
  }
  int mink{INT8_MAX};
  int maxk{INT8_MIN};
  int numPzero{0};
  for (int i{}; i < N; i++) {
    if (final[i] == 0) continue;
    bool hasWorked{false};
    for (int j{}; j <= T; j++) {
      int current[N]={0};
      int kLeft[N]={0};
      current[i] = 1;
      kLeft[i] = j;
      for (auto &[t, p] : interactions) {
        int x = p.first, y = p.second;
        if (current[x] == 0 and current[y] == 0) {continue;}
        bool q_infect = current[x] and kLeft[x] or current[y] and kLeft[y];
        if (kLeft[x]) --kLeft[x];
        if (kLeft[y]) --kLeft[y];
        if (!q_infect) continue;
        if (current[x] == 0) {
          current[x] = 1;
          kLeft[x] = j;
        }
        if (!current[y]) {
          current[y] = 1;
          kLeft[y] = j;
        }
      }
      bool isEqual = true;
      for (int l{}; l < N; l++) {
        if (final[l] != current[l]){isEqual = false; break;}
      }
      if (isEqual) {
        hasWorked = true;
        if (j < mink){mink = j;}
        if (j > maxk){maxk = j;}
      }
    }
    if (hasWorked){numPzero++;}
  }
  cout << numPzero << ' ' << mink << ' ';
  if (maxk == T){cout << "Infinity";}
  else {cout << maxk;}
}
