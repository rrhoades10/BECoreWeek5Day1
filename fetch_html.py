import requests
from bs4 import BeautifulSoup

# fetch data from a website -- coding temple website
# create a response object
response = requests.get("https://www.codingtemple.com/")
#checking our response status_code
print(response.status_code)
# print(response.content) <-- show all the cotenet we are parsing
# Using BeautifulSoup to parse html
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify()) <-- organizes the content juuuust a little bit

# using soup to grab specific html elements and their content
print(soup.title.text)

print(soup.a)

print(soup.h1.text)

