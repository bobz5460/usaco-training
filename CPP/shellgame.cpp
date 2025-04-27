//
// Created by bzhan on 2/21/2025.
//
#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    freopen("shell.in", "r", stdin);
    freopen("shell.out", "w", stdout);
    int n{};
    cin >> n;
    vector<vector<int>> steps{};
    for (int i{}; i < n; i++) {
        vector<int> line{};
        for (int j{}; j < 3; j++) {
            int temp{};
            cin >> temp;
            line.push_back(temp-1);
        }
        steps.push_back(line);
    }
    int points{};
    for (int initialPebble{}; initialPebble < 3; initialPebble++) {
        vector positions{0, 1, 2};
        int curPoints{};
        for (int i{}; i < n; i++) {

            swap(positions[steps[i][0]], positions[steps[i][1]]);
            if (positions[steps[i][2]] == initialPebble) {
                curPoints++;
            }
        }
        points = max(curPoints, points);
    }
    cout << points;
}