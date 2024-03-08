// https://leetcode.com/problems/squares-of-a-sorted-array/description/


#include <iostream>
#include <vector>

using namespace std; 

#define MaxN 10
#define MOD (10 )
#define ll long long int
#define vi vector<int>
#define loopi(i,data,n) for(int i = data; i < n; i++)
#define loopie(i,data,n) for(int i = data; i <= n; i++)
#define loopd(i,data,n) for(int i = data; i >=n; i--)
template <typename A> ostream& operator<< ( ostream& cout, vector<A> const& v ) { cout << "["; for ( int i = 0; i < v.size ( ); i++ ) { if ( i ) cout << ", "; cout << v[i] << '\t'; } return cout << "]\n"; }


vector<int> sortedSquares(vector<int>& nums) {

    int mid = 0;
    for (; mid < nums.size(); mid++) {
        if(nums[mid] >= 0)
            break;
    }

    vector<int> mod_sorted_array(nums.size());

    int pos_index = mid;
    int neg_index = mid - 1;

    int index = 0, len = nums.size();

    for (; (pos_index < len) || (neg_index >= 0);){
        if(pos_index >= len){
            mod_sorted_array[index] = nums[neg_index];
            neg_index--;
        }
        else if(neg_index < 0){
            mod_sorted_array[index] = nums[pos_index];
            pos_index++;
        }
        else{
            if (abs(nums[pos_index]) < abs(nums[neg_index])){
                mod_sorted_array[index] = nums[pos_index];
                pos_index++;
            }
            else{
                mod_sorted_array[index] = nums[neg_index];
                neg_index--;
            }
        }
        index++;
    }
    for (int i = 0; i < mod_sorted_array.size();i++){
        mod_sorted_array[i] = mod_sorted_array[i] * mod_sorted_array[i];
    }
    return mod_sorted_array;
}

int main() {

    int myints[] = {-1, 0, 1, 2, 3, 4, 5, 6};
    vector<int> indices (myints, myints + sizeof(myints) / sizeof(int) );
    
     vector<int> a = sortedSquares(indices);
     cout << a;
}