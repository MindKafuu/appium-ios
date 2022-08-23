from appium.webdriver.common.appiumby import AppiumBy

from config.setup import AppiumSetup

appium_setup = AppiumSetup("15.5", "iPhone 12")
driver = appium_setup(3)

slider = '**/XCUIElementTypeSlider'

# Views
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Sliders').click()

# Slider
sliders = driver.find_elements(AppiumBy.IOS_CLASS_CHAIN, slider)
sliders[1].send_keys("0.8") 