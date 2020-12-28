"""
Filename: drop.py
Description: This task involves computing the largest drops in life expectancy experienced
             across any portion of the entire timeline.
@author: Isaias Villalobos
Date: 12/10/17
"""
# program imports, defined data structures, function definitions here


##### YEARS WITH EMPTY STRINGS ARE BEING PASSED IN
from rit_lib import *
from utils import *

Range = struct_type("Range",(str,'country'),(int,'year1'), (int,'year2'),(float,'value1'),(float,'value2'))


def sorted_drop_data(data):
    """
    :param data: Tuple of 4 dictionaries
    :return: List of Range structures
    """

    CODE_TO_LIFE = data[3]
    REGION_TO_COUNTRY_DICT = data[2]
    INCOME_TO_COUNTRY_CODE_DICT = data[1]
    COUNTRY_CODE_TO_NAME = data[0]
    # DATA IS A TUPLE OF 4 DICTIONARIES

    lst_of_range_values = []

    ######## THIS IS ITERATION FOR THE YEAR 1 AND YEAR 2 CALCULATION   ##########
    for country in COUNTRY_CODE_TO_NAME:

        life_tracker = 100 #### ARBITRARY NUMBER #######
        year_one_tracker = 0
        year_two_tracker = 0

        count = 0
        for year_ONE in range(2016 - 1960): ## life_ex_1 is INTEGER ##

            if CODE_TO_LIFE[country][year_ONE] == '': ### CRITICALY IMPORTANT ###
                count += 1
                continue

            life_ex_1 = float(CODE_TO_LIFE[country][year_ONE]) ##### GETS THE LIFE EXP. FOR SPECIFED YEAR


            for year_TWO in range(year_ONE + 1, 2016 - 1960):
                if CODE_TO_LIFE[country][year_TWO] == '':  ### CRITICALY IMPORTANT ##
                    continue

                life_ex_2 = float(CODE_TO_LIFE[country][year_TWO]) ## life_ex_2 is INTEGER ##

                life_change = life_ex_2 - life_ex_1

                if life_change < life_tracker:
                    life_tracker = life_change

                    year_one_tracker = year_ONE
                    year_two_tracker = year_TWO

        if life_tracker == 100:
            continue

        if count <= 54:
            range1 = Range(COUNTRY_CODE_TO_NAME[country], year_one_tracker + 1960, year_two_tracker + 1960, float(CODE_TO_LIFE[country][year_one_tracker]), float(CODE_TO_LIFE[country][year_two_tracker]))
            lst_of_range_values += [range1]

        #################### USE THE REGION OR INCOME TO SORT FOR ALL AND THEN GIVE YOUJ ALL THE COUNTRIES AND TAKE OUT THE NON COUNTRIES ################

    lst_of_range_values.sort(key=lambda x: x.value2 - x.value1)

    return lst_of_range_values


def main():
    """
    Calls the read data function, filter region, filter income, and drop function
    Does some printing
    No return
    """
    filename = "worldbank_life_expectancy"
    data = read_data(filename)
    data = filter_region(data,'all')
    data = filter_income(data,'all')

    drop_lst = sorted_drop_data(data) ##### RETURNS LIST OF RANGE STRUCTURES

    print("Worst life expectancy drops: 1960 to 2015")

    for i in range(0, len(drop_lst)):
        if i == 10:
            break
        else:
            print(i+1,": ",drop_lst[i].country," from ", drop_lst[i].year2," (",drop_lst[i].value2,") to ", drop_lst[i].year1," (",drop_lst[i].value1,"): " ,drop_lst[i].value2 - drop_lst[i].value1,  sep='')

if __name__ == "__main__":
    # main runs only when directly invoking this module
    main()
    # end of program file