//тест для проверки установки и получения стратегии расчета налогов
#include "pch.h"
#include "../Design_patterns/settings.h"
#include "../Design_patterns/flatTaxStrategy.h"
TEST(SettingsTest, setAndGetStrategy) {
    Settings* settings = Settings::getInstance();
    TaxCalculationStrategy* strategy = new FlatTaxStrategy();
    settings->setStrategy(strategy);
    EXPECT_EQ(settings->getStrategy(), strategy);
}