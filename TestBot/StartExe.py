from BrowserHandle import BrowserDriver
from pathlib import Path
import os
from Utility import Util
import time


def start():
    try:
        config = Util.get_config_parser(os.path.join(Path(__file__).parents[1], 'config.ini'))
        js_str = Util.get_js_str(os.path.join(Path(__file__).parents[1], 'js_file'))
        url = config.get("news_site_data", "url")
        xpath=config.get("news_site_data","xpath_val")
        browser_type = config.get("browser", "browser_type")
        if browser_type == "FireFox":
            exe_path = os.path.join(Path(__file__).parents[1], "geckodriver", "geckodriver")
        elif browser_type == "Chrome":
            exe_path = os.path.join(Path(__file__).parents[1], "chromedriver", "chromedriver")
        driver = BrowserDriver.get_driver_instance(browser_type,exe_path)
        driver.get(url)
        element_val_list = driver.find_elements_by_xpath(xpath)
        i_temp = 0
        if len(element_val_list) >= 20:
            while i_temp <= 20:
                driver.execute_script("arguments[0].click();", element_val_list[i_temp])
                time.sleep(5)
                # executing js here
                driver.execute_script(js_str)
                #driver.execute_async_script(js_str)
                #driver.execute_script("var s=window.document.createElement('script');s.src='https://storage.googleapis.com/dev-ers/cnn_tracking_script.js';window.document.head.appendChild(s);")
                #print(driver.execute_script(js_str))
                # go back to home page again
                driver.get(url)
                element_val_list=driver.find_elements_by_xpath(xpath)
                i_temp += 1
        else:
            print("didn't get more than 20 links provide another xpath")
        driver.quit()
        print("Execution completed successfully")
    except Exception as ex:
        print("printing exception")
        print(ex)


if __name__ == "__main__":
    start()