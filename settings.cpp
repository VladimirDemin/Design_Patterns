//Реализация методов класса Settings, включая конструктор, 
//методы getInstance, setStrategy и getStrategy.
#include "settings.h"
Settings* Settings::instance = nullptr;
Settings::Settings() {}
Settings* Settings::getInstance() {
    if (!instance) {
        instance = new Settings();
    }
    return instance;
}
void Settings::setStrategy(TaxCalculationStrategy* strategy) {
    this->strategy = strategy;
}

TaxCalculationStrategy* Settings::getStrategy() {
    return strategy;
}