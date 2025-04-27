#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    freopen("teleport.in", "r", stdin);
    freopen("teleport.out", "w", stdout);
    int a, b, x, y;
    cin >> a >> b >> x >> y;
    int minStart{min(a,b)};
    int maxStart{max(a,b)};
    int minTeleport{min(x,y)};
    int maxTeleport{max(x,y)};
    cout << min((maxStart-minStart), (abs(minStart-minTeleport)+abs(maxStart-maxTeleport)));
}
