
# coding: utf-8

# In[1]:


#web scraping homework
#Marcus Manahan 


# In[2]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
import pandas as pd
import time


# In[3]:


#NASA Mars News


# In[4]:


executable_path = {'executable_path': 'chromedriver.exe'} #use the chrome driver
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url) #pointing to the NASA Mars News website


# In[6]:


html = browser.html #variable to hold the browser's html


# In[7]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')
#soup


# In[8]:


title = soup.find("div", class_ = 'content_title') #searching for the title 


# In[9]:


news_title = title.text #print out the title
print(news_title)


# In[10]:


news_p = soup.find("div", class_ = 'article_teaser_body') #search for paragraph and print out
news_p = news_p.text
print(news_p)


# In[11]:


#JPL Mars Space Images - Featured Image


# In[12]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url) #pointing to the JPL Mars images
html = browser.html #variable to hold the browser's html


# In[13]:


time.sleep(10)


# In[14]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')
browser.click_link_by_partial_text('FULL IMAGE')


# In[15]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[16]:


time.sleep(10)


# In[17]:


browser.click_link_by_partial_text('more info')


# In[18]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[19]:


feature_image = soup.find("figure", class_ = 'lede').findAll('img') #one way of searching for the image


# In[20]:


print(feature_image)


# In[21]:


pic = soup.find("img", class_ = "main_image")


# In[22]:


pic


# In[23]:


feature_image_url = pic['src']
print(feature_image_url )


# In[24]:


featured_image_url = pic['src']


# In[25]:


featured_image_url 


# In[26]:


home_url = str('https://www.jpl.nasa.gov')
home_url


# In[27]:


featured_image_url = home_url + featured_image_url 


# In[28]:


featured_image_url


# In[29]:


#Twitter Page


# In[30]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html #variable to hold the browser's html
soup = BeautifulSoup(html, 'html.parser')


# In[31]:


#<p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" lang="en"


# In[32]:


weather_tweet = soup.find_all("p", class_ ="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


# In[33]:


weather_tweet[0]


# In[34]:


weather_tweet[5].text
weather_info = []


# In[35]:


array_len = len(weather_tweet)
x = 0
for text in weather_tweet:         #for loop to determine if tweets contain weather information
    text = weather_tweet[x].text
    if text.find("hPa") == -1:     #if the tweet contains the string hPa then it is a weather tweet
        print("Not a weather tweet!")
    else:
        print("This is a weather tweet!")
        weather_info.append(weather_tweet[x].text)
        
    
    x += 1


# In[36]:


print(weather_tweet[0].text)


# In[37]:


weather_tweet[19]


# In[38]:


mars_weather = weather_info[0]
print(mars_weather)


# In[39]:


#Mars Facts page


# In[40]:


url = 'https://space-facts.com/mars/'
browser.visit(url) #pointing to the Mars facts page
html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[41]:


info = soup.find_all('td',class_ = 'column-2')
info


# In[42]:


eq_diameter = info[0].text
polar_diameter = info[1].text
mass = info[2].text
moons = info[3].text
orb_dist = info[4].text
orb_period = info[5].text
surface_temp = info[6].text
first_record = info[7].text
recorded_by = info[8].text


# In[43]:


info_array = [eq_diameter,polar_diameter,mass,moons,orb_dist,orb_period,surface_temp,first_record,recorded_by]
fact_df = pd.DataFrame(info_array)


# In[44]:


fact_df["label"] = ['Equatorial Diameter','Polar Diameter','Mass','Moons','Orbital Distance','Orbital Period','Surface Temperature','First Record','Recorded By']


# In[45]:


fact_df.set_index("label", inplace=True)


# In[46]:


fact_df = fact_df.rename(index = str,columns = {0:"fact"})


# In[47]:


fact_df


# In[48]:


facts_html = fact_df.to_html()   #turn dataframe into html script


# In[49]:


facts_html


# In[50]:


#Mars Hemispheres


# In[51]:


#Hemisphere 1 - Cerberus Hemisphere Enahnced


# In[52]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url) #pointing to the hemispheres website
html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[53]:


browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')


# In[54]:


html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[55]:


hem_1 = soup.find("div",class_="downloads") #image url is contained in downloads container


# In[56]:


hem_1


# In[57]:


hem_1 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg' #image url of hemispher


# In[58]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url) #pointing to the hemispheres website
html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[59]:


browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')


# In[60]:


html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[61]:


#Hemisphere 2 - Schiaparelli Hemisphere Enhanced


# In[62]:


hem_2 = soup.find("div",class_="downloads")


# In[63]:


hem_2 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg' #get img url


# In[64]:


#Hemisphere 3 - Syrtis Major Hemisphere Enhanced


# In[65]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url) #pointing to the hemispheres website
html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[66]:


browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')


# In[67]:


html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[68]:


hem_3 = soup.find("div",class_="downloads")


# In[69]:


hem_3 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg' #get img url


# In[70]:


#Hemisphere 4 - Valles Marineris Hemisphere Enhanced


# In[ ]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url) #pointing to the hemispheres website
html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')


# In[ ]:


html = browser.html #variable to hold the browser's html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


hem_4 = soup.find("div",class_="downloads")


# In[ ]:


hem_4 = 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg' #get img url


# In[ ]:


hemisphere_img_url = [
    {"title": "Cerberus Hemisphere", "img_url": hem_1},       #creating a list of dictionaries to hold image urls
    {"title": "Schiaparelli Hemisphere", "img_url": hem_2},
    {"title": "Syrtis Major Hemisphere", "img_url": hem_3},
    {"title": "Valles Marineris Hemisphere", "img_url": hem_4}
]


# In[ ]:


hemisphere_img_url[3]["img_url"] #testing dictionary

