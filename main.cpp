#include <iostream>
#include <fstream> 

using namespace std;


using namespace std;
ifstream fin;
ofstream fout;

void setupIO ( ) {
	fin.open ( "myfile.txt", ios::in );    // open the streams
	fout.open ( "outfile.txt", ios::out );
}

int main(){
    setupIO();
    int a;
    fin >> a;
    fout << a;
}