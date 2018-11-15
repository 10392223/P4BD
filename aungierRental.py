"""
Created on Thu Nov 15 14:55:47 2018

@author: Martin

Assignment 2 is based around the Car Dealership example use to demonstrate Object Oriented Programming - (see lecture notes below).

However this assignment is based on a brand new venture called Aungier Car Rental.

Aungier Car Rental will rent cars to their customer. They have the potential to rent either petrol, diesel, electric, or hybrid cars.
They have initially 40 cars in their rental pool made up of 50% petrol, 20% diesel, 10% electric and 20% hybrid.
When a car is not rented it is available to the customer to rent.
Once a car is rented the car is assigned to the customer, and removed from the rental pool.
When the car is returned by the customer it is assigned back into the rental pool.
If all 40 cars are rented out the rental function should return a message to the customer saying "Sorry nothing to rent, please try again"
All classes developed should be documented and accompanied by an associated test suite for the classes written.
The deadline is the 7th Oct 2018 on moodle @ 23:55.
"""
#create class to store generic details about cars
class Car(object):
    
    #init function to set up our generic car variables
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__reg = ''
    
    #setter for colour
    def setColour(self, colour):
        self.__colour = colour

    #getter for colour
    def getColour(self):
        return self.__colour
    
    #setter for make
    def setMake(self, make):
        self.__make = make
        
    #getter for make
    def getMake(self):
        return self.__make

    #setter for model
    def setModel(self, model):
        self.__model = model

    #getter for model
    def getModel(self):
        return self.__model
    
    #setter for reg
    def setReg(self, reg):
        self.__reg = reg
    
    #getter for reg
    def getReg(self):
        return self.__reg
    
    #repr fn allows to test for proper appending of instances of cars later on
    def __repr__(self):
      return '(colour=%s, make=%s, model=%s, reg=%s)' % (self.__colour, self.__make, self.__model, self.__reg)

#Class for attributes specific to diesel car
class DieselCar(Car):
    
    #init engine size
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
    
    #getter for engine size
    def getEngineSize(self):
        return self.__engineSize
    
    #setter for engine size
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

#Class for attributes specific to electric car      
class ElectricCar(Car):
    
    #init for # fuel cells
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 0
    
    #getter for number fuel cells.    
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    #setter for number fuel cells.
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
 
#Class for attributes specific to hybrid car             
class HybridCar(Car):
    
    #init # fuel cells
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 0
        
    #getter for number fuel cells.
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    #setter for number fuel cells.
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells

#Class for attributes specific to petrol car             
class PetrolCar(Car):
    
    #init engine size
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
    
    #getter for engine size    
    def getEngineSize(self):
        return self.__engineSize
    
    #setter for engine size
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize

