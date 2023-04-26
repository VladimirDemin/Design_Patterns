//Определение абстрактного класса TaxCalculationStrategy, 
//который будет использоваться для определения различных стратегий расчета налогов.
#pragma once
class TaxCalculationStrategy {
public:
    virtual double calculateTax(double income) = 0;
};
