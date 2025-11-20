#include<iostream>
using namespace std;

int sumOfDigit(int num)
{
    int rem, sumOfDigits = 0;
    while (num > 0)
    {
       rem = num % 10;
       num = num / 10;
       sumOfDigits = sumOfDigits + rem;
    }
    return sumOfDigits;
}

int main()
{
    int t, num;
    cin >> t;

    for(int i = 0; i<t; i++)
    {
        cin >> num;
        cout << sumOfDigit(num) << endl;
        
    }
    
    return 0;
}