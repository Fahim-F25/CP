#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currenSum = 0, maxSum = INT_MIN;
        for(int val : nums)
        {
            currenSum = currenSum + val;
            maxSum = max(currenSum,maxSum);
            if(currenSum < 0){
                currenSum = 0;
            }
        }
        return maxSum;
    }
};
int main()
{
    Solution obj;
    int n;
    cin >> n;
    vector <int> nums(n);
    for(int i=0; i<n; i++)
    {
        cin >> nums[i];
    }
    int maximumSubArray = obj.maxSubArray(nums);
    cout << "Maximum Subarray : " << maximumSubArray << endl;
    return 0;
}