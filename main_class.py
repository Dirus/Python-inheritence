#define your own Vehicle class here
#the order of the four required positional arguments should be: make,model,year,mileage
#please use the conventional way to define function names and refer to the following test to adjust function names 
#no need to handle exceptions here

class Vehicle:
    
    #type in your code
    def __init__(self,make,model,year,mileage):
        self._Vehicle__make = make
        self._Vehicle__model = model
        self._Vehicle__year = year
        self._Vehicle__mileage = mileage

    def __str__(self):
        return "Make: {0}; Model: {1};Year of Manufacture: {2};Mileage: {3}".format(self._Vehicle__make,self._Vehicle__model,self._Vehicle__year,self._Vehicle__mileage)

    def get_mileage(self):
        return self._Vehicle__mileage
    def set_year(self,year):
        self._Vehicle__year = year
    def get_year(self):
        return self._Vehicle__year
    def get_make(self):
        return self._Vehicle__make
    def get_model(self):
        return self._Vehicle__model
    
#do a quick test on the Vehicle class before moving forward (5 points)
#don't change this code
# vehicle1=Vehicle("Honda","Civic",2014,50000)
# print(vehicle1)
# vehicle1.set_year(2012)
# print("The year of manufacture of this vehicle is:", vehicle1.get_year())

# print("The mileage of this vehicle is:", vehicle1.get_mileage())

#define your own Employee class here
#the order of the three required positional arguments should be: name,address,vehicle object
#please use the conventional way to define function names and refer to the following test to adjust function names
#use emp for short of employee in naming attributes and functions
#no need to handle exceptions here

class Employee:

    #type in your code
    def __init__(self, name, address, vehicle):
        self._Employee__emp_name = name
        self._Employee__emp_addr = address
        self._Employee__vehicle = vehicle
    
    def get_emp_name(self):
        return self._Employee__emp_name

    def get_emp_addr(self):
        return self._Employee__emp_addr

    def get_vehicle(self):
        return self._Employee__vehicle
    def __str__(self):
        return "\nEmployee Name: {0}; Employee Address: {1}\nMake: {2}; Model: {3}; Year of Manufacture: {4}; Mileage: {5}".format(self._Employee__emp_name,self._Employee__emp_addr,self._Employee__vehicle.get_make(),self._Employee__vehicle.get_model(),self._Employee__vehicle.get_year(),self._Employee__vehicle.get_mileage())

    def set_emp_addr(self,address):
        self._Employee__emp_addr = address
    

#do a quick test on the Employee class before moving forward (5 points)
#don't change this code
# emp1=Employee("Amy", "100 W Campbell Road, Richardson, Texas, 75080",vehicle1)
# print(emp1)
# print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))
# print("{0} owns a {1} {2} vehicle.".format(emp1.get_emp_name(),emp1.get_vehicle().get_make(),emp1.get_vehicle().get_model()))
# emp1.set_emp_addr("800 E Campbell Road, Richardson, Texas, 75080")
# print("{0} lives at {1}.".format(emp1.get_emp_name(),emp1.get_emp_addr()))

#define your own Full Time Employee class here
#Full Time Employee class inherits from Employee class
#the order of the four required positional arguments should be: name,address,vehicle object,salary
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class FullTimeEmployee(Employee):

    #type in your code
    def __init__(self, name, address, vehicle, salary):
        self._FullTimeEmployee__salary = salary

        # invoking the constructor of parent class
        Employee.__init__(self,name,address,vehicle)
    
    def get_salary(self):
        return self._FullTimeEmployee__salary

    def set_salary(self,salary):
        self._FullTimeEmployee__salary = salary

    def compute_compensation(self):
        if self._FullTimeEmployee__salary <= 45000:
            tax = (18/100)*self._FullTimeEmployee__salary
        elif self._FullTimeEmployee__salary > 45000 and self._FullTimeEmployee__salary <=82000:
            tax = (18/100)*45000+(28/100)*(self._FullTimeEmployee__salary-45000)
        elif self._FullTimeEmployee__salary > 82000:
             tax = (18/100)*45000+(28/100)*(82000-45000)+(33/100)*(self._FullTimeEmployee__salary-82000)
        return (self._FullTimeEmployee__salary - tax)/52

    def __str__(self):
        return "\nDetails of this Full Time Employee are:\nEmployee Name: {0}; Employee Address: {1}\nMake: {2}; Model: {3}; Year of Manufacture: {4}; Mileage: {5}\nSalary: {6}".format(self._Employee__emp_name,self._Employee__emp_addr,self._Employee__vehicle.get_make(),self._Employee__vehicle.get_model(),self._Employee__vehicle.get_year(),self._Employee__vehicle.get_mileage(),self._FullTimeEmployee__salary)

    def compute_reimbursement(self,annual_expense):
        if annual_expense <= 10000:
            return annual_expense/52
        else:
            return (10000+0.5*(annual_expense-10000))/52
    

