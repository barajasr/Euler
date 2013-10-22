// Problem 2: Even Fibonacci numbers
//--------------------------------------------------------------------
// Each new term in the Fibonacci sequence is generated by adding the
// previous two terms. By starting with 1, and 2, the first 10 terms
// will be:
//   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do
// not exceed four million, find the sum of the even-valued terms.
//--------------------------------------------------------------------

#include <iostream>
#include <cmath>

unsigned evenFibSum(unsigned maxVal){
    unsigned summation{0}, previous{1}, current{2};
    while (current < maxVal){
        if (current%2 == 0)
            summation += current;
        auto tmp = current;
        current += previous;
        previous =tmp;
    }

    return summation;
}

unsigned usingRatios(unsigned maxVal){
    // φ is approximate ratio between nth and nth+1 fib numbers
    // φ³ is approximate ratio between even fib numbers
    // ((1+√5)/2)**3  / ≅ 4.236068
    float phiCubed = std::pow((1+std::sqrt(5))/2, 3.0);

    unsigned summation{0}, curEven{2};
    while (curEven < maxVal){
        summation += curEven;
        curEven = static_cast<unsigned>(std::round(curEven * phiCubed));
    }
    return summation;
}

int main(void){
    std::cout << "Summation of even Fib numbers under 4,000,000:\n";
    std::cout << evenFibSum(4000000) << std::endl;
    std::cout << usingRatios(4000000);
    // 4613732
    return 0;
}
