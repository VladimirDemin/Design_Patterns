//Реализация метода calculateTax для класса ProgressiveTaxStrategy.
#include "progressiveTaxStrategy.h"
double ProgressiveTaxStrategy::calculateTax(double income) {
    if (income < 10000) {
        return 0.1 * income;
    }
    else if (income < 50000) {
        return 0.2 * income;
    }
    else {
        return 0.3 * income;
    }
}