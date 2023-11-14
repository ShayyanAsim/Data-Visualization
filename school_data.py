# school_data.py
# SHAYYAN ASIM, UCID:30149567, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays

def import_data():
    '''The purpose of this function is to import the 3 csv files 

    Output:
    This function returns the data in the 3 csv files as 3 seperate lists

    '''
    data_2020_2021 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)#imports the data set from the file schoo_data_2020_2021 as a numpy array.
    data_2019_2020 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)#imports the data set from the file schoo_data_2019_2020 as a numpy array.
    data_2018_2019 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)#imports the data set from the file schoo_data_2018_2019 as a numpy array.
    return data_2020_2021 ,data_2019_2020 ,data_2018_2019 #returns the 3 numpy arrays of each file(data set)


# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")
    data_2020_2021 ,data_2019_2020 ,data_2018_2019 = import_data() #calls out the function which include the 3 numpy arrays
    # Print array data here
    print('Array data for 2020-2021:\n',data_2020_2021)#prints the numpy array for the year 2020-2021
    print('Array data for 2019-2020:\n',data_2019_2020)#prints the numpy array for the year 2019-2020
    print('Array data for 2018-2019:\n',data_2018_2019)#prints the numpy array for the year 2018-2019
   
    # Add request for user input here
    
    School_Name = { 
            'Centennial High School': '1224', 
            'Robert Thirsk School': '1679', 
            'Louise Dean School': '9626', 
            'Queen Elizabeth High School': '9806', 
            'Forest Lawn High School': '9813', 
            'Crescent Heights High School': '9815',
            'Western Canada High SchoolSchool': '9806', 
            'Forest Lawn High School': '9813',
            'Crescent Heights High School': '9815',
            'Western Canada High School': '9816', 
            'Central Memorial High School': '9823', 
            'James Fowler High School': '9825', 
            'Ernest Manning High School': '9826',
            'William Aberhart High School': '9829',
            'National Sport School': '9830',
            'Henry Wise Wood High School': '9836', 
            'Bowness High School': '9847', 
            'Lord Beaverbrook High School': '9850', 
            'Jack James High School': '9856', 
            'Sir Winston Churchill High School': '9857', 
            'Dr. E. P. Scarlett High School': '9858', 
            'John G Diefenbaker High School': '9860', 
            'Lester B. Pearson High School': '9865'} #a dictionary which was hard coded that includes all the school names and school code

    School_name_index = list(School_Name.values())#takes the values that is the school code in the dictionary and creates it list
    input_1 = input("Please enter the high school name or school code:")#user being asked to enter/input the school name or code
    while input_1 not in School_Name.keys() and input_1 not in School_Name.values():#conditional loop checking that is the school name or code in the dictionary.
        print("You must enter a valid school name or code.")#if the user input is not in the dictionary this line is printed that indicates that the userinput is wrong.
        input_1 = input("Please enter the high school name or school code: ")#if the user input is not in the dictionary he/she is asked to give the input again

    
    print("\n***Requested School Statistics***\n")
    if input_1 in School_Name.keys(): #condition checking if the school name is in the dictionary.
        School(input_1,School_Name[input_1]).print_all_stats() #creates an object and print allstats, calls on the class.
        position =School_name_index.index(School_Name[input_1]) #gets the index of the array of whichever row or column item is needed.

    else:
        for key,values in School_Name.items(): #loop checking that is the school name or code in the dictionary
            if input_1 == values: # user input is the school code
                School(key,values).print_all_stats() #calls on the class
                position =School_name_index.index(input_1) #gets the index of the array of whichever row or column item is needed

                break # is used to bring the control out of the loop when some external condition is triggered.
    
    
    
    

    # Print school name and code using the given class
    # Add data processing and plotting here

    #the 3 lines of code below calculates the mean as an integer of each grade using the index value of the school name and code using the data from the csv files.
    grade_10 = int(np.mean([data_2018_2019[position][1],data_2019_2020[position][1],data_2020_2021[position][1]])) 
    grade_11 = int(np.mean([data_2018_2019[position][2],data_2019_2020[position][2],data_2020_2021[position][2]]))
    grade_12 = int(np.mean([data_2018_2019[position][3],data_2019_2020[position][3],data_2020_2021[position][3]]))

    #the 3 lines of code below calculates the sum as an integer of grade 12 using the index value of the school name and code using the data from the csv files.
    sum_grad12 = int(np.sum([data_2018_2019[position][3],data_2019_2020[position][3],data_2020_2021[position][3]]))


    print("Mean enrollment for Grade 10:",grade_10) #print statement for the mean enrollment of grade 10 using the mean that was calculated above.
    print("Mean enrollment for Grade 11: ",grade_11) #print statement for the mean enrollment of grade 11 using the mean that was calculated above.
    print("Mean enrollment for Grade 12: ",grade_12) #print statement for the mean enrollment of grade 10 using the mean that was calculated above.
    print("Total number of students who graduated in the past three years:",sum_grad12) #print statement for the number of people who graduated using the sum of grade 12 that was calculated above.

    Grade_level = [10,11,12] #variable defining the content of the x-axis.
    plt.title("Grade Enrollment by Year") #sets the title of the plot
    plt.xlabel("Grade level") #labels the x-axis of the plot
    plt.ylabel("Total number of students") #labels the y-axis of the plot
    plt.xticks(Grade_level) #updated the ticks on the x-axis, we make our own ticks
    #the 3 lines of code below creates a scatter plot using the school data form the 3 csv files.
    plt.scatter(Grade_level,data_2020_2021[position][1:],c=["b"],label = "2021 Enrollment") #creates a scatter plot for the 2020-2021 data in the color blue
    plt.scatter(Grade_level,data_2019_2020[position][1:],c=["g"],label = "2020 Enrollment") #creates a scatter plot for the 2019-2020 data in the color green
    plt.scatter(Grade_level,data_2018_2019[position][1:],c=["r"],label = "2019 Enrollment") #creates a scatter plot for the 2018-2019 data in the color red

    #creates a legend on the plot for each year that is located on the upper left part of the plot.
    plt.legend(["2021 Enrollment","2020 Enrollment","2019 Enrollment"],loc = "upper left")

    plt.show() #shows the plot when the code is executed








# Do not modify the code below
if __name__ == '__main__':
    main()

