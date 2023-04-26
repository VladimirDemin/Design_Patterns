//тест для проверки расчета прогрессивного налога для дохода более 50000
#include "pch.h"
#include "../Design_patterns/progressiveTaxStrategy.h"
TEST(ProgressiveTaxStrategyTest, calculateTaxMoreThan50000) {
    ProgressiveTaxStrategy progressiveTax;
    double income = 60000;
    EXPECT_EQ(progressiveTax.calculateTax(income), 18000);
}