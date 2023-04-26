// Определение класса ProgressiveTaxStrategy, который реализует
// прогрессивную стратегию расчета налогов.
#pragma once
#include "taxCalculationStrategy.h"

class ProgressiveTaxStrategy : public TaxCalculationStrategy {
public:
    double calculateTax(double income);
};