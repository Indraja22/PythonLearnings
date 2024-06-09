from robot.libraries.BuiltIn import BuiltIn

class cdp_lib:


    def set_offline_status(self):
        driver_instance = BuiltIn().get_library_instance('SeleniumLibrary').driver
        driver_instance.set_network_conditions(offline=True,
                                               latency=5,
                                               download_throughput=500 * 1024,
                                               upload_throughput=500 * 1024)
        
    def cdp_responsiveness(self):
        driver_instance = BuiltIn().get_library_instance('SeleniumLibrary').driver
        driver_instance.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",{'width':600,
                                                             'height':1000,
                                                             'deviceScaleFactor':75,
                                                             'mobile':True})