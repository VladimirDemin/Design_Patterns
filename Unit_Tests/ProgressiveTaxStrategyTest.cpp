//тест для проверки расчета прогрессивного налога для дохода менее 10000
#include "pch.h"
#include "../Design_patterns/progressiveTaxStrategy.h"
TEST(ProgressiveTaxStrategyTest, calculateTaxLessThan10000) {
    ProgressiveTaxStrategy progressiveTax;
    double income = 5000;
    EXPECT_EQ(progressiveTax.calculateTax(income), 500);
}