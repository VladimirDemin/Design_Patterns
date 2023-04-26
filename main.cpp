#include <iostream>
#include "settings.h"
#include "flatTaxStrategy.h"
int main()
{
    Settings* settings = Settings::getInstance();
    settings->setStrategy(new FlatTaxStrategy());
    double tax = settings->getStrategy()->calculateTax(10000);
}
