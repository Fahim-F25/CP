#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;

        while (start <= end)
        {
           int mid = start + (end - start)/2;
            if (nums[mid] == target)
            {
                return mid;
            }

            if(nums[start] <= nums[mid]){ // left sorted
                if(nums[start] <= target && target <= nums[mid]){
                    end = mid - 1;
                }else{
                    start = mid + 1;
                }

            }else{// right sorted
                if(nums[mid] <= target && target <= nums[end]){
                    start = mid + 1;
                }else{
                    end = mid - 1;
                }
            }
            
        }
        return -1;
        
    }
};

int main()
{
    Solution obj;
    int n, target;
    cin >> n;
    cin >> target;

    vector <int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }

    cout << obj.search(nums, target) << endl;
    return 0;
}