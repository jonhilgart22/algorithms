#include <iostream>
#include "common_functions.h"
using namespace std;

void print_1darray(vector<int> input_array)
{
    int n = input_array.size();
    cout << " Array size = " << n << "\n";

    // loop through the elements of the array
    for (int i = 0; i < n; i++)
    {
        cout << "i = " << i << "\n";
        cout << input_array[i] << ' ';
    }
}