#do a quick test on the Full Time Employee class before moving forward (5 points)
#don't change this code
# emp2=FullTimeEmployee("Amy", "100 W Campbell Road, Richardson, Texas, 75080", vehicle1, 40000)
# print(emp2)
# print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))
# print("{0} has a weekly compensation of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_compensation()))
# print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp2.get_emp_name(),emp2.compute_reimbursement(12000)))
# emp2.set_salary(50000)
# print("{0} has an annual salary of ${1}.".format(emp2.get_emp_name(),emp2.get_salary()))

#define your own Hourly Employee class here
#Hourly Employee class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,hourly rate
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class HourlyEmployee(Employee):

    #type in your code
    def __init__(self,name,address,vehicle,hours_worked,hourly_rate):
        self._HourlyEmployee__hours_worked = hours_worked
        self._HourlyEmployee__hourly_rate = hourly_rate

        # invoking the constructor of parent class
        Employee.__init__(self,name,address,vehicle)

    def get_hours_worked(self):
        return self._HourlyEmployee__hours_worked

    def get_hourly_rate(self):
        return self._HourlyEmployee__hourly_rate

    def set_hourly_rate(self,hourly_rate):
        self._HourlyEmployee__hourly_rate = hourly_rate

    def __str__(self):
        return "\nDetails of this Hourly Employee are:\nEmployee Name: {0}; Employee Address: {1}\nMake: {2}; Model: {3}; Year of Manufacture: {4}; Mileage: {5}\nHours Worked: {6}; Hourly Rate: {7} ".format(self._Employee__emp_name,self._Employee__emp_addr,self._Employee__vehicle.get_make(),self._Employee__vehicle.get_model(),self._Employee__vehicle.get_year(),self._Employee__vehicle.get_mileage(),self._HourlyEmployee__hours_worked,self._HourlyEmployee__hourly_rate)

    def compute_compensation(self):
        if self._HourlyEmployee__hours_worked > 40:
            return self._HourlyEmployee__hours_worked*self._HourlyEmployee__hourly_rate + (self._HourlyEmployee__hours_worked-40)*1.8*self._HourlyEmployee__hourly_rate
        else:
            return self._HourlyEmployee__hours_worked*self._HourlyEmployee__hourly_rate

    def compute_reimbursement(self,weekly_expense):
        return weekly_expense if weekly_expense< 100 else 100


#do a quick test on the Hourly Employee class before moving forward (5 points)
#don't change this code
# emp3=HourlyEmployee("Grace", "400 W Campbell Road, Richardson, Texas, 75080", vehicle1,50,20)
# print(emp3)
# print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))
# print("{0} has a weekly compensation of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_compensation()))
# print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp3.get_emp_name(),emp3.compute_reimbursement(120)))
# emp3.set_hourly_rate(22)
# print("{0} works {1} hours per week at an hourly rate of ${2}.".format(emp3.get_emp_name(),emp3.get_hours_worked(),emp3.get_hourly_rate()))

