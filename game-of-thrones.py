from characters import characters
import requests # makes API requests (this is a third-party module)
import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps


#print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

#Chris - Print out the key names individually
def print_key(character_list):
    for person in character_list:
        print(person)

#Chris - Print out just the values
def print_value(character_list):
    for person in character_list:
        print(person["name"])

#Chris - Print both the key and the value
def print_key_value(character_list):
    for person in character_list:
        print("%s: %s" % (person, person["name"]))

#How many characters names start with "A"?
def characters_start_a(character_list):
    start_with_a = 0
    for person in character_list:
        if "A" == person["name"][0]:
            start_with_a += 1
    return(start_with_a)

#How many characters names start with "Z"?
def characters_start_z(character_list):
    start_with_z = 0
    for person in character_list:
        if "Z" == person["name"][0]:
            start_with_z += 1
    return (start_with_z)

#How many characters are dead?
def dead_characters(character_list):
    dead = 0
    for person in character_list:
        death = len(person["died"])
        if death > 0:
            dead += 1
    return dead

#Who has the most titles?
def title_count(character_list):
    # sorted(len(characters[501]["titles"]))
    # return character_list[0]["titles"]
    title_max = 0
    for person in character_list:
        if len(person["titles"]) > title_max:
            title_name = person["name"]
            title_max = len(person["titles"])
    return title_name

#How many are Valyrian?
def valyrian_count(character_list):
    val_count = 0
    for person in character_list:
        if person["culture"] == "Valyrian":
            val_count += 1
    return val_count

#What actors plays "Hot Pie" (and don't use IMDB)?
def who_played(character_list, name):
    for person in character_list:
        if person["name"] == name:
            return person["playedBy"]

#How many characters are not in the TV show?
def book_not_tv(character_list):
    result = 0
    for person in character_list:
        if len(person["tvSeries"][0]) == 0:
            result += 1
    return result

#Produce a list of characters with the last name "Targaryen"?
def last_name_count(character_list, last_name):
    result = 0
    for person in character_list:
        if last_name in person["name"]:
            result += 1
    return result

#Create a histogram of the houses (it's the "allegiances" key)
def house_count(character_list):
    house = {}
    for person in character_list:
        for i in person["allegiances"]:
            house_type = i
            if house_type not in house:
                house[house_type] = 1
            else:
                house[house_type] += 1
    return house

#Chris - Count the number of people who are part of a house
def make_house_histogram(character_list):
    histogram = {}

    #for-loop to go through characters
    for person in character_list:
        allegiances = person["allegiances"] 
        #allegiances is a list with URLs
        for house in allegiances:
            if house in histogram:
                histogram[house] += 1
            else:
                histogram[house] = 1

    #return 
    return histogram

#Print histogram in better, more-readable format
def pretty_print_historgram(histogram):
    for house in histogram:
        print("%s has %d members" % (house, histogram[house]))

#Translate address to house name
def translate_address_to_house_name(URL):
    house_name = ""
    
    r = requests.get(URL) #Brings the Response
    house_info = r.json() #Converts Response data into Python Dictionary
    house_name = house_info["name"]

    return house_name

#Translate histogram to names
def convert_to_nice_names(histogram):
    nice_histogram = {}

    for url in histogram:
        house_name = translate_address_to_house_name(url)
        nice_histogram[house_name] = histogram[url]
        time.sleep(0.1) #Delays for tenth of a second to prevent from rapid call to URL

    return nice_histogram

#Chris - Most Character Titles using a for loop
def most_titles_1(character_list):
    most_titles = 0
    person_with_most = ""

    #for loop used to see if they have the most titles and update most_titles if they do
    for person in character_list:
        num_titles = len(person["titles"])
        if num_titles > most_titles:
            most_titles = num_titles
            person_with_most = person["name"]

    return "%s has %d titles" % (person_with_most, most_titles)

#Chris - using sort method to sort character list and return top 10 list
# def most_titles_sort(character_list):





# print(most_titles_sort(characters))
# print(len(characters[501]["titles"]))
# ugly_histogram = make_house_histogram(characters)
# convert_name = convert_to_nice_names(ugly_histogram)
# pretty_print_historgram(convert_name)