#include<iostream>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        long binForm = n;
        if (n < 0) {
            binForm = -binForm;
            x = 1 / x;
        }
        double ans = 1;
        while (binForm > 0) {
            if (binForm % 2 == 1) {
                ans = ans * x;
            }
            x = x * x;
            binForm = binForm / 2;
        }
        return ans;
    }
};

int main()
{
    Solution sol;

    double x;
    cin >> x;

    int n;
    cin >> n;

    cout << sol.myPow(x, n);
    return 0;
}