#define your own Consultant class here
#Consultant class inherits from Employee class
#the order of the five required positional arguments should be: name,address,vehicle object,hours worked,project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class Consultant(Employee):

    #type in your code
    def __init__(self,name,address,vehicle,hours_worked,project_type):
        self._Consultant__hours_worked = hours_worked
        self._Consultant__project_type = project_type

        # invoking the constructor of parent class
        Employee.__init__(self,name,address,vehicle)

    def get_hours_worked(self):
        return self._Consultant__hours_worked

    def get_project_type(self):
        return self._Consultant__project_type

    def set_hours_worked(self,hours_worked):
        self._Consultant__hours_worked = hours_worked

    def __str__(self):
        return "\nDetails of this Consultant are:\nEmployee Name: {0}; Employee Address: {1}\nMake: {2}; Model: {3}; Year of Manufacture: {4}; Mileage: {5}\nHours Worked: {6}; Project Type: {7} ".format(self._Employee__emp_name,self._Employee__emp_addr,self._Employee__vehicle.get_make(),self._Employee__vehicle.get_model(),self._Employee__vehicle.get_year(),self._Employee__vehicle.get_mileage(),self._Consultant__hours_worked,self._Consultant__project_type)
    
    def compute_compensation(self):
        if self._Consultant__project_type == 1:
            hourly_rate = 55
        elif self._Consultant__project_type == 2:
            hourly_rate = 70
        elif self._Consultant__project_type == 3:
            hourly_rate = 85
        return hourly_rate*self._Consultant__hours_worked

    def compute_reimbursement(self,weekly_expense):
        if self._Consultant__project_type == 1:
            return weekly_expense
        elif self._Consultant__project_type == 2:
            return 0.9*weekly_expense
        elif self._Consultant__project_type == 3:
            return 0.8*weekly_expense

#do a quick test on the Consultant class before moving forward (5 points)
#don't change this code
# emp4=Consultant("Michael", "700 W Campbell Road, Richardson, Texas, 75080",vehicle1,40,2)
# print(emp4)
# print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))
# print("{0} has a weekly compensation of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_compensation()))
# print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp4.get_emp_name(),emp4.compute_reimbursement(300)))
# emp4.set_hours_worked(35)
# print("{0} works {1} hours per week for type {2} project.".format(emp4.get_emp_name(),emp4.get_hours_worked(),emp4.get_project_type()))

#define your own Management class here
#Management class inherits from both Full Time Employee class and Consultant class
#the order of the six required positional arguments should be: name, address,vehicle object, salary, hours worked, project type
#please use the conventional way to define function names and refer to the following test to adjust function names
#see detailed requirements on compute_compensation() function and compute_reimbursement() function in the pdf file
#no need to handle exceptions here

class Management(FullTimeEmployee,Consultant):

    #type in your code
    def __init__(self, name, address, vehicle, salary, hours_worked, project_type):
        FullTimeEmployee.__init__(self,name, address, vehicle, salary)
        Consultant.__init__(self,name,address,vehicle,hours_worked,project_type)

    def compute_compensation(self):
        return FullTimeEmployee.compute_compensation(self) + Consultant.compute_compensation(self)

    def compute_reimbursement(self, annual_expense, weekly_expense=0):
        return FullTimeEmployee.compute_reimbursement(self, annual_expense) + Consultant.compute_reimbursement(self, weekly_expense)

    def __str__(self):
        return "\nDetails of this Management are:\nEmployee Name: {0}; Employee Address: {1}\nMake: {2}; Model: {3}; Year of Manufacture: {4}; Mileage: {6}\nSalary: {5}; Hours Worked: {7}; Project Type: {8} ".format(self._Employee__emp_name,self._Employee__emp_addr,self._Employee__vehicle.get_make(),self._Employee__vehicle.get_model(),self._Employee__vehicle.get_year(),self._Employee__vehicle.get_mileage(),self._FullTimeEmployee__salary,self._Consultant__hours_worked,self._Consultant__project_type)

#do a quick test on the Management class before moving forward (5 points)
#don't change this code
# emp5=Management("Jane", "1000 W Campbell Road, Richardson, Texas, 75080",vehicle1,120000,10,3)
# print(emp5)
# print("\n")
# print("{0} has an annual salary of ${1}.".format(emp5.get_emp_name(),emp5.get_salary()))
# print("{0} works {1} hours per week for type {2} project.".format(emp5.get_emp_name(),emp5.get_hours_worked(),emp5.get_project_type()))
# print("{0} has a weekly compensation of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_compensation()))
# print("{0} has a weekly reimbursement of ${1:0.2f}.".format(emp5.get_emp_name(),emp5.compute_reimbursement(8000,300)))

#complete this get_emp_input() function to prepare for the main menu application
#this function is used to ask for basic employee information and then return them: name and address
#this function doesn't take arguement(s)
#no need to handle exceptions here
def get_emp_input():
    #type in your code
    name = input("Enter the employee's name: ")
    address = input("Enter the employee's address: ")
    return name,address

