#include <iostream>
#include <vector>
#include <algorithm> // std::unique, std::distance

using namespace std;

int main()
{
    vector<int> subsequence = {10, 20, 30, 1, 2, 3, 4};

    vector<vector<int>> dp_subsequences(subsequence.size(), vector<int>(subsequence.size()));
    cout << subsequence.size() << "size"
         << "\n";

    int counter = 0;
    int longest_size = 0;

    for (int i = 0; i < subsequence.size(); i++) // row
    {
        for (int j = counter; j < subsequence.size(); j++) // col
        {
            cout << "i=" << i << "j= " << j << "counter=" << counter << " subsequence[j] = " << subsequence[j] << "\n";
            if (j == counter)
            {
                dp_subsequences[i][j] = subsequence[j];
            }
            else if (dp_subsequences[i][j - 1] < subsequence[j])
            {
                dp_subsequences[i][j] = subsequence[j];
                std::cout << "TRUE"
                          << "\n";
            }
            else
            {
                dp_subsequences[i][j] = dp_subsequences[i][j - 1];
            }
            cout << "dp_subsequences[i][j]=" << dp_subsequences[i][j] << "\n";
        }
        counter += 1;
        vector<int>::iterator it;
        vector<int> current_row;
        sort(dp_subsequences[i].begin(), dp_subsequences[i].end());

        it = unique(dp_subsequences[i].begin(), dp_subsequences[i].end()); // unique  eliminated the first element from every consecutive group of equivalent elements from the range

        dp_subsequences[i].resize(distance(dp_subsequences[i].begin(), it));
        cout << "Size of the unique elements in current row = " << dp_subsequences[i].size() - 1;

        int current_row_size = dp_subsequences[i].size() - 1;
        if (current_row_size > longest_size)
        {
            longest_size = current_row_size;
        }
        cout << "longest_size" << longest_size << "\n";
        cout << "--- "
             << "\n\n\n";
    }

    cout << " The longest increasing subsequence is of length = " << longest_size;
}