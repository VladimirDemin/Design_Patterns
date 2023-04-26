//тест для проверки создания объекта класса Settings и его метода getInstance
#include "pch.h"
#include "../Design_patterns/settings.h"
TEST(SettingsTest, getInstance) {
    Settings* settings = Settings::getInstance();
    EXPECT_NE(settings, nullptr);
}