// https://leetcode.com/problems/maximum-subarray/description/

#include <iostream>
#include <vector>
#include <fstream> 
#include <iterator>
#include <algorithm>

using namespace std;

#define ll long long int
#define vi vector<int>
#define loopi(i,data,n) for(int i = data; i < n; i++)
#define loopie(i,data,n) for(int i = data; i <= n; i++)
#define loopd(i,data,n) for(int i = data; i >=n; i--)
template <typename A> ostream& operator<< ( ostream& cout, vector<A> const& v ) { cout << "["; for ( int i = 0; i < v.size ( ); i++ ) { if ( i ) cout << ", "; cout << v[i] << '\t'; } return cout << "]\n"; }
#include <limits>

//your code here

void  run ( ) {
	// freopen ( "in.txt", "r", stdin );
	//freopen ( "outfile.txt", "w", stdout );
}

int maxSubArray(vector<int>& nums) {

    int max_sum_inc_i = nums[0];
    int max_val  = nums[0];
    // cout << "min" << max_val << endl;
    
    loopi(i, 1, nums.size()){
        max_sum_inc_i = max(max_sum_inc_i + nums[i], nums[i]);
        max_val = max(max_val, max_sum_inc_i);
    }
    // cout << max_sum_inc_i;
    return max_val;
}

int main(){
    run();
    int len;
    cin >> len;
    vector<int> arr(len);

    loopi(i, 0, len){
        cin>>arr[i];
    }
    cout<< maxSubArray(arr);
}
