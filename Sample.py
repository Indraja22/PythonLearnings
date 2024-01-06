from requests_html import HTMLSession

s = HTMLSession()
query = "London"
# query = input("Enter City Name : ")
url = f"https://www.google.com/search?q={query}+weather"
user_agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
# print(url)    
r = s.get(url,headers=user_agent)
# print(r.html.find('title', first=True).text)
temperature = r.html.find('span#wob_tm', first=True).text
# print(temperature)
unit_of_temp = r.html.xpath('//span[@aria-label="°Celsius"]',first=True).text
temperature_with_unit = temperature + unit_of_temp
print(f"Temperature in {query} : {temperature_with_unit}")

humidity = r.html.xpath('//div[contains(text(),"Humidity")]//span',first=True).text
print(f"Humidity in {query} : {humidity}")

weather = r.html.xpath("//div[@id='wob_loc']//following-sibling::div//span",first=True).text
print(weather)



top_rated = []
flag = True
for i in zomato_data_drop_na['rate']:
    i = str(i)
    i = i.split("/")[0].strip()
    if isinstance(i, float) and float(i) > 4.5:
        top_rated.append("YES")
        flag = False
    elif isinstance(i, float) and float(i) < 4.5:
        top_rated.append("NO")