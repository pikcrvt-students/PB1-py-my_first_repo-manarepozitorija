#include <iostream>

int main() {
    // apreiķināt y=2x - 1, ja x [-3; 1], Δx=0,5
    float x, y;
    x = -3.0;
    do {
        y = 2 * x - 1;
        std::cout << "x=" << x << "y=" << y << std::endl;
        x += 0.5; //vai x = x + 0.5
    } while(x <= 1);
    

    return 0;
}