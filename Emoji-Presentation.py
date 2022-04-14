from dataclasses import dataclass
import requests


@dataclass
class smileys_and_people:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class animals_and_nature:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class food_and_drink:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class travel_and_places:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class activities:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class objects:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class symbols:
    name: str
    group: str
    htmlCode: str
    unicode: str


@dataclass
class flags:
    name: str
    group: str
    htmlCode: str
    unicode: str



def getJSON(url): # Function makes a get request for a URL and returns a JSON Dict
    response = requests.get(url)
    return response.json()


def Emoji_List (url, class_name):
    json = getJSON(url)
    emoji_list = []
    for i in range(len(json)):
        emoji = class_name(json[i]["name"],json[i]["group"],''.join(json[i]["htmlCode"]),''.join(json[i]["unicode"]))
        emoji_list.append(emoji)
    return emoji_list


# Smileys and People
URL = 'https://emojihub.herokuapp.com/api/all/category_smileys_and_people'
smiley_list = Emoji_List(URL, smileys_and_people)


# Animals and Nature
URL = 'https://emojihub.herokuapp.com/api/all/category_animals_and_nature'
animals_list = Emoji_List(URL, animals_and_nature)


# Food and Drink
URL = 'https://emojihub.herokuapp.com/api/all/category_food_and_drink'
food_list = Emoji_List(URL, food_and_drink)


# Travel and Places
URL = 'https://emojihub.herokuapp.com/api/all/category_travel_and_places'
places_list = Emoji_List(URL, travel_and_places)

# Activities
URL = 'https://emojihub.herokuapp.com/api/all/category_activities'
activities_list = Emoji_List(URL, activities)

# Objects
URL = 'https://emojihub.herokuapp.com/api/all/category_objects'
objects_list = Emoji_List(URL, objects)


# Symbols
URL = 'https://emojihub.herokuapp.com/api/all/category_symbols'
symbols_list = Emoji_List(URL, symbols)

# Flags
URL = 'https://emojihub.herokuapp.com/api/all/category_flags'
flags_list = Emoji_List(URL, flags)



