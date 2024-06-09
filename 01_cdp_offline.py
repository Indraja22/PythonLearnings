import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",{'width':600,
                                                             'height':1000,
                                                             'deviceScaleFactor':75,
                                                             'mobile':True})
driver.get("https://www.google.com")
# driver.set_network_conditions(offline=True,latency=5,download_throughput=500 * 1024, upload_throughput=500 * 1024)
driver.refresh()

time.sleep(50)
driver.close()
