// Problem 4: Largest palindrome product
//--------------------------------------------------------------------
//   A palindromic number reads the same both ways. The largest
//   palindrome made from the product of two 2-digit numbers is
//   9009 =  91·99.
//
//   Find the largest largest palindrome made from the product of
//   two 3-digit numbers.
//--------------------------------------------------------------------

#include <iostream>
#include <string>
#include <vector>

bool isPalindrome(const std::string& toTest){
    // Uses reverse iterators for comparison string construction
    return toTest == std::string(toTest.rbegin(), toTest.rend());
}

unsigned bruteMultiplication(){
    unsigned solution{0};
    std::vector<unsigned> range;
    for (auto i=999; i > 99; --i)
        range.push_back(i);

    for (auto i=999; i >99; --i){
        for(auto number:range){
            auto product = i*number;
            if (product > solution){
                if (isPalindrome(std::to_string(product)))
                    solution = product;
            }else {
                // Save a couple (~8) thousandths of a sec
                break;
            }
        }
        // Don't do redundant work
        range.erase(range.begin());
    }
    return solution;
}

int main(void){
    std::cout << "Largest palindrome from product of two 3-digit numbers.\n";
    std::cout <<  "solution: " << bruteMultiplication() << std::endl;
    // 906609
    return 0;
}

