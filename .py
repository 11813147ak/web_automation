from selenium import webdriver


driver=webdriver.Chrome("C:/Users/HP/Desktop/chromedriver.exe")
driver.get("https://www.codechef.com/")


message_box=driver.find_element_by_id("edit-name")

message_box.clear()
message_box.send_keys("akarsh123")


password_box=driver.find_element_by_id("edit-pass")
password_box.clear()
password_box.send_keys("******")

click_button=driver.find_element_by_id("edit-submit")
click_button.click()
