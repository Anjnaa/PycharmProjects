from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org")
# # driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_2")
# #
# # price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# # price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# #
# # print(f'the price is {price_dollar.text}.{price_cent.text}')
#
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# # for time in event_times:
# #     print(time.text)
#
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# # for name in event_names:
# #     print(name.text)
#
#
#
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
#
# print(events)



# driver.quit()