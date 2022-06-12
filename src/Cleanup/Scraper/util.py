# flake8: noqa=F821
from asyncore import write
from csv import reader, writer
from distutils.debug import DEBUG
from genericpath import exists
from lib2to3.pgen2.driver import Driver
from xmlrpc.client import Boolean
from os import remove

from tomlkit import value
from Website import Artwork
from Website import Website_Community
from scraper_variables import (
    artwork_variables_csv_path,
    artwork_variables_temp_csv_path,
    webdriver_used,
    likes_css_selector_path,
    views_css_selector_path,
    comments_css_selector_path,
    tags_css_selector_path,
)
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_from_href_and_profile_page(href: str, driver) -> tuple[str]:

    artwork_website = Website_Community(
        URL=href,
        csv_file=artwork_variables_csv_path,
        driver=webdriver_used,
        # element_path: placeholder, replace with the 10
        # variables on each iteration (inefficient)
        element_path="",
        element_type=By.CSS_SELECTOR,
    )

    def extract_from_href_page() -> tuple[str]:
        driver.get(href)
        "extract likes, views, comments and tags from main page"
        likes = get_web_element_new(likes_css_selector_path, driver)[0].get_attribute(
            "innerText"
        )
        views = get_web_element_new(views_css_selector_path, driver, DEBUG=True)[
            0
        ].get_attribute("innerText")
        comments = get_web_element_new(comments_css_selector_path, driver, DEBUG=True)[
            0
        ].get_attribute("innerText")
        tags = ["placeholder"]
        return (likes, views, comments, tags)

    def extract_from_profile_page():
        pass

    return extract_from_href_page()


def save_into_temp_csv(
    variables: tuple[str], temp_csv: str = artwork_variables_temp_csv_path
) -> None:
    with open(temp_csv, "a+", encoding="utf-8", newline="") as f:
        writer_object = writer(f)
        writer_object.writerow(variables)
    pass


def overwrite_Artwork_variables():
    pass


def get_web_element_new(
    web_element: str, driver, web_element_type: str = By.CSS_SELECTOR, DEBUG=False
):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((web_element_type, web_element))
    )

    if DEBUG:
        print(f"web element type (util.py): {web_element_type}")
        print(f"web element value (util.py): {web_element}")
        print(f"1st element type (util.py): {type(element[0])}")
        print(f"1st element (util.py): {element[0]}")
        print(f"1st element tag_name (util.py): {element[0].tag_name}")
        print(
            f"1st element innerText (util.py): {element[0].get_attribute('innerText')}"
        )
        print(
            f"list of elements innerText(util.py): {[e.get_attribute('innerText') for e in element]}"
        )

    return element


def get_hrefs(DEBUG=False):  # -> list[str]:
    artwork = Artwork(URL="")
    if DEBUG:
        print(artwork.csv_file)
    href_list = []
    with open(artwork.csv_file, "r", encoding="utf-8", newline="") as f:
        artworkreader = reader(f)
        for row in artworkreader:
            href_list.append(row[0])
    if DEBUG:
        print(f"Href list: {href_list}")
    return href_list[1:]


def save_artwork_to_csv(artwork: Artwork, csv_file: str = None, DEBUG=False):
    """
    wipes artwork.csv_file clean and adds header, then appends all
    """
    if csv_file is None:
        csv_file = artwork.csv_file

    with open(csv_file, "a+", encoding="utf-8", newline="") as f:
        writer_object = writer(f)
        writer_object.writerow(artwork.attribute_tuple())

    if DEBUG:
        print(artwork.attribute_tuple())


def instanciate_driver():
    return eval(webdriver_used)


def initialise_csv(artwork: Artwork, header: str):
    def delete_csv():
        remove(artwork.csv_file)

    def add_header_to_csv():
        with open(artwork.csv_file, "a+", encoding="utf-8", newline="") as f:
            writer_object = writer(f)
            writer_object.writerow(header)

    if exists(artwork.csv_file):
        delete_csv()
    add_header_to_csv()


def append_hrefs_from_web_element_to_csv(web_element, csv_file_dir, DEBUG=False):
    # returns a list of HTML elements contained in web_element

    def clean_web_element(outerHTML: str):
        # takes the outerHTML and returns a list of href objects linking to the 100 images linked to on the community page
        listed = [d + ">" for d in outerHTML.split(">")]
        cleaned = [k for k in listed if "href" in k]
        return cleaned[:100]

    with open(csv_file_dir, "w", encoding="utf-8") as f:
        writer_object = writer(f)
        cleaned = clean_web_element(web_element.get_attribute("outerHTML"))
        writer_object.writerow(cleaned)

        if DEBUG:
            print(f"web element type: {type(web_element)}")
            print(f"{csv_file_dir}'s content after write: {f.read()}")


def parse_csv_for_href(csv_file_dir: str, DEBUG: Boolean = False) -> list:
    # take csv file and find all the href links and make a list only containing them

    begin_string = {"identifier": "href=", "offset": 6}
    end_string = {"identifier": '">', "offset": 0}

    def index_tag(tag: str, string: str) -> int:
        return tag.find(str(string))

    with open(csv_file_dir, "r", encoding="utf-8") as f:

        reader_object = reader(f)
        css_tags = [row for row in reader_object][0]
        href_values = []

        for tag in css_tags:
            href_values.append(
                tag[
                    index_tag(tag, begin_string["identifier"])
                    + begin_string["offset"] : index_tag(tag, end_string["identifier"])
                    + end_string["offset"]
                ]
            )

        if DEBUG:
            print(f"csv file : {csv_file_dir}")
            print(f"reader object type: {reader_object}")
            [print(f"href_values {i}") for i in href_values]

        return href_values


def driver_get(URL: str, driver, DEBUG=False):
    driver.get(URL)
    if DEBUG:
        print(f"driver get successful for {URL}")
