from selenium import webdriver
from selenium.webdriver.common.by import By
from scraper_variables import artwork_variables_csv_path, webdriver_used

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

    def instancate_driver(self, DEBUG=False):
        if DEBUG:
            print(self.driver)
            print(type(self.driver))
        if eval(webdriver_used) is not None:
            self.driver = webdriver.Firefox()

        else:
            raise TypeError("driver not instanciated properly")


class Website_Community(Website):
    def __init__(
        self,
        URL: str = "",
        csv_file: str = "",
        # TODO:driver should not be str, it should be a driver object
        driver: str = "",
        # element_path: the path to the element we want to extract ie "channel-project-list.ng-star-inserted > div:nth-child(1)"
        # element_type: the format that the pathing takes ie By.CSS_SELECTOR
        element_path: str = "",
        element_type: str = "",
    ):
        Website.__init__(self, URL, csv_file, driver)
        self.element_path = element_path
        self.element_type = element_type.lower()


class Artwork(Website):
    def __init__(
        self,
        URL: str,
        post_age_weeks: int = 0,
        views: int = 0,
        likes: int = 0,
        tags: list[str] = [],
        no_of_skills: int = 0,
        software_used: list[str] = [],
        csv_file: str = artwork_variables_csv_path,
        driver: str = " ",
    ):
        Website.__init__(self, URL, csv_file, driver)
        self.post_age_weeks = post_age_weeks
        self.views = views
        self.likes = likes
        self.tags = tags
        self.no_of_skills = no_of_skills
        self.software_used = software_used

    def __repr__(self) -> str:
        return f"Artwork({self.URL},{self.post_age_weeks},{self.views},{self.tags},{self.no_of_skills},{self.software_used},{self.csv_file},{self.driver})"

    def attribute_tuple(self):
        # returns a tuple of all variables in Artwork class (except driver)
        return (
            self.URL,
            self.post_age_weeks,
            self.views,
            self.likes,
            self.tags,
            self.no_of_skills,
            self.software_used,
            self.csv_file,
        )
