#include <iostream>
// 1, 2, 3, 5, 8, 13
// 1, 2, 3, 4, 5, 6
using namespace std;

int dp_fib(int input_n)
{
    int previous_fib = 0;
    int current_fib = 1;
    int new_current_fib;

    for (int i = 0; i <= input_n; i++)
    {

        new_current_fib = current_fib + previous_fib;
        previous_fib = current_fib;
        current_fib = new_current_fib;
    }
    return previous_fib;
};

int main()
{
    int input_n = 5;
    cout << "Fib number for " << input_n << " is = " << dp_fib(input_n);
}