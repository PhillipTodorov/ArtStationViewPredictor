from dataclasses import dataclass

from attr import field


@dataclass
class Artwork_variables:
    # These are found on the 'href' page
    likes: int = field(factory=int)
    views: int = field(factory=int)
    comments: int = field(factory=int)
    tags: list[str] = field(factory=list[str])
    software_used: list[str] = field(factory=list[str])
    # These are found on the 'href/artist_profile/profile' page
    skills: list[str] = field(factory=list[str])
    location: str = field(factory=str)
    no_of_followers: int = field(factory=int)
    no_of_likes: int = field(factory=int)
    no_of_following: int = field(factory=int)
