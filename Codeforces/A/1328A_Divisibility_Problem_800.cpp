#include<iostream>
using namespace std;

int visibility(int a, int b)
{
    if(a % b == 0){
        return 0;
    }
    else{
        return b - (a % b);
    }
}
int main()
{
    int a, b, t;
   cin >> t;
   for(int i = 0; i<t; i++){
    cin >> a >> b;
    cout << visibility(a,b) << endl;
   }
    return 0;
} 
