#include <iostream>
#include <fstream>
#include <unordered_set>
using namespace std;

int main() {
    ifstream in("circlecross.in");
    ofstream out("circlecross.out");
    string cross{};
    in >> cross;
    size_t total = 0;
    unordered_set<char> seen;
    for (int i{}; i < 52; i++) {
        const char currentCow{cross[i]};
        if (!seen.insert(currentCow).second)
            continue;
        unordered_set<char> to_pair;
        for (int j{i+1}; j < 52 and currentCow != cross[j]; j++)
            if (!to_pair.insert(cross[j]).second)
                to_pair.erase(cross[j]);
        total += to_pair.size();
    }
    out << total/2;
}