import csv
import json
from distutils.debug import DEBUG

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import util
from dataclass_util import scrape_artwork_variables
from Website import Artwork, Website_Community
from scraper_variables import (
    artstation_community_csv_path,
    webdriver_used,
    community_url,
)

# flake8: noqa=F821


artstation_community = Website_Community(
    URL=community_url,
    element_path="channel-project-list.ng-star-inserted > div:nth-child(1)",
    element_type=By.CSS_SELECTOR,
    csv_file=artstation_community_csv_path,
    driver=webdriver_used,
)


def main():
    scrape_artwork_variables()
    pass


def get_HTML_from_community():
    """
    Crawl community tab for outerHTML and save to "Website_Community.csv_file"
    """
    artstation_community.instancate_driver()
    util.driver_get(artstation_community.URL, artstation_community.driver)
    web_element = artstation_community.get_web_element()
    util.append_hrefs_from_web_element_to_csv(
        web_element, artstation_community.csv_file
    )
    artstation_community.driver.quit()


def parse_HTML_for_href_save_to_csv():
    """
    Parses "Website_Community.csv_file" for hrefs and saves to csv file
    """
    href_list = util.parse_csv_for_href(artstation_community_csv_path)
    for href in href_list:
        href = Artwork(href)
        util.save_artwork_to_csv(href)


if __name__ == "__main__":
    main()
