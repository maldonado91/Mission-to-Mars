#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install splinter


# In[ ]:


# pip install webdriver_manager


# In[ ]:


# pip install bs4


# In[4]:


# pip install selenium


# In[5]:


# pip install --upgrade requests


# In[46]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[7]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


# # Quit Splinter session
# browser.quit()


# In[9]:


# 10.3.2 Practice with Splinter and BeautifulSoup


# In[10]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[11]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[12]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[13]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[14]:


for x in range(1, 6):
    html = browser.html
    quote_soup = soup(html, 'html.parser')
    quotes = quote_soup.find_all('span', class_='text')
    for quote in quotes:
        print('page:', x, '----------')
        print(quote.text)
    browser.links.find_by_partial_text('Next').click()


# In[15]:


# 10.3.3 Scrape Mars Data: The News


# In[16]:


browser.quit()


# In[17]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[18]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[19]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[20]:


slide_elem.find('div', class_='content_title')


# In[21]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[27]:


# Use the parent element to find the paragraph text
news_p = news_soup.find('div', class_='col-12').get_text().strip()
news_p


# In[29]:


# 10.3.4 Scrape Mars Data: Featured Image


# In[32]:


browser.quit()


# ### Featured Images

# In[35]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[36]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[38]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[39]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[40]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[41]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[42]:


# 10.3.5 Scapre Mars Data: Mars Facts


# In[43]:


browser.quit()


# In[44]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[47]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[49]:


df.to_html()


# In[ ]:




