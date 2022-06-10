# flake8: noqa=F501

artstation_community_csv_path = "src/Cleanup/Scraper/Artstation_community.csv"
webdriver_used = "webdriver.Firefox()"
community_url = "https://www.artstation.com/?sort_by=community"
artwork_variables_csv_path = "src/Cleanup/Scraper/Artwork_variables.csv"
artwork_variables_header = [
    "URL",
    "post_age_weeks",
    "views",
    "likes",
    "tags",
    "no_of_skills",
    "software_used",
    "csv_file",
]


# used in 'dataclass_util.py'
likes_css_selector_path = ".project-meta > show-likes-button:nth-child(1) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)"
views_css_selector_path = ""
comments_css_selector_path = ""
tags_css_selector_path = []
href_css_selector_path = [
    likes_css_selector_path,
    views_css_selector_path,
    comments_css_selector_path,
    tags_css_selector_path,
]
