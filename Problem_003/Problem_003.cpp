// Problem 3: Largest prime factor
//--------------------------------------------------------------------
// The prime factors of 13195 are 5, 7, 13, and 29.
//
// What is the largest prime factor of the number 600851475143?
//--------------------------------------------------------------------

#include <iostream>
#include <set>
 
unsigned primeFactors(long long num){
    std::set<unsigned> factors;
    unsigned divisor{2};
    while (num > 1){
        while (num%divisor == 0){
            factors.insert(divisor);
            num /= divisor;
        }
        divisor += 1;
        if (divisor*divisor > num){
            if (num > 1)
                factors.insert(num);
            break;
        }
    }
    return *--factors.end();
}

int main(void){
    std::cout << "Largest prime factor of the number 600851475143?\n";
    std::cout << primeFactors(600851475143) << std::endl;
    // 6857
    return 0;
}

