#include <iostream>
using namespace std;

int main() {
    freopen("pails.in", "r", stdin);
    freopen("pails.out", "w", stdout);
    int x, y, m;
    cin >> x >> y >> m;
    int thing{m/x};
    int max{};
    for (int i{0}; i < thing+1; i++) {
        for (int j{0}; j < thing+1; j++) {
            int added{(i*x)+(j*y)};
            if (added>m) {
                break;
            }
            if (added > max){max = added;}}
        }
    cout << max;
    }