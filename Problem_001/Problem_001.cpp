// Problem 1: Multiples of 3 and 5
//-------------------------------------------------------------------
//   If we list all the natural numbers below 10 that multiples of 3
//   or 5, we get 3, 5, 6 and 9. The sum of thes is 23.
//
//   Find the sum of all the multiples of 3 or 5 below 1000.
//-------------------------------------------------------------------

#include <iostream>

unsigned byCounting(unsigned num1, unsigned num2, unsigned endRange){
    unsigned summation{0};
    for (auto i=num1; i < endRange; i+=num1)
        summation += i;
    for (auto i=num2; i < endRange; i+=num2){
        if (i%num1 == 0) continue;
        summation += i;
    }
    return summation;
}

int main(void){
    std::cout << "Find the sum of all the multiples of 3 or 5 below 1000:\n";
    std::cout << byCounting(3, 5, 1000) << std::endl;
    return 0;
}

