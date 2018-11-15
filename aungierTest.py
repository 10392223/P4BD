"Testing module for aungierRental.py"

#import unittest module
import unittest 
#import all classes we used
from aungierRental import  Car, DieselCar, ElectricCar, HybridCar, PetrolCar, AungierRental

#test class, inherits from unittest module
class TestAungierCar(unittest.TestCase):

    #set up instances for use in testing
    def setUp(self):
        self.car = Car()
        self.diesel = DieselCar()
        self.electric = ElectricCar()
        self.hybrid = HybridCar()
        self.petrol = PetrolCar()
        self.aungier = AungierRental()
    
    #tests colour getters/setters
    def testCarColour(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getColour())
        #set colour
        self.car.setColour('Red')
        self.assertEqual('Red',self.car.getColour())
   
    #tests make getters/setters     
    def testCarMake(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getMake())
        #set colour
        self.car.setMake('Ford')
        self.assertEqual('Ford',self.car.getMake())
    
    #tests model getters/setters
    def testCarModel(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getModel())
        #set colour
        self.car.setModel('Fiesta')
        self.assertEqual('Fiesta',self.car.getModel())
    
    #tests reg getters/setters
    def testCarReg(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getReg())
        #set colour
        self.car.setReg('18D001')
        self.assertEqual('18D001',self.car.getReg())    
    
    #tests diesel engine size getters/setters
    def testDieselEngSize(self):
        #fn to test DieselCar setter
        self.assertEqual('',self.diesel.getDiesEngineSize())
        #set colour
        self.diesel.setDiesEngineSize('1000cc')
        self.assertEqual('1000cc',self.diesel.getDiesEngineSize()) 
    
    #tests electric fuel cells getters/setters
    def testElecCells(self):
        #testing electric car fuel cells setter
        #check init value
        self.assertEqual(0,self.electric.getElecNumberFuelCells())
        #set and test #cells
        self.electric.setElecNumberFuelCells(2)
        self.assertEqual(2,self.electric.getElecNumberFuelCells()) 
 
    #tests hybrid fuel cells getters/setters
    def testHybridCells(self):
        #testing hybrid car fuel cells setter
        #check init value
        self.assertEqual(0,self.hybrid.getHybNumberFuelCells())
        #set and test #cells
        self.hybrid.setHybNumberFuelCells(2)
        self.assertEqual(2,self.hybrid.getHybNumberFuelCells())    
    
    #tests petrol engine size getters/setters    
    def testPetrolEngSize(self):
        #fn to test PetrolCar setter
        #check init value
        self.assertEqual('',self.petrol.getPetrolEngineSize())
        #set engine size and test
        self.petrol.setPetrolEngineSize('1000cc')
        self.assertEqual('1000cc',self.petrol.getPetrolEngineSize())
    
    
    def testRepr(self):
        #test repr fn, this allows me to see if instances are created from csv properly
        
        #use setters to set up generic car attributes
        self.car.setColour('red')
        self.car.setMake('Ford')
        self.car.setModel('Fiesta')
        self.car.setReg('18D00001')
        
        #test returns correctly
        self.assertEqual('(colour=red, make=Ford, model=Fiesta, reg=18D00001)', self.car.__repr__())
        
        #I didn't bother due to time constraints working out a test for all appends perfectly, but the below code will generate each of the instances and show you the data from the csv
#                               import gc
#                               for obj in gc.get_objects():
    #                                if isinstance(obj, DieselCar):
    #                                       print(obj)
    #                                   elif isinstance(obj, ElectricCar):
    #                                    print(obj)
    #                                elif isinstance(obj, HybridCar):
    #                                    print(obj)
    #                                elif isinstance(obj, PetrolCar):
    #                                    print(obj))
        
    def testDieselCarList(self):
        #function to test does the initial append in aungierRental() work for storing diesel cars
        
        self.assertEqual(8, len(self.aungier.getDieselCars()))
        
    def testElectricCarList(self):
        #function to test does the initial append in aungierRental() work for storing electric cars
        
        self.assertEqual(4, len(self.aungier.getElectricCars()))
    
    def testHybridCarList(self):
        #function to test does the initial append in aungierRental() work for storing hyrbid cars
        
        self.assertEqual(8, len(self.aungier.getHybridCars()))
        
    def testPetrolCarList(self):
        #function to test does the initial append in aungierRental() work for storing petrol cars
        
        self.assertEqual(20, len(self.aungier.getPetrolCars()))
        
    def testRentCar(self):
       #test if renting car removes a car from stock
       #check stock is 8 for deisel at beginning
       self.assertEqual(8, len(self.aungier.getDieselCars()))
       #rent diesel car
       self.aungier.rent('D')
       #confirm stock is now 7
       self.assertEqual(7, len(self.aungier.getDieselCars()))
        
           
       
    def testReturnCar(self):
        #test if return car function works
        #will need to enter a valid reg here to get to work (enter 18D001), not sure if there's a way around this
        #rent diesel car
        self.aungier.rent('D')
           
           #confirm stock is now 7
        self.assertEqual(7, len(self.aungier.getDieselCars()))
           #return diesel car
        self.aungier.returnCar('D')
           #confirm stock is now 8 again
        self.assertEqual(8, len(self.aungier.getDieselCars()))
       

if __name__ == '__main__':    
    unittest.main() 