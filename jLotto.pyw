# jLotto 2022 (c) jTech
# Import the os module for opening a file in the computer
import os

# Import the random module for generating lucky numbers
import random

# Import the tkinter module for creating graphic user interface (GUI)
import tkinter
from tkinter import *

# Import the messagebox module for giving info to the user when clicking Save
from tkinter import messagebox

# Import the webbrowser module for directing the user to the Readme page
import webbrowser

# Create a new function called "Show Output", which gets integer number transformed from the text number input
def show_output():
    # Romdonly select the three-digit lucky numbers four times
    threeDigitLottoNumber1 = str(random.randint(0, 999))
    threeDigitLottoNumber2 = str(random.randint(0, 999))
    threeDigitLottoNumber3 = str(random.randint(0, 999))
    threeDigitLottoNumber4 = str(random.randint(0, 999))
    # Romdonly select the two-digit lucky number one time
    twoDigitLottoNumber = str(random.randint(0, 99))
    # Put zero tp the left.
    luckyThreeNumber1 = threeDigitLottoNumber1.zfill(3)
    luckyThreeNumber2 = threeDigitLottoNumber2.zfill(3)
    luckyThreeNumber3 = threeDigitLottoNumber3.zfill(3)
    luckyThreeNumber4 = threeDigitLottoNumber4.zfill(3)
    luckyTwoNumber = twoDigitLottoNumber.zfill(2)
    # Define correct numbers. If correct, show the numbers. Otherwise, show nothing.
    if buyThreeDigitNumber1_input.get() in [luckyThreeNumber1,
                                            luckyThreeNumber2,
                                            luckyThreeNumber3,
                                            luckyThreeNumber4,
                                            luckyTwoNumber]:
        number1Correct =  buyThreeDigitNumber1_input.get()
    else:
        number1Correct = ""

    if buyThreeDigitNumber2_input.get() in [luckyThreeNumber1,
                                            luckyThreeNumber2,
                                            luckyThreeNumber3,
                                            luckyThreeNumber4,
                                            luckyTwoNumber]:
        number2Correct =  buyThreeDigitNumber2_input.get()
    else:
        number2Correct = ""

    if buyThreeDigitNumber3_input.get() in [luckyThreeNumber1,
                                            luckyThreeNumber2,
                                            luckyThreeNumber3,
                                            luckyThreeNumber4,
                                            luckyTwoNumber]:
        number3Correct =  buyThreeDigitNumber3_input.get()
    else:
        number3Correct = ""

    if buyThreeDigitNumber4_input.get() in [luckyThreeNumber1,
                                            luckyThreeNumber2,
                                            luckyThreeNumber3,
                                            luckyThreeNumber4,
                                            luckyTwoNumber]:
        number4Correct =  buyThreeDigitNumber4_input.get()
    else:
        number4Correct = ""

    if buyThreeDigitNumber5_input.get() in [luckyThreeNumber1,
                                            luckyThreeNumber2,
                                            luckyThreeNumber3,
                                            luckyThreeNumber4,
                                            luckyTwoNumber]:
        number5Correct =  buyThreeDigitNumber5_input.get()
    else:
        number5Correct = ""

    # Check if each number is a lucky number and notify the user.
    if buyThreeDigitNumber1_input.get() in [luckyThreeNumber1, luckyThreeNumber2,
                                            luckyThreeNumber3, luckyThreeNumber4,
                                            luckyTwoNumber]:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
                 + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
                 + luckyTwoNumber + " " + "คุณถูกรางวัล เลข " + number1Correct  + " " \
                 + number2Correct  + " " + number3Correct  + " " + number4Correct \
                 + " " + number5Correct
    elif buyThreeDigitNumber2_input.get() in [luckyThreeNumber1, luckyThreeNumber2,
                                              luckyThreeNumber3, luckyThreeNumber4,
                                              luckyTwoNumber]:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
             + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
             + luckyTwoNumber + " " + "คุณถูกรางวัล เลข" + " " + number1Correct  + " " \
                 + number2Correct  + " " + number3Correct  + " " + number4Correct \
                 + " " + number5Correct
    elif buyThreeDigitNumber3_input.get() in [luckyThreeNumber1, luckyThreeNumber2,
                                            luckyThreeNumber3, luckyThreeNumber4,
                                             luckyTwoNumber]:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
             + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
             + luckyTwoNumber + " " + "คุณถูกรางวัล เลข" + " " + number1Correct  + " " \
                 + number2Correct  + " " + number3Correct  + " " + number4Correct \
                 + " " + number5Correct
    elif buyThreeDigitNumber4_input.get() in [luckyThreeNumber1, luckyThreeNumber2,
                                            luckyThreeNumber3, luckyThreeNumber4,
                                              luckyTwoNumber]:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
             + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
             + luckyTwoNumber + " " + "คุณถูกรางวัล เลข" + " " + number1Correct  + " " \
                 + number2Correct  + " " + number3Correct  + " " + number4Correct \
                 + " " + number5Correct
    elif buyThreeDigitNumber5_input.get() in [luckyThreeNumber1, luckyThreeNumber2,
                                            luckyThreeNumber3, luckyThreeNumber4,
                                              luckyTwoNumber]:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
             + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
             + luckyTwoNumber + " " + "คุณถูกรางวัล เลข" + " " + number1Correct  + " " \
                 + number2Correct  + " " + number3Correct  + " " + number4Correct \
                 + " " + number5Correct
    else:
        output = luckyThreeNumber1 + " " + luckyThreeNumber2 \
                 + " " + luckyThreeNumber3 + " " + luckyThreeNumber4 + " " \
                 + luckyTwoNumber

    # Show the output as Arial text, 20 px
    output_label.configure(
        text=output,
        # Set the output's font as Arial with the size of 25
        font=('Arial', 20)
    )
    # Get the number from the entry
    threeDigitNumberBuy1 = buyThreeDigitNumber1_input.get()
    threeDigitNumberBuy2 = buyThreeDigitNumber2_input.get()
    threeDigitNumberBuy3 = buyThreeDigitNumber3_input.get()
    threeDigitNumberBuy4 = buyThreeDigitNumber4_input.get()
    threeDigitNumberBuy5 = buyThreeDigitNumber5_input.get()

    # Open the text file for recording the numbers
    luckyNumberFile = open("luckyNumber.txt", "a", encoding="utf-8")
    allNumbersBuy = threeDigitNumberBuy1 + " " + threeDigitNumberBuy2 + " " + \
                    threeDigitNumberBuy3 + " " + threeDigitNumberBuy4  + " " + \
                    threeDigitNumberBuy5
    # Write the number to buy in the text file
    luckyNumberFile.write(allNumbersBuy + "\n")
    # Indend in the next line
    luckyNumberFile.write(" ")
    # Write the lucky numbers in the text file
    luckyNumberFile.write("เลขที่ออก " + output + "\n")
    # Close the file
    luckyNumberFile.close()

