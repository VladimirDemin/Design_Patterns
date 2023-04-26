//Определение класса Settings, который будет использоваться для установки
//и получения выбранной стратегии расчета налогов.
#pragma once
#include "taxCalculationStrategy.h"
class Settings {
private:
    static Settings* instance;
    TaxCalculationStrategy* strategy;
    Settings();
public:
    static Settings* getInstance();
    void setStrategy(TaxCalculationStrategy* strategy);
    TaxCalculationStrategy* getStrategy();
};