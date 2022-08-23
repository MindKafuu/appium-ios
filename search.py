from appium.webdriver.common.appiumby import AppiumBy

from config.setup import AppiumSetup

appium_setup = AppiumSetup("15.5", "iPhone 12")
driver = appium_setup(3)

driver.find_element(AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeCell[9]").click()
driver.find_element(AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther").click()
field = driver.find_element(AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeSearchField'")
field.click()
field.send_keys("Mind")
