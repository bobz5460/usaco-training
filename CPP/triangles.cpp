#include <iostream>
#include <vector>
using namespace std;


bool validTriangle(int cords[3][2]) {
  for (int i{}; i < 3; i++) {
    if (cords[i][0] == cords[(i+1)%2][0] or cords[i][0] == cords[(i+2)%2][0]) {
      if (cords[i][1] == cords[(i+1)%2][1] or cords[i][1] == cords[(i+2)%2][1]) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  freopen("triangles.in", "r", stdin);
  freopen("triangles.out", "w", stdout);
  int N;
  cin >> N;
  int cords[N][2];
  for (int i{}; i < N; i++) {
    int temp{};
    cin >> temp;
    cords[i][0] = temp;
    cin >> temp;
    cords[i][1] = temp;
  }
  vector<array[3][2]> triangles;
  for (int i{0}; i<sizeof(cords)-2; i++) {
    for (int j{1}; j<sizeof(cords)-1; j++) {
      for (int k{2}; k<sizeof(cords); k++) {
        int triangle[3][2];
        triangle[0][0] = cords[i][0];
        triangle[0][1] = cords[i][1];
        triangle[1][0] = cords[j][0];
        triangle[1][1] = cords[j][1];
        triangle[2][0] = cords[k][0];
        triangle[2][1] = cords[k][1];
        if (validTriangle(triangle)) {
          triangles.pushback(triangle);
        }

      }
    }
  }
}