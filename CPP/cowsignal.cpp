#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    freopen("cowsignal.in", "r", stdin);
    freopen("cowsignal.out", "w", stdout);
    int m{}, n{}, k{};
    cin >> m;
    cin >> n;
    cin >> k;
    for (int i{}; i < m; i++) {
        string currentLine{};
        string multipliedLine{};
        cin >> currentLine;
        for(const char charactor : currentLine) {
            for (int j{}; j < k; j++) { multipliedLine += charactor; }
        }
        for (int j{}; j < k; j++) { cout << multipliedLine << endl; }
    }
}