#do a quick test on the get_emp_input() function before moving forward
#don't change this code and please use the example input
#example input: Bob; 350 E Campbell Road, Richardson, Texas, 75080
# name, address=get_emp_input()
# print("{0} lives at {1}.".format(name,address))


#complete this get_vehicle_input() function to prepare for the main menu application
#this function is used to ask for vehicle information and then return them: make,model,year,mileage
#this function doesn't take arguement(s)
#no need to handle exceptions of make input and model input
#handle exceptions to make sure year is a 4-digit positive number between 1900 and 2020
#handle exceptions to make sure mileage is a positive number
def get_vehicle_input():
    veh_make = input('Enter the vehicle make: ')
    veh_model = input('Enter the vehicle model: ')

    #type in your code
    veh_year = int(input("Enter the year of manufacture (yyyy): "))
    while (veh_year < 1900 or veh_year > 2020):
        print("Please enter an integer value for year in the format of yyyy between 1900 and 2020.")
        veh_year = int(input("Enter the year of manufacture (yyyy): "))

    veh_mileage = int(input("Enter the mileage: "))
    while veh_mileage < 0:
        print("Please enter a positive value for mileage.")
        veh_mileage = int(input("Enter the mileage: "))

    return (veh_make, veh_model, veh_year, veh_mileage)

    #do a quick test on the get_vehicle_input() function before moving forward (5 points)
#don't change this code and please use the example input
#example input:Ford; Ranger; 2021 (when asked to enter again enter 2011); 80000
# vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()  
# print("The vehicle entered is a {0} {1} made in {2} with {3} mileage curently.".format(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage))

#complete this get_full_time_input() function to prepare for the main menu application
#this function is used to ask for specific information of full time employees and then return it: annual salary
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_full_time_input():
    #type in your code
    return  int(input("Enter the annual salary: "))

# salary=get_full_time_input()
# print("The annual salary entered is {0:0.2f}".format(salary))

#complete this get_hourly_input() function to prepare for the main menu application
#this function is used to ask for specific information of hourly employees and then return them: hours worked, hourly rate
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_hourly_input():
    #type in your code
    hours_worked = int(input("Enter the hours worked: "))
    hourly_rate = int(input("Enter the hourly rate: "))
    return hours_worked, hourly_rate

# hours_worked, hourly_rate = get_hourly_input()
# print("This hourly employee works {0} hours per week at an hourly rate of ${1:0.2f}".format(hours_worked,hourly_rate))

#complete this get_consultant_input() function to prepare for the main menu application
#this function is used to ask for specific information of consultants and then return them: hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_consultant_input():
    #type in your code
    hours_worked = int(input("Enter the hours worked: "))
    project_type = int(input("Project Type? (Enter a number between 1 and 3): "))
    return hours_worked, project_type

# hours_worked, project_type = get_consultant_input()
# print("This consultant works {0} hours per week for type {1} project.".format(hours_worked,project_type))

#complete this get_management_input() function to prepare for the main menu application
#this function is used to ask for specific information of managements and then return them: annual salary, hours worked, project type
#this function doesn't take arguement(s)
#no need to handle exceptions
def get_management_input():
    #type in your code
    annual_salary = int(input("Enter the annual salary: "))
    hours_worked = int(input("Enter the hours worked: "))
    project_type = int(input("Project Type? (Enter a number between 1 and 3): "))
    return annual_salary,hours_worked,project_type

# salary, hours_worked, project_type = get_management_input()
# print("This management has an annual salary of ${0:0.2f}. This management also works {1} hours per week additionally for type {2} project.".format(salary, hours_worked,project_type))

#complete this read_file_data() function to prepare for the main menu application
#this function is used to read information from an existing databse/binary file, which is empdata.dat in the final exam
#this function doesn't take argument(s)
#this function returns a list containing all employee objects stored in the database; each employ object is an element in the list; the list will also be used and updated later
#need to handle exceptions if file doesn't exist
import pickle
def read_file_data():
    #type in your code
    infile = open('empdata.dat','rb')
    db = pickle.load(infile)
    infile.close
    return db

emp_list=read_file_data()
print("There are {} employees stored in the database.".format(len(emp_list)))
print("\nBelow is the information of the first employee in the database: {}".format(emp_list[0]))
print("\n{} is the first employee.".format(emp_list[0].get_emp_name()))


#complete option 1 related code here
#the idea is to walk through users to input required information
#the first and foremost step is to ask for emloyee type
#this function doesn't take arguement(s)
#this function prints the entered object and also returns the entered object
#some parts are provided so you don't need to change them (but you still can if you want to)

