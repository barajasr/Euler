// Problem 62: Cubic permutations
//--------------------------------------------------------------------
// The cube, 41063625 (345³), can be permuted to produce two other
// cubes: 56623104 (384³) and 66430125 (405³). In fact, 41063625 is
// the smallest cube which has exactly three permutations of its digits
// which are also cube.
//
// Find the smallest cube for which exactly five permutations of its
// digits are cube.
//-------------------------------------------------------------------
#include <algorithm>        // min_element
#include <string>           // to_string
#include <iostream>         // cout
#include <unordered_map>    // unordered_map

using namespace std;

int main() {
    const int maxCube = 10000;

    unordered_map<string, vector<long long>> htable;

    for (long long i{2}; i < maxCube; ++i) {
        long long cube = i*i*i;
        string s = to_string(cube);
        sort(begin(s), end(s));     // smallest permutation
        //cout << s << endl;
        htable[s].push_back(cube); // Need at least 5 collisions
    }

    for (const auto& entry : htable) {
        if (entry.second.size() == 5) {
            cout << *min_element(begin(entry.second), end(entry.second)) << endl;
            return 0;
        }
    }
    return -1;
}
