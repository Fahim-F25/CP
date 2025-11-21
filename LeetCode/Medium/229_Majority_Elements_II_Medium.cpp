#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) 
    {
        int n = nums.size();
        int count1 = 0, count2 = 0;
        int cand1 = 1000, cand2 = 2000;

        // find potential candidates for majority elements 
        for(int num : nums){
            if(num == cand1) count1 ++;
            else if (num == cand2) count2 ++;
            else if (count1 == 0){
                cand1 = num;
                count1 = 1;
            }
            else if (count2 == 0){
                cand2 = num;
                count2 = 1;
            }
            else {
                count1 --;
                count2 --;
            }
             
        }

        // verify actual counts
        count1 = 0;
        count2 = 0;
        for(int num : nums){
            if(num == cand1) count1 ++;
            else if (num == cand2) count2 ++;
        }

        vector<int> result;
        if(count1 > n / 3) result.push_back(cand1);
        if(count2 > n / 3) result.push_back(cand2);

        return result;
    }
};
int main()
{
    Solution obj;
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i=0; i<n; i++)
    {
        cin >> nums[i];
    }
    vector<int> ans = obj.majorityElement(nums);
    for(int val : ans){
        cout << val << " ";
    }
    cout << endl;
    return 0;
}