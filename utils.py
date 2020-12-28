"""
Filename: ultils.py
Description: This file contains a set of utilities which includes data structures and functions used by the
            other program tasks.
@author: Isaias Villalobos
Date: 11/20/17
"""

def valid_country_code_name(data,user_input):
    """
    :param data: Four dictionaries
    :param user_input: string parameter
    :return: A dictionary
    """
    year = 1960
    invalid = False
    dict1 = data[0]

    country_dict = {}
    data1 = open("data/worldbank_life_expectancy_data.txt")
    next(data1)
    for line in data1:
        line = line.split(",")
        country_dict[line[0]] = line[2:-1]#MAPS THE COUNTRY NAME TO THE LIFE EXPECTANACY

    while not invalid:
        if len(user_input) == 3:#
            if user_input in dict1:
                user_input = dict1[user_input]  # COUNTRY NAME
            else:
                print(user_input, "is not a country name or country code.")

        if user_input in country_dict:
            for values in country_dict[user_input]:
                if values != '':
                    print("Year", year, "Life expctanacy: ",values)
                year +=1
            year = 1960
            user_input= input("Enter name of country or country code (Enter to quit): ")

        else:
            if user_input == '':
                invalid = True
    country_code_to_life_ex = country_dict

    return country_code_to_life_ex

def read_data(filename):
    """
    Description: This function just reads the data
    :param filename: Name of the data file
    :return: Returns a tuple
    """

    file = "data/" + filename + "_data.txt"

    file2 = "data/" + filename + "_metadata.txt"

    f = open(file, 'r')
    f2 = open(file2, 'r')


    COUNTRY_CODE_TO_NAME = {}
    data1 = open(file)
    next(data1)
    for line in data1:
        line = line.split(",")
        COUNTRY_CODE_TO_NAME[line[1]]= line[0]
    ################################ MADE THE COUNTRY CODE TO NAME DICTIONARY

    INCOME_TO_COUNTRY_CODE_DICT = {}
    data2 = open(file2)
    next(data2)
    for line in data2:
        line = line.split(",")
        if line[2] in INCOME_TO_COUNTRY_CODE_DICT:
            INCOME_TO_COUNTRY_CODE_DICT[line[2]].append(line[0])
        else:

            INCOME_TO_COUNTRY_CODE_DICT[line[2]] = [line[0]]

    # print(INCOME_TO_COUNTRY_CODE_DICT)

    ################################## MADE THE INCOME TO CODE DICTIONARY

    REGION_TO_COUNTRY_DICT = {}
    data2 = open(file2)
    next(data2)
    for line in data2:
        line = line.split(",")
        if line[1] in REGION_TO_COUNTRY_DICT:
            REGION_TO_COUNTRY_DICT[line[1]].append(line[0])
        else:

            REGION_TO_COUNTRY_DICT[line[1]] = [line[0]]
    # print(REGION_TO_COUNTRY_DICT)

    ################################# MADE THE REGION TO CODE DICTIONARY

    CODE_TO_LIFE = {}
    data1 = open(file)
    next(data1)
    for line in data1:
        line = line.split(",")
        CODE_TO_LIFE[line[1]] = line[2:-1]

    ################################ MADE THE CODE TO LIFE EXPECTANCY DICTIONARY


    return COUNTRY_CODE_TO_NAME, INCOME_TO_COUNTRY_CODE_DICT, REGION_TO_COUNTRY_DICT,CODE_TO_LIFE



def filter_region(data, region):
    """
    :param data: containing information from the data and metadata files.
    :param region: string specifying a particular region by which to filter.
    :return: filtered to only retain data corresponding to the specified region
    """

    region_to_codes_dict = data[2]
    code_to_country = data[0]

    ###################  LIST OF ALL THE DICTIONARIES  ####################
    filtered_region_dict_region = {}

    if region == 'all':
        return data[0], data[1],data[2], data[3]

    for code in region_to_codes_dict[region]:
        if code != '':
            filtered_region_dict_region[code] = code_to_country[code]

    return filtered_region_dict_region, data[1], data[2], data[3]


def filter_income(data, income):
    """
    :param data: containing information from the data and metadata files
    :param income:string specifying a particular income category by which to filter
    :return:
    """

    ######## ALL THE DICTIONARIES ######
    income_to_codes_dict = data[1]
    country_code_to_name_dict = data[0]

    ###################  LIST OF ALL THE DICTIONARIES  ####################
    filtered_income_dict = {}

    if income == 'all':
        return data[0], data[1],data[2], data[3]

    for value in income_to_codes_dict[income]:
        if value != '':
            if value in country_code_to_name_dict:
                filtered_income_dict[value] = country_code_to_name_dict[value]
            # else:
        #     continue

    return filtered_income_dict,data[1], data[2],data[3]


