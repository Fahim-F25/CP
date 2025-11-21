#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxWater = 0; // that will be our answer
        int n = height.size();
        // lp = left pointer, rp = right pointer
        int lp = 0, rp = n - 1; 
        
         while (lp < rp)
         {
            int w = rp - lp; // width of container
            int h = min(height[lp], height[rp]); // height of container
            int currentWater = w * h;

            maxWater = max(maxWater, currentWater);

            if(height[lp] < height[rp]) {
                lp ++; }
            else{
             rp --;}
                
        }                

        return maxWater;
    }
};
int main()
{
    Solution obj;
    int n,i;
    cin >> n;

    vector <int> height(n);
    for(i = 0; i < n; i++){
        cin >> height[i];
    }

    cout << obj.maxArea(height) << endl;
    return 0;
}