from selenium import webdriver
import os
from pathlib import Path
exe_path=os.path.join(Path(__file__).parents[1],'chromedriver','chromedriver')
driver_val=webdriver.Chrome(executable_path=exe_path)
driver_val.get("https://www.ndtv.com/")