def main():
    """
    CALLS OTHER FUNCTIONS SUCH AS FILTER REGION AND FILTER INCOME, DOES SOME PRINTING
    RUNS THIS FILE
    """
    filename = "worldbank_life_expectancy"

    DATA_TUPLE_DICTIONARIES = read_data(filename)

    COUNTRY_CODE_TO_NAME, INCOME_TO_COUNTRY_CODE_DICT, REGION_TO_COUNTRY_DICT, CODE_TO_LIFE = DATA_TUPLE_DICTIONARIES

    ################ LENGTHS OF THE DICTIONARIES #########################

    LENGTH_OF_MIDDLE_EAST = len(REGION_TO_COUNTRY_DICT['Middle East & North Africa'])  ###LENGTH OF INCOME DICTIONARY
    LENGTH_OF_EUROPE_CENTRAL_ASIA = len(REGION_TO_COUNTRY_DICT['Europe & Central Asia'])
    LENGTH_OF_NORTH_AMERICA = len(REGION_TO_COUNTRY_DICT['North America'])
    LENGTH_OF_LATIN_AMERICA_CARRIBBEAN = len(REGION_TO_COUNTRY_DICT['Latin America & Caribbean'])
    LENGTH_OF_SOUTH_ASIA = len(REGION_TO_COUNTRY_DICT['South Asia'])
    LENGTH_OF_EAST_ASIA_PACIFIC = len(REGION_TO_COUNTRY_DICT['East Asia & Pacific'])
    LENGTH_OF_SUB_SAHARAN_AFRICA = len(REGION_TO_COUNTRY_DICT['Sub-Saharan Africa'])
    LENGTH_LOWER_MIDDLE_INCOME = len(INCOME_TO_COUNTRY_CODE_DICT['Lower middle income'])
    LENGTH_UPPER_MIDDLE_INCOME = len(INCOME_TO_COUNTRY_CODE_DICT['Upper middle income'])
    LENGTH_HIGH_INCOME = len(INCOME_TO_COUNTRY_CODE_DICT['High income'])
    LENGTH_LOW_INCOME = len(INCOME_TO_COUNTRY_CODE_DICT['Low income'])

    LENGTH_TOTAL_NUMBER_OF_ENTITIES = len(COUNTRY_CODE_TO_NAME)

    ##### EMPTY SPACE HAS A COUNTRIES

    LENGTH_OF_COUNTRIES = 0
    for key in REGION_TO_COUNTRY_DICT:
        if key != '':
            LENGTH_OF_COUNTRIES += len(REGION_TO_COUNTRY_DICT[key])

    #########################  PRINTOUTS #######################

    print("Total Number of entities: ", LENGTH_TOTAL_NUMBER_OF_ENTITIES)
    print("Total Number of Countries/territories: ", LENGTH_OF_COUNTRIES)

    print()
    print("Regions and their country count:")
    print("Middle East & North Africa:", LENGTH_OF_MIDDLE_EAST)
    print("Europe & Central Asia:", LENGTH_OF_EUROPE_CENTRAL_ASIA)
    print("North America:", LENGTH_OF_NORTH_AMERICA)
    print("Latin America & Caribbean:", LENGTH_OF_LATIN_AMERICA_CARRIBBEAN)
    print("South Asia:", LENGTH_OF_SOUTH_ASIA)
    print("East Asia & Pacific:", LENGTH_OF_EAST_ASIA_PACIFIC)
    print("Sub-Saharan Africa", LENGTH_OF_SUB_SAHARAN_AFRICA)

    print()
    print("Income categories and their country count: ")
    print("Lower middle income:", LENGTH_LOWER_MIDDLE_INCOME)
    print("Upper middle income:", LENGTH_UPPER_MIDDLE_INCOME)
    print("High income:", LENGTH_HIGH_INCOME)
    print("Low income:", LENGTH_LOW_INCOME)

    print()
    ####### THE LINES BELOW ARE USED FOR CHECKING VALID INPUTS TO FILTER REGION ##################
    region = input("Enter region name: ")
    if region == '':
        exit()
    if region == "South Asia" or region == "Sub-Saharan Africa" or region == "Middle East & North Africa" or region == "Latin America & Caribbean" or region == "all":
        print() ### USED FOR FORMATTING ###
        print("Countries in the", region, "region: ")
        filter_region(DATA_TUPLE_DICTIONARIES, region)
    else:
        print("Enter valid region name")
        exit()

    #################### PRINTOUTS ##################################
    region_dict = filter_region(DATA_TUPLE_DICTIONARIES, region)[0]

    for country_codes in region_dict.keys():
        print(COUNTRY_CODE_TO_NAME[country_codes], "(", country_codes,')')


    ####### THE LINES BELOW ARE USED FOR CHECKING VALID INPUTS TO FILTER INCOME ##################
    print()
    income = input("Enter income category: ")
    if income == "Upper middle income" or income == "High income" \
            or income == "Low income" or income == "Lower middle income":
        print("Countries in the", income, "income category: ")
        filter_income(DATA_TUPLE_DICTIONARIES, income)

    else:
        print("Enter valid income string")
        exit()
    #################### PRINTOUTS ##################################
    income_dict = filter_income(DATA_TUPLE_DICTIONARIES, income)[1]

    for codes in income_dict.values():
        for code in codes:
            print(COUNTRY_CODE_TO_NAME[code], "(", code, ')')

    #########################################

    print()#USED FOR FORMATTING
    user_input = input("Enter name of country or country code (Enter to quit): ")
    valid_country_code_name(DATA_TUPLE_DICTIONARIES,user_input)




# main’s code body here...
if __name__ == "__main__":
    # main runs only when directly invoking this module
    main()

# end of program file
