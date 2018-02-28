"""Restaurant rating lister."""

import sys

file_name = sys.argv[1]

opened_file = open(file_name)

def get_restaurant_ratings():
    """takes input from file and stores it in a dictionary"""

    restaurant_ratings = {}

    for line in opened_file:
        list_of_restaurant = line.rstrip().split(":")
        #list_of_restaurant.sort()

        restaurant_ratings[list_of_restaurant[0]] = list_of_restaurant[1]

    print_restaurant_ratings(restaurant_ratings)

    return restaurant_ratings



def get_user_restaurant():
    """get input from user about new resturant"""

    restuant_name = raw_input ("Enter a name of resturant: ")
    user_rating = raw_input("Enter the rating for that restaurant(1-5) ")

    return (restuant_name,user_rating)


def add_user_input_to_dictionary(dictionary, user_args):

    dictionary[user_args[0]] = user_args[1]

    return print_restaurant_ratings(dictionary)


def print_restaurant_ratings(restaurant_dictionary):

     for resturant, rating in sorted(restaurant_dictionary.items()):
        print "{} is rated at {}".format(resturant, rating)


add_user_input_to_dictionary(get_restaurant_ratings(), get_user_restaurant())

opened_file.close()