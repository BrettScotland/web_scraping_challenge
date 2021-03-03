

import requests
import pymongo
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


db = client.nasa_db
collection = db.articles



def scrape_info():

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')


    # Find required text element
    news_p = soup.find("div", class_="rollover_description_inner").text
    print(news_p)


    # Print article title
    news_title = soup.find("div", class_ = "content_title").text
    print(news_title)



    # Create pathway for splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    # Open splinter browser
    url = "https://www.jpl.nasa.gov/images?search=&category=Mars"
    browser.visit(url)



    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Open full size image
    browser.click_link_by_partial_text('Image')



    soup.find("div", class_="BaseImagePlaceholder")


    # Print featured image url
    featured_image_url = soup.find("div", class_="BaseImagePlaceholder").find("img")["data-src"]
    print(featured_image_url)


    # Read Mars facts table
    url = "https://space-facts.com/mars/"


    tables = pd.read_html(url)
    tables


    df = tables[0]
    df.columns = ["", "Mars"]
    mars_facts = df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    




  # Create pathway for splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[8]:


    # Open splinter browser
    url = "https://www.jpl.nasa.gov/images?search=&category=Mars"
    browser.visit(url)


    # In[9]:


    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Open full size image
    browser.click_link_by_partial_text('Image')


    # In[10]:


    soup.find("div", class_="BaseImagePlaceholder")


    # In[11]:


    # Print featured image url
    featured_image_url = soup.find("div", class_="BaseImagePlaceholder").find("img")["data-src"]
    print(featured_image_url)


    # In[12]:


    browser.quit()


    # In[13]:


    # Read Mars facts table
    url = "https://space-facts.com/mars/"


    # In[14]:


    tables = pd.read_html(url)
    tables


    # In[15]:


    df = tables[0]
    df.columns = ["", "Mars"]
    mars_facts = df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    df.head()


    # In[16]:


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[23]:


    # Open Splinter browser
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


    # In[34]:


    browser.click_link_by_partial_text('Cerberus')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[35]:


    anchors = soup.find_all("a", target="_blank")


    # In[41]:


    hemisphere_image_urls = []

    for anchor in anchors:
        if anchor.text.strip() == "Sample":
            image_url = anchor["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(a)


    # In[42]:


    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[43]:


    for anchor in anchors:
        if anchor.text.strip() == "Sample":
            image_url = anchor["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(a)


    # In[44]:


    browser.click_link_by_partial_text('Major Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[45]:


    for anchor in anchors:
        if anchor.text.strip() == "Sample":
            image_url = anchor["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(a)


    # In[46]:


    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[47]:


    for anchor in anchors:
        if anchor.text.strip() == "Sample":
            image_url = anchor["href"]

    title = soup.find("h2", class_="title").text

    a = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(a)
    hemisphere_image_urls

    # In[ ]:


    browser.quit()



    Mars_dict = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url" : featured_image_url,
        "mars_facts" : mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    print(Mars_dict)
    return Mars_dict

if __name__ == "__main__":
    scrape_info()
