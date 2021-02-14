#include "common_functions.h"
#include <vector>
using namespace std;

int main()
{
    vector<int> subsequence = {10, 20, 30, 1, 2, 3, 4, 3, 50, 100};
    vector<int> lis_size;

    print_1darray(subsequence);

    for (int i; i < subsequence.size(); i++)
    {
        lis_size[i] = 1;
        for (int j; j < subsequence.size() - 1; j++)
        {
            if (subsequence[i] > subsequence[j] && lis_size[i] < 1 + lis_size[j] + 1)
            {
                lis_size[i] = 1 + lis_size[j];
            }
        }
    }

    auto it = max_element(begin(subsequence), end(subsequence)); // c++11
}