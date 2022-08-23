from appium.webdriver.common.appiumby import AppiumBy

from config.setup import AppiumSetup

appium_setup = AppiumSetup("15.5", "iPhone 12")
driver = appium_setup(3)

button_elements = '**/XCUIElementTypeButton'

show_year_picker = '**/XCUIElementTypeButton[`label == "Show year picker"`]'
hide_year_picker = '**/XCUIElementTypeButton[`label == "Hide year picker"`]'
time_picker = '**/XCUIElementTypePickerWheel'

date = '//*[contains(@label, " 22")]'

# Views
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Date Picker').click()

# Pick Date
button = driver.find_elements(AppiumBy.IOS_CLASS_CHAIN, button_elements)
button[1].click()
driver.find_element(AppiumBy.XPATH, date).click()
driver.find_element(AppiumBy.IOS_CLASS_CHAIN, show_year_picker).click()
driver.implicitly_wait(3)
driver.find_element(AppiumBy.IOS_CLASS_CHAIN, hide_year_picker).click()

# Pick Time
button[2].click()
wheel = driver.find_elements(AppiumBy.IOS_CLASS_CHAIN, time_picker)
wheel[0].send_keys("11")
wheel[1].send_keys("30")
wheel[2].send_keys("PM")
button[2].click()