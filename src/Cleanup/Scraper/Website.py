from selenium import webdriver
from selenium.webdriver.common.by import By

# flake8: noqa=F821


class Website:
    def __init__(
        self,
        URL: str,
        csv_file: str,
        driver: str,
    ):
        self.URL = URL
        self.csv_file = csv_file
        self.driver = driver

    def __repr__(self) -> str:
        return f"Website({self.URL}, {self.csv_file}, {self.driver})"

    @property
    def get_csv_file(self):
        return self.csv_file

    def instancate_driver(self):
        if eval(self.driver) is not None:
            self.driver = eval(self.driver)
        else:
            raise TypeError("driver not instanciated properly")


class Website_Community(Website):
    def __init__(
        self,
        URL: str = "",
        csv_file: str = "",
        driver: str = "",
        element_path: str = "",
        element_type: str = "",
    ):
        Website.__init__(self, URL, csv_file, driver)
        self.element_path = element_path
        self.element_type = element_type.lower()

    def get_web_element(self):
        webelement = self.driver.find_element(
            by=self.element_type, value=self.element_path
        )

        if webdriver is not None:
            return webelement
        else:
            raise TypeError("Webelement should not be None")


class Artwork(Website):
    def __init__(
        self,
        URL: str,
        post_age_weeks: int = 0,
        views: int = 0,
        tags: list[str] = [],
        no_of_skills: int = 0,
        software_used: list[str] = [],
        csv_file: str = r"Cleanup\Scraper\artwork.csv",
        driver: str = " ",
    ):
        Website.__init__(self, URL, csv_file, driver)
        self.post_age_weeks = post_age_weeks
        self.views = views
        self.tags = tags
        self.no_of_skills = no_of_skills
        self.software_used = software_used

    def __repr__(self) -> str:
        return f"Artwork({self.URL},{self.post_age_weeks},{self.views},{self.tags},{self.no_of_skills},{self.software_used},{self.csv_file},{self.driver})"

    def attribute_tuple(self):
        # returns a tuple of all variables in Artwork class
        return (
            self.URL,
            self.post_age_weeks,
            self.views,
            self.tags,
            self.no_of_skills,
            self.software_used,
            self.csv_file,
            self.driver,
        )
