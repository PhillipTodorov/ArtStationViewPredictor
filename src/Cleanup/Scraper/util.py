# flake8: noqa=F821
from csv import reader, writer
from xmlrpc.client import Boolean

from Website import Artwork


def get_hrefs():  # -> list[str]:
    artwork = Artwork(URL="")
    # print(artwork.csv_file)

    with open(artwork.csv_file, "r", encoding="utf-8", newline="") as f:
        artworkreader = reader(f)
        print(artworkreader)
        return artworkreader

    pass


def save_artwork_to_csv(artwork: Artwork, csv_file: str = None, DEBUG=False):
    if csv_file is None:
        csv_file = artwork.csv_file

    with open(csv_file, "a+", encoding="utf-8", newline="") as f:
        writer_object = writer(f)
        writer_object.writerow(artwork.attribute_tuple())

    if DEBUG:
        print(artwork.attribute_tuple())


def append_hrefs_from_web_element_to_csv(web_element, csv_file_dir, DEBUG=False):
    # returns a list of HTML elements contained in web_element

    def clean_web_element(outerHTML: str):
        # takes the outerHTML and returns a list of href objects linking to the 100 images linked to on the community page
        listed = [d + ">" for d in outerHTML.split(">")]
        cleaned = [k for k in listed if "href" in k]
        return cleaned[:100]

    with open(csv_file_dir, "w", encoding="utf-8") as f:
        writer_object = writer(f)
        print(f"web element type: {type(web_element)}")
        cleaned = clean_web_element(web_element.get_attribute("outerHTML"))
        writer_object.writerow(cleaned)

        if DEBUG:
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
            # print(tag)
            # print(f"{tag[index_tag(tag, begin_string)+6 : index_tag(tag, end_string)]}")
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
