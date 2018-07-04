from appium import webdriver


desired_capabilities = {
    "platformName": "iOS",
    "platformVersion": "11.4",
    "deviceName": "iPhone 6",
    "automationName": "XCUITest",
    "app": "/Users/akuznetsova/Library/Developer/Xcode/DerivedData/WebApp-cfdslsltqhxdjvamatrfbuvejufc/Build/Products/Debug-iphonesimulator/WebApp.app"
}

mobile = webdriver.Remote(
    'http://localhost:4723/wd/hub',
    desired_capabilities
)
button = mobile.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="WebApp"]/'
            'XCUIElementTypeWindow[1]/XCUIElementTypeOther/'
            'XCUIElementTypeTextField'
        )
button.send_keys('Hello')
mobile.quit()

