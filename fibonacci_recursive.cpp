#include <iostream>
// 1, 2, 3, 5, 8, 13
// 1, 2, 3, 4, 5, 6
using namespace std;

int fib_number(int input_fib_number, int current_fib_number, int previous_fib_number, int counter)

{
    if (counter == input_fib_number)
    {
        return current_fib_number + previous_fib_number;
    }
    else
    {
        return fib_number(input_fib_number, current_fib_number + previous_fib_number, current_fib_number, counter + 1);
    }
}

int main()
{
    int input_n = 6;
    cout << "Fib number for " << input_n << " is = " << fib_number(input_n, 1, 0, 1) << "\n";
}
