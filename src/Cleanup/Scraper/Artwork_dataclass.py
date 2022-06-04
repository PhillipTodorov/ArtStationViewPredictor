from dataclasses import dataclass


@dataclass
class Artwork_variables:
    # These are found on the 'href' page
    likes: int
    views: int
    comments: int
    tags: list[str]
    software_used: list[str]
    # these are found on the 'href/artist_profile/profile' page
    skills: list[str]
    location: str
    no_of_followers: int
    no_of_likes: int
    no_of_following: int