def run_option1():
    #ask for employee type
    #exceptions need to be handled here to accept valid input 

    sel = input("Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management) : ")
    while sel not in ['1','2','3','4']:
        print("Please select an option from 1, 2, 3, and 4.")
        sel = input("Type of Employee?(1-Full Time;2-Hourly;3-Consultant;4-Management) : ")

    sel = int(sel)

    #call the previous get_emp_input() to ask for employee information and store the values      
    name, address = get_emp_input()

    #call the previous get_vehicle_input() to ask for vehicle information and store the values
    vehiclemake, vehiclemodel, vehicleyear, vehiclemileage = get_vehicle_input()    
    
    #create an object of Vehicle class using the prervious information
    a_vehicle = Vehicle(vehiclemake, vehiclemodel, vehicleyear, vehiclemileage)

    #depending on previous input, call the prervious functions to ask for corresponding information
    #then use all the required information to create an object of a certain class 
    #type 1:annual salary
    #type 2:hours worked,hourly rate
    #type 3:hours worked, project type
    #type 4:annual salary, hours worked, project type
    if sel == 1:
        sal = get_full_time_input()
        an_emp = FullTimeEmployee(name, address, a_vehicle,sal)
    elif sel == 2:
        hw, hr = get_hourly_input()
        an_emp = HourlyEmployee(name, address, a_vehicle, hw, hr)
    elif sel == 3:
        hw, pt = get_consultant_input()
        an_emp = Consultant(name, address, a_vehicle, hw, pt)
    elif sel ==4:
        sal, hw, pt = get_management_input()
        an_emp = Management(name, address, a_vehicle, sal, hw, pt)
    
    print(an_emp)
    # display_emp_info(an_emp)
    
    print("============================================================")        
    print("New employee entered successfully! Now going to the main menu.")
    print("==============================================================")     
    return an_emp    
      
# run_option1()
# emp_list.append(run_option1())
# dbfile = open('empdata.dat','wb')
# pickle.dump(emp_list,dbfile)
# dbfile.close()
#complete option 2 related code here
#the function is to print centain number of employees as required by users
#first choice:print all employees; second choice: print first 5 employees when there are at least 5 employees (print all if fewer than 5)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#needs to handle exceptions when taking user seletions
def run_option2(my_lst):
    #type in your code
    choice = input("Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? ")
    while choice not in ['1','2']:
        print("Please select 1 or 2")
        choice = input("Do you want to see information of all employees (input 1) or the first 5 employees (input 2)? ")

    print("==========================================================================")
    if choice == '1':
        print("Below is the information of all the employees stored in the database.")
        print("==========================================================================")
        for emp in my_lst:
            print(emp)
    else:
        print("Below is the information of the first 5 employees stored in the database.")
        print("==========================================================================")
        for i in range(0,5):
            print(my_lst[i])


# run_option2(emp_list)

#complete option 3 related code here
#the function is used to print compensations of all Employees
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions
def run_option3(my_lst):
    print("\nEmployee name and Compensation of all Employees")
    print("=================================================")
    
    #type in your code 
    for emp in my_lst:
        print("{0}'s weekly compensation is ${1}".format(emp.get_emp_name(),emp.compute_compensation()))

# run_option3(emp_list)

#complete option 4 related code here
#the function is used to search for an employee by name and the searching is NOT case sensitive
#if there are some matching cases, print the information of all matched employees
#if no matchng cases, print "There is no employee matching the name you entered."
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function also returns a list of objects of the matched employees
#no need to handle exceptions
def run_option4(my_lst):
    #type in your code
    name = input("Please enter the name of the employee you want to search: ")
    matched_emp_list = []
    for emp in my_lst:
        if emp.get_emp_name().lower() == name.lower():
            if len(matched_emp_list) == 0:
                print("==========================================================================")
                print("Below is the information of all employees that match the name you entered.")
                print("==========================================================================")
            print(emp)
            matched_emp_list.append(emp)
    if len(matched_emp_list) == 0:
        print("There is no employee matching the name you entered.")
    return matched_emp_list

# matched_emp_list=run_option4(emp_list)
# print("\nThere are {} employees matching your search.".format(len(matched_emp_list)))

