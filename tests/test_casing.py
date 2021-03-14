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
            if "attached" in fct:
                continue
            var = getattr(casing, fct)(self.var_list) 
            function = "{0}case".format(casing.detect(var))
            self.assertTrue(function == fct)
    
    def test_transform_list(self):
        import casing
        casing.transform(self.var_list)
    
    def test_invalid_transform(self):
        import casing
        with self.assertRaises(Exception):
            casing.transform(self.var_list, "unknow")
    
    def test_invalid_transform_type(self):
        import casing        
        with self.assertRaises(Exception):
            casing.transform(0, "unknow")
        
    
    def test_invalid_detect(self):
        import casing
        self.assertTrue(casing.detect("some-Incredible_variable") == "unknow")
        
    
    
    
# if __name__ == "__main__":
    # unittest.main()