#include "common_functions.h"
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    vector<int> int_subsequence = {5, 15, -20, 10, -5, 40, 10};
    vector<int> max_contigous_int_subsequence;
    cout << "test0";
    cout << int_subsequence.size() << "size\n";

    // print_1darray(int_subsequence);

    for (int j; j < 2; j++)
    {
        cout << j << "j";
    }

    for (int i; i < int_subsequence.size(); i++)
    {
        cout << i << "i"
             << "\n";
        if (i == 0)
        {
            cout << "test1";
            max_contigous_int_subsequence.push_back(int_subsequence[i]);
        }
        else if (int_subsequence[i] + max_contigous_int_subsequence[i - 1] > max_contigous_int_subsequence[i - 1])
        {
            cout << "test";
            max_contigous_int_subsequence.push_back(int_subsequence[i] + max_contigous_int_subsequence[i - 1]);
        }
        else
        {
            max_contigous_int_subsequence.push_back(0);
        }
    }

    // print_1darray(max_contigous_int_subsequence);
}