#class for the aungier rental business module
class AungierRental(object):
        
    #init to set up the four empty lists for the dif types of car
    def __init__(self):
        self.__diesel_cars = []
        self.__electric_cars = []
        self.__hybrid_cars = []
        self.__petrol_cars = []
        
        #import pandas and read in a csv with 40 unique cars in it, this is a 'database' of aungier rentals cars.csv attached in zip
        import pandas as pd
        cars = pd.read_csv("aungier_cars.csv")
        
        #itterate through cells of csv
        for index, row in cars.iterrows():
            #if row is type diesel append an instance of a diesel car based on details in csv
          if row['Type'] == 'D':
            #set identifier as the reg (only unique column)
            reg_it = row['Reg']
            #create an instance of DieselCar()
            reg_it = DieselCar()
            #use setters to create attributes of instance, all taken from csv
            reg_it.setColour(row['Colour'])
            reg_it.setMake(row['Make'])
            reg_it.setModel(row['Model'])
            reg_it.setReg(row['Reg'])
            #this variable specific to diesel car class
            reg_it.setEngineSize(row['EngSize'])
            #append the instance to the list of diesel cars
            self.__diesel_cars.append(reg_it)
           
            #repeat as above but for electric
          elif row['Type'] == 'E':
            
            reg_it = row['Reg']
            
            reg_it = ElectricCar()
            
            reg_it.setColour(row['Colour'])
            reg_it.setMake(row['Make'])
            reg_it.setModel(row['Model'])
            reg_it.setReg(row['Reg'])
            
            reg_it.setNumberFuelCells(row['FuelCells'])
            
            self.__electric_cars.append(reg_it)
            
            #repeat as above but for hybrid
          elif row['Type'] == 'H':
            
            reg_it = row['Reg']
            
            reg_it = HybridCar()
            
            reg_it.setColour(row['Colour'])
            reg_it.setMake(row['Make'])
            reg_it.setModel(row['Model'])
            reg_it.setReg(row['Reg'])
            
            reg_it.setNumberFuelCells(row['FuelCells'])
            
            self.__hybrid_cars.append(reg_it)  
          
            #repeat as above but for petrol
          elif row['Type'] == 'P':
            
            reg_it = row['Reg']
            
            reg_it = PetrolCar()
            
            reg_it.setColour(row['Colour'])
            reg_it.setMake(row['Make'])
            reg_it.setModel(row['Model'])
            reg_it.setReg(row['Reg'])
            
            reg_it.setEngineSize(row['EngSize'])
            
            self.__petrol_cars.append(reg_it)
           
        
    #getter for list of diesel cars    
    def getDieselCars(self):
        return self.__diesel_cars
    
    #getter for list of electric cars
    def getElectricCars(self):
        return self.__electric_cars
    
    #getter for list of hybrid cars
    def getHybridCars(self):
        return self.__hybrid_cars
    
    #getter for list of petrol cars
    def getPetrolCars(self):
        return self.__petrol_cars
    
    #function to print the stock of cars. Returns number by calling the getters for lists and returning their lengths.
    def checkCarsInStock(self):
    
        print('Number of Diesel Cars : ', len(self.getDieselCars()))
        print('Number of Electric Cars : ', len(self.getElectricCars()))
        print('Number of Hybrid Cars : ', len(self.getHybridCars()))
        print('Number of Petrol Cars : ', len(self.getPetrolCars()))
        
     #function for enabling the renting a car function, one input called type   
    def rent(self, type):
    
        #initial check to see if any cars are left, if not, returns error and doesn't allow rental
        if len(self.getDieselCars()) == 0 and len(self.getElectricCars()) == 0 and len(self.getHybridCars()) == 0 and len(self.getPetrolCars())==0:
            print("All cars are rented out, take the bus!")
       
        else:
            #takes in the type the customer wants to rent
            if type == 'D':
                #checks to see if any of the type left.
                if len(self.__diesel_cars) >0:
                    #if there is pop car from the list
                    return self.__diesel_cars.pop()
               #else print no diesel cars left
                else:
                    print('\n' + 'No Diesel cars remaining')
            
            #same as above except for type E
            elif type == 'E':
                if len(self.__electric_cars) >0:
                    return self.__electric_cars.pop()
                else:
                    print('\n' + 'No Electric cars remaining')
            
            #same as above except for type H
            elif type == 'H':
                if len(self.__hybrid_cars) >0:
                    return self.__hybrid_cars.pop()
                else:
                    print('\n' + 'No Hybrid cars remaining')
            
            #same as above except for type P
            elif type == 'P':
                if len(self.__petrol_cars) >0:
                    return self.__petrol_cars.pop()
                else:
                    print('\n' + 'No Petrol cars remaining')
    
    def returnCar(self, type):
    
        if len(self.getDieselCars()) == 8 and len(self.getElectricCars()) == 4 and len(self.getHybridCars()) == 8 and len(self.getPetrolCars())== 20:
            print("All cars are returned, did you rob this one instead?")
            
        import pandas as pd
        cars = pd.read_csv("aungier_cars.csv")
         
        reg_it = input("Please enter the registration of the car: ").upper()
        
        if type == 'D':
            if len(self.__diesel_cars) <8:
              
              for index, row in cars.iterrows():
                if row['Reg'] == reg_it:
              
                              
                    reg_it = DieselCar()
            
                    reg_it.setColour(row['Colour'])
                    reg_it.setMake(row['Make'])
                    reg_it.setModel(row['Model'])
                    reg_it.setReg(row['Reg'])
                    self.__diesel_cars.append(reg_it)
                
            else:
                print('\n' + 'All Diesel cars returned, try again')
                
        elif type == 'E':
            if len(self.__electric_cars) <4:
              
              for index, row in cars.iterrows():
                if row['Reg'] == reg_it:
              
                              
                    reg_it = ElectricCar()
            
                    reg_it.setColour(row['Colour'])
                    reg_it.setMake(row['Make'])
                    reg_it.setModel(row['Model'])
                    reg_it.setReg(row['Reg'])
                    self.__electric_cars.append(reg_it)
            else:
                print('\n' + 'All Electric cars returned, try again')
                
        elif type == 'H':
            if len(self.__hybrid_cars) <8:
              for index, row in cars.iterrows():
                if row['Reg'] == reg_it:
              
                              
                    reg_it = HybridCar()
            
                    reg_it.setColour(row['Colour'])
                    reg_it.setMake(row['Make'])
                    reg_it.setModel(row['Model'])
                    reg_it.setReg(row['Reg'])
                    self.__hybrid_cars.append(reg_it)
            else:
                print('\n' + 'All Hybrid cars returned, try again')
                
        elif type == 'P':
            if len(self.__hybrid_cars) <20:
              for index, row in cars.iterrows():
                if row['Reg'] == reg_it:
              
                              
                    reg_it = PetrolCar()
            
                    reg_it.setColour(row['Colour'])
                    reg_it.setMake(row['Make'])
                    reg_it.setModel(row['Model'])
                    reg_it.setReg(row['Reg'])
                    self.__petrol_cars.append(reg_it)
            else:
                print('\n' + 'All Hybrid cars returned, try again')
                
    def mainMenu(self):
        
        while 1==1:
            
            print("**********************")
            print('Welcome to Aungier Rental')
            print("**********************")
            print('\n' + "What would you like to do?", '\n')
            print("1. Rent a Car." + '\n' + '2. Return a Car.' + '\n' + '3. Quit')
            
            answer = input()
            
            if answer == '3':
                print('\n' + 'Goodbye')
                break
            elif answer !='1' and answer !='2':
                print('Invalid input, try again')
            
            else:
                while 1==1:
                    if answer == '1':
                        print('What car would you like to rent?')
                        type = input('D for Diesel, E for electric, H for Hybrid, P for petrol, M for Main Menu: ')
                        type= type.upper()
                        if type == 'M':
                            break
                        elif type!= 'D' and type!='E' and type!= 'H' and type!= 'P':
                            print("Please try again.")
                        else:
                            self.rent(type)
                            self.checkCarsInStock()
                            break
                    elif answer == '2':
                        print('What car would you like to return?')
                        type = input('D for Diesel, E for electric, H for Hybrid, P for petrol, M for Main Menu: ')
                        type = type.upper()
                        if type == 'M':
                            break
                        elif type!= 'D' and type!='E' and type!= 'H' and type!= 'P':
                            print("Please try again.")
                        else:
                            self.returnCar(type.upper())
                            self.checkCarsInStock()
                            break
       
Martin = AungierRental()


if __name__ == '__main__':
    Martin.mainMenu()
    