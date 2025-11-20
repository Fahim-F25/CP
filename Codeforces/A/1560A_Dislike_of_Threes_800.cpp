#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t, k;
    cin >> t; // take number of test cases

    vector<int> nums;

    // Precompute valid numbers
    for (int i = 1; i <= 2000; i++) {
        if (i % 3 != 0 && i % 10 != 3) {
            nums.push_back(i);
        }
    }

    // Answer each test case
    for (int i = 0; i < t; i++) {
        cin >> k;
        cout << nums[k - 1] << endl;
    }

    return 0;
}
