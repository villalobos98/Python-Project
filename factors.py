"""
Filename: factors.py
Description: This task involves looking at how region and income affect life expectancy.
             Turtle graphics is used to generate plots to visualize the data.
@author: Isaias Villalobos
Date: 12/10/17
"""
# program imports, defined data structures, function definitions here

import turtle as t
from utils import *
from statistics import median


def median_region(data):
    """
    :param data: Tuple of 4 dictionaries
    :return: No return
    Turtle starts off in the corner x pos at -500 and y pos -500
    DRAWS AND DRAWS WITH TURTLE
    """
    dummy_lst = []
    real_lst = []

    CODE_TO_LIFE = data[3]
    REGION_TO_COUNTRY_DICT = data[2]
    INCOME_TO_COUNTRY_CODE_DICT = data[1]
    COUNTRY_CODE_TO_NAME = data[0]

    ######  THE BEGINNING OF TURTLE STUFF #########
    t.speed(0)
    t.shapesize(5, 5, 5)
    t.width(5)
    t.up()
    t.setpos(-500, -500)
    # t.setworldcoordinates(-300,-300,300,300)
    t.left(90)
    t.down()
    t.fd(900)
    t.bk(900)
    t.rt(90)
    t.fd(900)
    t.bk(900)
    t.down()
    t.lt(180)
    t.up()
    t.fd(50)

    ##### THIS PART IS TO DRAW THE LIFE EXP ########
    t.fd(100)
    t.rt(90)
    t.fd(500)
    t.rt(90)
    t.write("Life", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.write("Exp", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(450)
    t.lt(90)
    t.fd(100)
    t.rt(180)

    #### DRAW THE AXIS #######
    t.write("0", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(100)
    t.write("10", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("20", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("30", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("40", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("50", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("60", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("70", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("80", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("90", move=False, align="left", font=("Arial", 11, "normal"))
    t.bk(950)
    t.rt(90)
    t.fd(50)
    t.write("1960", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(900)
    t.write("2015", move=False, align="left", font=("Arial", 11, "normal"))
    t.bk(900)

    #### lABEL THE AXIS ###
    t.fd(450)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.write("Year", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.bk(50)
    t.lt(90)
    t.bk(450)

    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.lt(90)
    t.fd(1100)
    t.rt(90)
    t.fd(100)

    ##### WRITING LOW INCOME #####
    t.pencolor("blue")
    t.write("Sub-Saharan Africa", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.down()
    t.pencolor("blue")
    t.pensize(50)
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    ##### WRITING UPPER MIDDLE INCOME ###@@

    t.down()
    t.pencolor("red")
    t.write("South Asia", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("red")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    ##### WRITING LOWER MIDDLE INCOME ###@@
    t.pencolor("green")
    t.write("Europe & Central Asia", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("green")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    #### MAKE THE LOWER MIDDLE INCOME ####
    t.pencolor("orange")
    t.write("Latin America & Carribbean", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("orange")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)

    t.pencolor("black")
    t.write("Middle East & North Africa", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("black")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)

    t.pencolor("yellow")
    t.write("North America", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("yellow")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)

    t.pencolor("purple")
    t.write("East Asia & Pacific", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("purple")
    t.write("_________", move=False, align="left", font=("Arial", 11, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    # t.done()

    ##### FINISHED WRITING ALL THE WORDS ####
    t.width(2)
    l = ["orange", "red", "blue", "green", "black", "purple", "yellow"]
    a = 0
    for region in REGION_TO_COUNTRY_DICT:
        x = -500
        t.up()
        if region != "":
            t.color(l[a])
            a += 1
            for index in range(2016 - 1960):
                for code in REGION_TO_COUNTRY_DICT[region]:
                    life_ex = CODE_TO_LIFE[code]
                    ## GRABS 55 THINGS ##
                    if life_ex[index] == '':  ### CRITICALY IMPORTANT ###
                        continue
                    life_ex_value = float(life_ex[index])
                    dummy_lst.append(life_ex_value)

                if (len(dummy_lst) != 0):
                    y_cor = (median(dummy_lst) * 10) - 500
                    if x != -500:
                        t.down()
                    else:
                        t.up()
                    t.goto(x, y_cor)
                    x += 16

                if (len(dummy_lst) != 0):
                    real_lst.append(median(dummy_lst))
                else:
                    real_lst.append(0)
                dummy_lst = []

                # print(len(real_lst))  #### REAL LIST CONTAINS ALL 263 MEDIANS FOR EACH COUNTRY
                # t.clear()


def median_income(data):
    """
    :param data: Tuple of 4 dictionaries
    :return: No return
    """
    t.pencolor("black")
    dummy_lst = []
    real_lst = []

    CODE_TO_LIFE = data[3]
    REGION_TO_COUNTRY_DICT = data[2]
    INCOME_TO_COUNTRY_CODE_DICT = data[1]
    COUNTRY_CODE_TO_NAME = data[0]

    ######  THE BEGINNING OF TURTLE STUFF #########
    t.speed(0)
    t.shapesize(5, 5, 5)
    t.width(5)
    t.up()
    t.setpos(-500, -500)
    # t.setworldcoordinates(-300,-300,300,300)
    t.left(90)
    t.down()
    t.fd(900)
    t.bk(900)
    t.rt(90)
    t.fd(900)
    t.bk(900)
    t.down()
    t.lt(180)
    t.up()
    t.fd(50)

    ##### THIS PART IS TO DRAW THE LIFE EXP ########
    t.fd(100)
    t.rt(90)
    t.fd(500)
    t.rt(90)
    t.write("Life", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.write("Exp", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(450)
    t.lt(90)
    t.fd(100)
    t.rt(180)

    #### DRAW THE AXIS #######
    t.write("0", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.fd(100)
    t.write("10", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("20", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("30", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("40", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("50", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("60", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("70", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("80", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(100)
    t.write("90", move=False, align="left", font=("Arial", 11, "normal"))
    t.bk(950)
    t.rt(90)
    t.fd(50)
    t.write("1960", move=False, align="left", font=("Arial", 11, "normal"))
    t.fd(900)
    t.write("2015", move=False, align="left", font=("Arial", 11, "normal"))
    t.bk(900)

    #### LABEL THE YEAR AXIS ###

    t.fd(450)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.write("Year", move=False, align="left", font=("Arial", 11, "normal"))
    t.rt(90)
    t.bk(50)
    t.lt(90)
    t.bk(450)

    ##### CONTINUE TURTLE STUFF ###
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.lt(90)
    t.fd(1100)
    t.rt(90)
    t.fd(100)

    ##### WRITING LOW INCOME###
    t.pencolor("blue")
    t.write("Low income", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.fd(600)
    t.down()
    t.pencolor("blue")
    t.pensize(50)
    t.write("_________", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    ##### WRITING UPPER MIDDLE INCOME ###@@

    t.down()
    t.pencolor("red")
    t.write("Upper middle income", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("red")
    t.write("_________", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    ##### WRITING LOWER MIDDLE INCOME ###@@
    t.pencolor("green")
    t.write("Lower middle income", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("green")
    t.write("_________", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    #### MAKE THE LOWER MIDDLE INCOME ####
    t.pencolor("orange")
    t.write("High income", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.fd(600)
    t.pencolor("orange")
    t.write("_________", move=False, align="left", font=("Arial", 13, "normal"))
    t.up()
    t.bk(600)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    # t.done()

    ##### FINISHED WRITING ALL THE WORDS ####
    t.width(2)
    l = ["orange", "blue", "green", "red"]
    a = 0
    for income in INCOME_TO_COUNTRY_CODE_DICT:
        x = -500
        t.up()
        if income != "":
            t.color(l[a])
            a += 1
            for index in range(2016 - 1960):
                for code in INCOME_TO_COUNTRY_CODE_DICT[income]:
                    life_ex = CODE_TO_LIFE[code]
                    ## GRABS 55 THINGS ##
                    if life_ex[index] == '':  ### CRITICALY IMPORTANT ###
                        continue
                    life_ex_value = float(life_ex[index])
                    dummy_lst.append(life_ex_value)

                if (len(dummy_lst) != 0):
                    y_cor = (median(dummy_lst) * 10) - 500
                    if x != -500:
                        t.down()
                    else:
                        t.up()
                    t.goto(x, y_cor)
                    x += 16

                if (len(dummy_lst) != 0):
                    real_lst.append(median(dummy_lst))
                else:
                    real_lst.append(0)
                dummy_lst = []


                # print(len(real_lst)) #### REAL LIST CONTAINS ALL 263 MEDIANS FOR EACH COUNTRY


def main():
    """
    CALLS THE READ DATA_FUNCTION, THE FILTER REGION, THE FILTER INCOME FUNCTION
    """
    filename = "worldbank_life_expectancy"

    data = read_data(filename)
    data1 = filter_income(data, 'all')

    median_income(data1)

    user_input = input("Hit Enter to continue: ")

    if user_input == '':
        t.clear()

        data2 = filter_region(data, 'all')
        median_region(data2)
        t.done()


# main’s code body here...
if __name__ == "__main__":
    # main runs only when directly invoking this module
    main()
    # end of program file
