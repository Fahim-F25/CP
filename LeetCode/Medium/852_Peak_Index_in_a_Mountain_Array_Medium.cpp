#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int start = 1, end = arr.size() - 2;

        while (start <= end)
        {
            int mid = start + (end - start)/2;
            if(arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1]){
                return mid;
            }else if (arr[mid - 1] < arr[mid]) // right
            {
                start = mid + 1;
            }else{ // left
                end = mid - 1;
            }
            
        }

        return -1;
        
    }
};

int main()
{
    Solution obj;
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    cout << obj.peakIndexInMountainArray(arr) << endl;

    return 0;
}