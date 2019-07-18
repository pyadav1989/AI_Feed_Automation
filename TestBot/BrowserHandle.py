from selenium import webdriver


class BrowserDriver:

    driver=None

    def __init__(self,web_driver):
        self.driver_ref=web_driver

    @classmethod
    def get_driver_instance(cls,browser_type,exe_path):
        if cls.driver==None and browser_type == "FireFox":
            cls.driver=webdriver.Firefox(executable_path=exe_path)
        elif cls.driver == None and browser_type == "Chrome":
            cls.driver=webdriver.Chrome(executable_path=exe_path)
        return cls.driver


if __name__ == "__main__":
    """
    driver = webdriver.Firefox(executable_path=r'/home/prashant/Desktop/CloudAI/Automation/geckodriver/geckodriver')
    url = "https://edition.cnn.com/"
    driver.get(url)
    """
