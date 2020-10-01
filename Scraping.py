'''
Author = Zeeshan
Date = 8/19/2020
Purpose = Web Scraping

'''

#  Step 0 : Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = 'https://codewithharry.com'

#  Step 1 : Get the HTML
r = requests.get(url)
html_content = r.content
# print(html_content)

#  Step 2 : Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify)

#  Step 3 : HTML Tree traversal
# 
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. Navigable String
# print(type(soup))  # 3. BeautifulSoup

# 4. Comment
# markup = '<p><!-- This is a comment --></p>'
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

# Get the title of the HTML page
title = soup.title

# Get all the paragraphs form the page
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags form the page
anchors = soup.find_all('a')
# print(anchors)

# Get all the links on the page
# all_links = set()
# for link in anchors:
#     if (link.get('href') != "#"):
#         linkText = 'https://codewithharry.com' + link.get('href')
#         all_links.add(link)
#         print(linkText)

# Get the first element in the HTML page
# print(soup.find('p'))

# Get the classes of any element in the HTML page
# print(soup.find('p')['class'])

# Find all the elements with class lead
# print(soup.find_all('p', class_= 'lead'))

# Get the text form the tags/soup
# print(soup.find('p').get_text())

# Get the text from the page
# print(soup.get_text())


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's childern are avalible as a list
# .childern - A tag's childern are avalible as a generator
# for elem in navbarSupportedContent.contents:
    # print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)

# for item in navbarSupportedContent.parents:
#     print(item)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elm = soup.select('#loginModal')
# print(elm)
