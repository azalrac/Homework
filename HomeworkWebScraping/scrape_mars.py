# coding: utf-8
#
import os
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time
import pandas as pd

def scrape():
    # # Mars Headline
    chrome_driver = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **chrome_driver, headless=True)

    nasa_url = 'https://mars.nasa.gov/news'
    browser.visit(nasa_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find('div', class_="bottom_gradient").text
    news_p = soup.find('div', class_="article_teaser_body").text

    # # JPL Image

    # chrome_driver = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **chrome_driver, headless=False)

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')

    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')


    image_path = image_soup.find('figure', class_="lede").a['href']
    featured_image_url = "https://www.jpl.nasa.gov" + image_path

    # # Mars Weather

    # chrome_driver = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **chrome_driver, headless=False)

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    weather_html = browser.html
    weather_soup = bs(weather_html, 'html.parser')

    mars_twitter = weather_soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    
    mars_weather = []
    for twitter in mars_twitter:
        if "Sol" in str(twitter):
            mars_weather.append(twitter.text)

    mars_weather[0]
    # # Mars Facts

    # chrome_driver = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **chrome_driver, headless=False)

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    facts_html = browser.html
    facts_soup = bs(facts_html, 'html.parser')

    fact_table = facts_soup.find('table', class_="tablepress tablepress-id-mars")

    table = fact_table.find_all('tr')

    labels = []
    values = []

    for tr in table:
        td_elements = tr.find_all('td')
        labels.append(td_elements[0].text)
        values.append(td_elements[1].text)

    table_df = pd.DataFrame({"Label": labels,
                            "Values": values})

    table_df

    table_html = table_df.to_html(header=False, index=False)
    table_html

    # # Mars Hemispheres

    # chrome_driver = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **chrome_driver, headless=False)

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_html = browser.html
    usgs_soup = bs(usgs_html, "html.parser")

    overall_div = usgs_soup.find('div', class_="collapsible results")
    hemispheres = overall_div.find_all('div', class_="description")

    hemisphere_urls = []

    for a in hemispheres:
        
        title = a.h3.text
        link = "https://astrogeology.usgs.gov" + a.a['href']
        
        browser.visit(link)
        time.sleep(5)
        
        images_html = browser.html
        images_soup = bs(images_html, "html.parser")
        images_link = images_soup.find('div', class_='downloads').find('li').a['href']
        
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = images_link
        
        hemisphere_urls.append(image_dict)
        
        print(hemisphere_urls)

    mars_dict = {
        "id":1,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather[0],
        "fact_table": table_html,
        "hemisphere_urls": hemisphere_urls
    }
    return mars_dict