# Create a Check ID function. To open the customer ID file
def checkNumber():
    # Define which file is the number file
    luckyNumberFile = "luckyNumber.txt"
    # Use the default editor to open the file
    os.startfile(luckyNumberFile)

# Create Open Readme function. To open the url
def openReadMe():
    # Define which url to pen
    webbrowser.open('https://github.com/Kietpawpan/jLotto#readme')

# Create a graphic user interface (GUI) for this application
window = Tk()

# Set the size of the GUI as 450 x 200 px
window.geometry("900x500")

# Set the name of my app as Lotto 2022.
window.title("jTech")

# Set the text on what this app does and show it in the window with space between lines at 20 px.
title_label = tkinter.Label(master=window, text='jLotto')
title_label.place(x=200, y=10)

# Define the number-to-buy variable
threeDigitNumberBuy1 = StringVar
threeDigitNumberBuy2 = StringVar
threeDigitNumberBuy3 = StringVar
threeDigitNumberBuy4 = StringVar
threeDigitNumberBuy5 = StringVar

# Create an entry box for the number-to-buy variable, and its location
buyThreeDigitNumber1_input = tkinter.Entry(textvariable=threeDigitNumberBuy1, width=10, font=("",12))
buyThreeDigitNumber1_input.place(x=15,y=40)

buyThreeDigitNumber2_input = tkinter.Entry(textvariable=threeDigitNumberBuy2, width=10, font=("",12))
buyThreeDigitNumber2_input.place(x=15,y=100)

buyThreeDigitNumber3_input = tkinter.Entry(textvariable=threeDigitNumberBuy3, width=10, font=("",12))
buyThreeDigitNumber3_input.place(x=15,y=160)

buyThreeDigitNumber4_input = tkinter.Entry(textvariable=threeDigitNumberBuy4, width=10, font=("",12))
buyThreeDigitNumber4_input.place(x=15,y=220)

buyThreeDigitNumber5_input = tkinter.Entry(textvariable=threeDigitNumberBuy5, width=10, font=("",12))
buyThreeDigitNumber5_input.place(x=15,y=280)

# Label the entry box and set its location
buyNumber_text1 = Label(text="ตัวที่ 1", font=("",10))
buyNumber_text1.place(x=15,y=60)

buyNumber_text2 = Label(text="ตัวที่ 2", font=("",10))
buyNumber_text2.place(x=15,y=120)

buyNumber_text3 = Label(text="ตัวที่ 3", font=("",10))
buyNumber_text3.place(x=15,y=180)

buyNumber_text4 = Label(text="ตัวที่ 4", font=("",10))
buyNumber_text4.place(x=15,y=240)

buyNumber_text5 = Label(text="ตัวที่ 5", font=("",10))
buyNumber_text5.place(x=15,y=300)

# Add a button, named 'Get ID', and add this command: 'show_output'.
# Set the button size as
spin_button = tkinter.Button(text='Spin',
    command=show_output, width=15, height=2
)
# Place the button on the screen
spin_button.place(x=200,y=50)

# Add a check ID button
check_button = tkinter.Button(master=window, text='Check',
    command=checkNumber, width=15, height=2
)
# Place the button on the screen
check_button.place(x=200,y=100)

# Add Readme button
readme_button = tkinter.Button(master=window, text='Read Me',
    command=openReadMe, width=15, height=2
)
# Place the button on the screen
readme_button.place(x=200,y=150)

# Show the output on the screen with 20 px space vertically
output_label = tkinter.Label(master=window)
output_label.place(x=200,y=250)

# Show the app window
window.mainloop()

# Design a message box to show after the user click the Save ID button
saveInfoBox = Tk()
saveInfoBox.geometry("300x200")
saveInfoBox.mainloop()

# Prevent the console window from opening, by saving this file as IDGen.pyw instead of .py