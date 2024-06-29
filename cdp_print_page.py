import base64
from robot.libraries.BuiltIn import BuiltIn

class cdp_print_page:

    def print_pdf_preview(self):
        driver_instance = BuiltIn().get_library_instance('SeleniumLibrary').driver
        result = driver_instance.execute_cdp_cmd("Page.printToPDF",{"printBackground": True,
            "landscape": False,
            "displayHeaderFooter": False,
            "paperWidth": 8.27,
            "paperHeight": 11.69})
        
        print(result,file=open("Text_op.txt","w"))

        if 'data' in result:
            pdf_data = result['data']
            with open('output_costco.pdf', 'wb') as file:
                file.write(base64.b64decode(pdf_data))
            print('PDF saved as output.pdf')
        else:
            print('Failed to print to PDF')
            
# c = cdp_print_page()
# c.print_pdf_preview()
        