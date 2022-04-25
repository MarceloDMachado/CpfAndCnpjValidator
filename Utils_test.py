import unittest
import Utils
import array as arr

class testCnpjUtil(unittest.TestCase):
    def test_hasOnlyNumericChars(self):
        #Invalid scenario
        self.assertFalse(Utils.hasOnlyNumericChars('123456abcdef'))
        
        #Valid scenario
        self.assertTrue(Utils.hasOnlyNumericChars('1234567890'))

    def test_isCnpjComplete(self):
        #invalid scenario
        self.assertFalse(Utils.isCnpjComplete('1234567890123'))

        #Valid scenario
        self.assertTrue(Utils.isCnpjComplete('12345678901234'))
        
    def test_isCpfComplete(self):
        #invalid scenario
        self.assertFalse(Utils.isCpfComplete('1234567890'))
        
        #valid scenario
        self.assertTrue(Utils.isCpfComplete('12345678901'))
        
    def test_getModResult(self):
        #Only valid scenario
        self.assertTrue(Utils.getModResult(123) == 2)
    
    def test_sumAlgarisms(self):
        #Only valid scenario
        self.assertTrue(Utils.sumAlgarisms(arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])) == 45)
    
    def test_multiplyAlgarisms(self):
        #valid scenario
        primaryFactors = arr.array("i", [2, 3, 4])
        secondaryFactors = arr.array("i", [5, 5, 5])
        
        products = Utils.multiplyAlgarisms(primaryFactors, secondaryFactors)
        
        self.assertTrue(products[0] == 10)
        self.assertTrue(products[1] == 15)
        self.assertTrue(products[2] == 20)
        
        #check return type
        self.assertTrue(type(products) == arr.array)
        
    def test_transmuteStringToArray(self):
        #valid scenario
        testStringValue = str('123456')
        transmutResult = Utils.transmuteStringToArray(testStringValue)
        
        self.assertTrue(len(transmutResult) == len(testStringValue))
        
        #check type
        self.assertTrue(type(transmutResult) == arr.array)
    
    def test_addAlgarismAtArrayStart(self):
        #valid scenario
        originalArray = arr.array("i", [1, 2, 3, 4])
        
        newArray = Utils.addAlgarismAtArrayStart(0, originalArray)
        
        #check first element on new array
        self.assertTrue(newArray[0] == 0)
        
        #check if the original array keep imutable
        self.assertTrue(len(newArray) == len(originalArray) + 1)
        self.assertTrue(originalArray[0] == 1)
        
    def test_validateFirstDigit(self):
        #valid scenario        
        self.assertTrue(Utils.validateFirstCnpjDigit('50567038000119'))
        
        #invalid scenario
        self.assertFalse(Utils.validateFirstCnpjDigit('12345678901244'))
    
    def test_validateSecondDigit(self):
        #valid scenario
        self.assertTrue(Utils.validateSecondCnpjDigit('50567038000119'))
        
        #invalid scenario
        self.assertFalse(Utils.validateSecondCnpjDigit('12345678901244'))
    
    def test_isThisCnpjValid(self):
        #valid Scenario
        self.assertTrue(Utils.isThisCnpjValid('50567038000119'))
        
        #invalid scenario
        self.assertFalse(Utils.isThisCnpjValid('12345678901244'))
        
    def test_validateFirstCpfDigit(self):
        #invalid scenario
        self.assertFalse(Utils.validateFirstCpfDigit('44862720814'))
        
        #vaid scenario
        self.assertTrue(Utils.validateFirstCpfDigit('44862720803'))
    
    def test_validateSecondCpfDigit(self):
        #invalid scenario
        self.assertFalse(Utils.validateSecondCpfDigit('44862720814'))
        
        #valid scenario
        self.assertTrue(Utils.validateSecondCpfDigit('44862720803'))
        
    def test_isThisCpfValid(self):
        #invalid scenario
        self.assertFalse(Utils.isThisCpfValid('44862720814'))
        
        #valid scenario
        self.assertTrue(Utils.isThisCpfValid('44862720803'))
        
if __name__ == '__main__':
    unittest.main()