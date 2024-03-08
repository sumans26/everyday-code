#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<int> a{1,2,3,4,5,6,7,8,9,10,11,12};
    int ran;
    cin >> ran;
    for (auto i : a)
    {
        cout << i;
    }
    // cout << ran;
}