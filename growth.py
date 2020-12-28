"""
Filename: growth.py
Description: This task involves computing the largest drops in life expectancy experienced
             across any portion of the entire timeline.
@author: Isaias Villalobos
Date: 12/10/17
"""
# program imports, defined data structures, function definitions here
from rit_lib import *
from utils import *

countryValue = struct_type("countryValue", (str, "country"), (float, "value"))

def sorted_growth_data(data, year1, year2):
    """
    This task has inputs of a starting year and an ending year, and involves
    computing and rank ordering the absolute growth in life expectancy over the time
    period
    :param data: Dictionaries
    :param year1: String year that the user entered
    :param year2: String that the user entered
    :return: List of countryValue structures
    """
    CODE_TO_LIFE = data[3]
    REGION_TO_COUNTRY_DICT = data[2]
    INCOME_TO_COUNTRY_CODE_DICT = data[1]
    COUNTRY_CODE_TO_NAME = data[0]
    # DATA IS A TUPLE OF 4 THINGS

    lst_of_country_values = []

    ######## THIS IS FOR YEAR 1 AND YEAR 2   ##########
    for value in COUNTRY_CODE_TO_NAME:
            life_ex_1 = CODE_TO_LIFE[value][int(year1) - 1960] ##### GETS THE LIFE EXP. FOR SPECIFED YEAR
            life_ex_2 = CODE_TO_LIFE[value][int(year2) - 1960]

            if life_ex_1 == '' or life_ex_2 == '':
                continue

            life_change = float(life_ex_2) - float(life_ex_1)

            countryValue1 = countryValue(COUNTRY_CODE_TO_NAME[value], float(life_change))
            lst_of_country_values += [countryValue1]

    #################### USE THE REGION OR INCOME TO SORT FOR ALL AND THEN GIVE YOUJ ALL THE COUNTRIES AND TAKE OUT THE NON COUNTRIES ################

            # countryValue1 = countryValue(COUNTRY_CODE_TO_NAME[country_code], float(life_change))
            # lst_of_country_values += [countryValue1]


    lst_of_country_values.sort(key=lambda x: x.value, reverse=True)

    return lst_of_country_values


###SUBTRACT LARGER FROM SMALLER


def main():
    """
    CALLS THE READ DATA FUNCTION, FILTER REGION AND FILTER INCOME
    GETS INPUT FROM THE USER.
    DOES SOME PRINTING
    """
    while True:
        year1 = input("Enter starting year of interest (-1 to quit): ")
        if year1 == '-1':
            exit()
        year2 = input("Enter ending year of interest (-1 to quit): ")
        if year2 == '-1':
            exit()
        region = input("Enter region (type ’all’ to consider all): ")
        income = input("Enter income category (type ’all’ to consider all): ")
        filename = "worldbank_life_expectancy"

        data = read_data(filename)

        data1 = filter_region(data, region)

        data2 = filter_income(data1, income)
        country_lst = sorted_growth_data(data2, year1, year2)

        # country_lst = sorted_growth_data(data, year1, year2)

        print("Top 10 Life Expectancy Growth:", year1, "to", year2)

        for i in range(0, len(country_lst)):
            if i == 10:
                break
            else:
                print(str(i+1),country_lst[i].country, country_lst[i].value)

        reversed_country_list = list(reversed(country_lst))
        print()
        print("Bottom 10 Life Expectancy Growth:", year1, "to", year2)

        for i in range(0, len(reversed_country_list)):
            if i == 10:
                break
            else:
                print(str(i+1),reversed_country_list[i].country, reversed_country_list[i].value)

        print()
# main’s code body here...
if __name__ == "__main__":
    # main runs only when directly invoking this module
    main()
    # end of program file
