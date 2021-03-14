import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "casing"))

class Test_casing(unittest.TestCase):
    def setUp(self):
        self.var_list = ["some", "incredible", "variable"]

    def test_import(self):
        import casing
        
    def test_cases(self):
        import casing
        
    def test_analyze(self):
        import casing
        for fct in casing.getcases():
            var = getattr(casing, fct)(self.var_list) 
            ana_var = casing.analyze(var)
            self.assertTrue(self.var_list == ana_var or "attached" in fct)
    
    def test_detect(self):
        import casing
        for fct in casing.getcases():
            var = getattr(casing, fct)(self.var_list) 
            function = "{0}case".format(casing.detect(var))
            self.assertTrue(function == fct or "attached" in fct)
    
    def test_invalid(self):
        import casing
        
        with self.assertRaises(Exception):
            casing.transform(self.var_list, "unknow")
    
# if __name__ == "__main__":
    # unittest.main()