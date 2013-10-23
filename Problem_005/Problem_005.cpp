// Problem 5: Smallest Multiple
//--------------------------------------------------------------------
//   2520 is the smallest number that can be divided by each of the
//   numbers from 1 to 10 without any remainder.
//
//   What is the smallest positive number that is evenly divisble by
//   all of the numbers from 1 to 20?

// Other solution
// http://mathforum.org/library/drmath/view/62527.html
// 01 = 1¹| 
// 02 =   | 2¹ |
// 03 =   |    | 3¹ |
// 04 =   | 2² |    |
// 05 =   |    |    | 5¹ |
// 06 =   | 2¹ | 3¹ |    |
// 07 =   |    |    |    | 7¹ |
// 08 =   | 2³ |    |    |    |
// 09 =   |    | 3² |    |    |
// 10 =   | 2¹ |    | 5¹ |    |
// 11 =   |    |    |    |    | 11¹ |
// 12 =   | 2² | 3¹ |    |    |     |
// 13 =   |    |    |    |    |     | 13¹ |
// 14 =   | 2¹ |    |    | 7¹ |     |     |
// 15 =   |    | 3¹ | 5¹ |    |     |     |
// 16 =   | 2⁴ |    |    |    |     |     |
// 17 =   |    |    |    |    |     |     | 17¹ |
// 18 =   | 2¹ | 3² |    |    |     |     |     |
// 19 =   |    |    |    |    |     |     |     | 19¹
// 20 =   | 2² |    | 5¹ |    |     |     |     |
// ----------------------------------------------------
// max→ 1¹| 2⁴ | 3² | 5¹ | 7¹ | 11¹ | 13¹ | 17¹ | 19¹
//
// solution = 1¹* 2⁴ * 3² * 5¹ * 7¹ * 11¹ * 13¹ * 17¹ * 19¹
//          = 232792560
//--------------------------------------------------------------------

#include <iostream>

bool isDivisbleTo(unsigned num, unsigned numRange){
    for (auto i=numRange; i > 0; --i)
        if (num%i != 0)
            return false;
    return true;
}
unsigned divisibleTo(unsigned numRange){
    if (numRange > 0){
        auto step = divisibleTo(numRange-1);
        auto num = 0;
        bool found{false};
        while (!found){
            num += step;
            found = isDivisbleTo(num, numRange);
        }
        return num;
    }else{
        std::cout << "exit\n";
        return 0;
    }
}

int main(void){
    std::cout << "Smallest positive number evenly divisble by [1...20]:\n";
    std::cout << divisibleTo(20) << std::endl;
    return 0;
}

