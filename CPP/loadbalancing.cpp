#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    freopen("balancing.in", "r", stdin);
    freopen("balancing.out", "w", stdout);
    int N, B;
    cin >> N >> B;
    vector<int> xCords{};
    vector<int> yCords{};
    for (int i{}; i < N; i++) {
        int x, y;
        cin >> x >> y;
        xCords.push_back(x);
        yCords.push_back(y);
    }
    vector<int> sortedxCords = xCords;
    vector<int> sortedyCords = yCords;
    sort(sortedxCords.begin(), sortedxCords.end());
    sort(sortedyCords.begin(), sortedyCords.end());
    vector<int> xWalls{};
    vector<int> yWalls{};
    for (int i{}; i < N-1; i++) {
        if (sortedxCords[i] != sortedxCords[i+1]) {
            xWalls.push_back((sortedxCords[i]+sortedxCords[i+1])/2);
        }
        if (sortedyCords[i] != sortedyCords[i+1]) {
            yWalls.push_back((sortedyCords[i]+sortedyCords[i+1])/2);
        }
    }
    //xWalls is an x cord that goes up and down
    int minMax{999999999};
    for (int i{}; i < xWalls.size()-1; i++) {
        for (int j{}; j < yWalls.size()-1; j++) {
            const int xWall{xWalls[i]};
            const int yWall{yWalls[j]};
            int q1{}, q2{}, q3{}, q4{};
            for (int k{}; k < N; k++) {
                const int currentX{xCords[k]};
                const int currentY{yCords[k]};
                if (currentX < xWall) {
                    if (currentY < yWall)
                        q3++;
                    else
                        q1++;
                }
                else {
                    if (currentY < yWall)
                        q4++;
                    else
                        q2++;
                }
            }
            minMax = min(minMax, max({q1, q2, q3, q4}));
        }
    }
    cout << minMax;
}