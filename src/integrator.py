from selenium import webdriver
from selenium.webdriver.common.by import By

class LegacySystemIntegrator:
    def __init__(self, config):
        self.driver = None
        self.config = config
    
    def connect(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.config['legacy_system_url'])