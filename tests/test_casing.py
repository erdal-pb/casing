import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "source"))

class Test_casing(unittest.TestCase):

    def test_import(self):
        import casing
        
    def test_cases(self):
        import casing
        
    def test_analyze(self):
        import casing
        var_list = ["some", "incredible", "variable"]
        for fct in casing.get_cases():
            var = getattr(casing, fct)(var_list) 
            ana_var = casing.analyze(var)
            self.assertTrue(var_list == ana_var or "attached" in fct)
    
    def test_detect(self):
        import casing
        var_list = ["some", "incredible", "variable"]
        for fct in casing.get_cases():
            var = getattr(casing, fct)(var_list) 
            function = "{0}case".format(casing.detect(var))
            print("function: " + str(function))
            print("fct: " + str(fct))
            self.assertTrue(function == fct or "attached" in fct)
    
if __name__ == "__main__":
    unittest.main()