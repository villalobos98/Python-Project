"""
Filename: ranking.py
Description: This task involves processing the data and rank ordering it for a given year
@author: Isaias Villalobos
Date: 11/20/17
"""

from rit_lib import *
from utils import *

countryValue = struct_type("countryValue", (str, "country"), (float, "value"))


def sorted_ranking_data(data, year):
    """
    :param data: containing information from the data and metadata files
    :param year: integer representing the year under consideration.
    :return: A list of CountryValue structures
    """
    CODE_TO_LIFE = data[3]
    REGION_TO_COUNTRY_DICT = data[2]
    INCOME_TO_COUNTRY_CODE_DICT = data[1]
    COUNTRY_CODE_TO_NAME = data[0]
    #DATA IS A TUPLE OF 4 THINGS

    lst_of_country_values = []

    for code in COUNTRY_CODE_TO_NAME:
        life_ex = CODE_TO_LIFE[code][int(year) - 1960]
        if life_ex == '':
            continue
        countryValue1 = countryValue(COUNTRY_CODE_TO_NAME[code],float(life_ex))
        lst_of_country_values += [countryValue1]


    lst_of_country_values.sort(key=lambda x: x.value, reverse=True)

    return lst_of_country_values

def main():
    """
    CALLS THE READ DATA FUNCCTION, FILTER REGION, FILTER INCOME
    """
    while True:
        filename = "worldbank_life_expectancy"

        data = read_data(filename)

        year = input("Enter year of interest (-1 to quit): ")
        if int(year) == -1:
            break
        region = input("Enter region (type ’all’ to consider all): ")
        if region == '':
            print("Enter valid string")
            break
        income = input("Enter income of interest (-1 to quit): ")



        filtered_data = filter_region(data,region)
        filter_data_again = filter_income(filtered_data, income)

        country_lst = sorted_ranking_data(filter_data_again, year)
        # print(country_lst)
        # exit()

        print("Top 10 Life Expectancy for", year)

        for i in range(0, len(country_lst)):
            if i == 10:
                break
            else:
                print(str(i+1),country_lst[i].country, country_lst[i].value)

        reversed_country_list = list(reversed(country_lst))
        print()
        print("Bottom 10 Life Expectancy for", year)

        for i in range(0, len(reversed_country_list)):
            if i == 10:
                break
            else:
                print(str(i+1),reversed_country_list[i].country, reversed_country_list[i].value)





if __name__ == "__main__":
    # main runs only when directly invoking this module
    main()
    # end of program file
