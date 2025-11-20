#include<iostream>
using namespace std;
int differ(string s)
{
    string a = "codeforces";
    int counter = 0;

    for(int i = 0; i < a.size(); i++ )
    {
        if (a[i] != s[i])
        {
            counter = counter + 1;
        }
    }
    return counter;   
}

int main()
{
  int t;
  string s;
  cin >> t;
  for(int i = 0; i<t; i++)
  {
    cin >> s ;
    cout<< differ(s) << endl;
  } 

return 0;
}