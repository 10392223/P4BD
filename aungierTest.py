import unittest 
from aungierRental import  Car, DieselCar, ElectricCar, HybridCar, PetrolCar, AungierRental


class TestAungierCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.diesel = DieselCar()
        self.electric = ElectricCar()
        self.hybrid = HybridCar()
        self.petrol = PetrolCar()
        self.aungier = AungierRental()
        
    def testCarColour(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getColour())
        #set colour
        self.car.setColour('Red')
        self.assertEqual('Red',self.car.getColour())
        
    def testCarMake(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getMake())
        #set colour
        self.car.setMake('Ford')
        self.assertEqual('Ford',self.car.getMake())
        
    def testCarModel(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getModel())
        #set colour
        self.car.setModel('Fiesta')
        self.assertEqual('Fiesta',self.car.getModel())
    
    def testCarReg(self):
        #test that colour is blank when init runs
        self.assertEqual('',self.car.getReg())
        #set colour
        self.car.setReg('18-D-00001')
        self.assertEqual('18-D-00001',self.car.getReg())    
    
    def testDieselEngSize(self):
        #fn to test DieselCar setter
        self.assertEqual('',self.diesel.getEngineSize())
        #set colour
        self.diesel.setEngineSize('1000cc')
        self.assertEqual('1000cc',self.diesel.getEngineSize()) 
        
    def testElecCells(self):
        #testing electric car fuel cells setter
        #check init value
        self.assertEqual(0,self.electric.getNumberFuelCells())
        #set and test #cells
        self.electric.setNumberFuelCells(2)
        self.assertEqual(2,self.electric.getNumberFuelCells()) 
 
    def testHybridCells(self):
        #testing hybrid car fuel cells setter
        #check init value
        self.assertEqual(0,self.hybrid.getNumberFuelCells())
        #set and test #cells
        self.hybrid.setNumberFuelCells(2)
        self.assertEqual(2,self.hybrid.getNumberFuelCells())    
        
    def testPetrolEngSize(self):
        #fn to test PetrolCar setter
        #check init value
        self.assertEqual('',self.petrol.getEngineSize())
        #set engine size and test
        self.petrol.setEngineSize('1000cc')
        self.assertEqual('1000cc',self.petrol.getEngineSize())
    
    
    def testRepr(self):
        #test function for repr fn
        self.car.setColour('red')
        self.car.setMake('Ford')
        self.car.setModel('Fiesta')
        self.car.setReg('18D00001')
        
        self.assertEqual('(colour=red, make=Ford, model=Fiesta, reg=18D00001)', self.car.__repr__())
        
        #I didn't bother working out a test for all appends perfectly, but the below code will generate each of the instances and show you the data from the csv
#                               #import gc
                                #for obj in gc.get_objects():
#                                   if isinstance(obj, DieselCar):
#                                       print(obj)
#                                   elif isinstance(obj, ElectricCar):
    #                                    print(obj)
    #                                elif isinstance(obj, HybridCar):
    #                                    print(obj)
    #                                elif isinstance(obj, PetrolCar):
    #                                    print(obj))
        
    def testDieselCarList(self):
        #function to test does init append work for storing diesel cars
        
        self.assertEqual(8, len(self.aungier.getDieselCars()))
        
    def testElectricCarList(self):
        #function to test does init append work for storing electric cars
        
        self.assertEqual(4, len(self.aungier.getElectricCars()))
    
    def testHybridCarList(self):
        #function to test does init append work for storing hyrbid cars
        
        self.assertEqual(8, len(self.aungier.getHybridCars()))
        
    def testPetrolCarList(self):
        #function to test does init append work for storing petrol cars
        
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
        #will need to enter a valid reg here to get to work
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