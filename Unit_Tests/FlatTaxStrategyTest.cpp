//тест для проверки расчета налога с фиксированной ставкой
#include "pch.h"
#include "../Design_patterns/flatTaxStrategy.h"
TEST(FlatTaxStrategyTest, calculateTax) {
    FlatTaxStrategy flatTax;
    double income = 10000;
    EXPECT_EQ(flatTax.calculateTax(income), 2000);
}