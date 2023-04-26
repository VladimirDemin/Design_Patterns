//ќпределение класса FlatTaxStrategy, который реализует стратегию расчета налогов
// с фиксированной ставкой.
#pragma once
#include "taxCalculationStrategy.h"

class FlatTaxStrategy : public TaxCalculationStrategy {
public:
    double calculateTax(double income);
};
