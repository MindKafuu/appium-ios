from appium import webdriver

class AppiumSetup:

    def __init__(self, platform_version, device_name):
        self.platform_version = platform_version
        self.device_name = device_name

    def __call__(self, time):
        desired_cap = {
            "platformName": "iOS",
            "platformVersion": self.platform_version,
            "deviceName": self.device_name,
            "automationName": "XCUITest",
            "app": "/Users/ibank/Documents/appium/ios_test1/app_binaries/UIKitCatalog.app"
        }

        command_executor = "http://127.0.0.1:4723/wd/hub"
        driver = webdriver.Remote(command_executor, desired_cap)
        driver.implicitly_wait(time)
        return driver