#complete option 5 related code here
#the function is used to show some basic statistics. They are: 
#(1) the number of employees stored in the database
#(2) the highest weekly compensation
#(3) the mean weekly compensation
#(4) the number of employees who have a vehicle with over 100,000 mileage
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

def run_option5(my_lst):
    #type in your code
    print("========================================================\nBelow is the statistics of all employees in this database.\n========================================================")
    print("There are {} employees stored in this employee database.".format(len(my_lst)))
    highest_weekly_compensation, sum_compensation,count = 0,0,0
    for emp in my_lst:
        if emp.compute_compensation() > highest_weekly_compensation:
            highest_weekly_compensation = emp.compute_compensation()
        sum_compensation = sum_compensation+emp.compute_compensation()
        if emp.get_vehicle().get_mileage() > 100000:
            count = count+1
    print("The highest weekly compensation is $",highest_weekly_compensation)
    print("The mean weekly compensation is:$",sum_compensation/len(my_lst))
    print("The number of employees who have a vehicle with over 100,000 mileage is",count)

# run_option5(emp_list)

#complete option 6 related code here
#the function is used to compute weekly reimbursement (assuming the user has the requirerd information)
#the first step is to ask for the name of the employee (you can call run_option4() here)
#the second step is to select one employee from the matched employees
#the third step is to ask for required information 
#this function doesn't return anything
#no need to handle exceptions
def run_option6(emp_list):
    matched_list=run_option4(emp_list)
    choice=int(input("Which employee do you want to check (enter a number)? "))
    emp=matched_list[choice-1]
    
    #type in your code
    annual_expense = int(input("What is the annual expense? "))
    print("############################################################")
    print("This employee should have a weekly reimbursement of ${}.".format(emp.compute_reimbursement(annual_expense)))

# run_option6(emp_list)

#complete option 7 related code here
#the function is used to store changes into a new file/database (i.e. empdata_updated.dat) and exit the program
#the first step is to double check with the user if he/she does want to exit (not case sensitive)
#this function takes one argument, which is the emp_lst list (i.e. the list created previously which is used to store employee objects)
#this function doesn't return anything
#no need to handle exceptions

import sys
def run_option7(my_lst):
    #type in your code
    print("You chose to exit the program")
    choice = input("Are you sure (Y/N)? ")
    if choice.upper() not in ['Y','N']:
        print("Your input doesn't match any valid option and has been considered as 'N'.\nGoing back to the selection menu")
    elif choice.upper() == 'N':
        print("=================================\nGoing back to the selection menu.\n=================================")
    elif choice.upper() == 'Y':
        dbfile = open('empdata_updated.dat','wb')
        pickle.dump(my_lst,dbfile)
        dbfile.close()
        print("=================================\nProgram successfully being closed\n=================================")
        quit()

# run_option7(emp_list)

#complete the main application
#the application menu provides 7 options
#when user selects a valid option (except for 7), execute that option and come back to the menu again
#need to handle exceptions when taking user's choice
#this function doesn't tale any argument
#it will work on the employ object list which is read from file empdata.dat
def run_menu_options():
    #read employee objects in to a list
    emp_list = read_file_data()
    
    #display 7 options and ask users to select from them and execute the selection
    sel = 1
    while sel <=  7 and sel >= 1:
        #display options
        display_options()
        
        #take selection input
        
        choice = input("Your selection is : ")
        while choice not in ['1','2','3','4','5','6','7']:
            print("=========================================\nYou must enter an integer between 1 and 7!\n=========================================")
            display_options()
            choice = input("Your selection is : ")
        sel = int(choice)

        #execute selection
        if sel == 1:
            emp_list.append(run_option1())
        elif sel == 2:
            run_option2(emp_list)
        elif sel == 3:
            run_option3(emp_list)
        elif sel == 4:
            run_option4(emp_list)
        elif sel == 5:
            run_option5(emp_list)
        elif sel == 6:
            run_option6(emp_list)
        elif sel == 7:  
            run_option7(emp_list)
        else:
            print("Invalid choice!")

def display_options():
    print("\n==== Menu ====")
    print("1. To add an employee")
    print("2. To print the name and address of employees")
    print("3. To print the employee name and compensation of all employees")
    print("4. To search for employees by name")
    print("5. To check the basic statistics of employees")
    print("6. To calculate the reimbursement of one employee")
    print("7. To exit program")

run_menu_options()