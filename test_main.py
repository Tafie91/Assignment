import unittest
import pandas as pd
from main import IdealFunctionFitter

class TestIdealFunctionFitter(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.train_data = pd.DataFrame({'x': [1, 2, 3], 'y': [1.1, 2.2, 3.3]})
        self.ideal_data = pd.DataFrame({
            'x': [1, 2, 3],
            'ideal1': [1.0, 2.0, 3.0],
            'ideal2': [1.2, 2.4, 3.6]
        })
        self.fitter = IdealFunctionFitter(self.train_data, self.ideal_data)

    def test_find_best_fit(self):
        # Test that 'ideal1' is identified as the best fit
        best_fit = self.fitter.find_best_fit()
        self.assertEqual(best_fit[0], 'ideal1')

    def test_map_test_data(self):
        # Sample test data to map
        test_data = pd.DataFrame({'x': [1, 2], 'y': [1.05, 2.15]})
        best_fit_funcs = ['ideal1']
        mapped = self.fitter.map_test_data(test_data, best_fit_funcs)
        # Test if two points were correctly mapped
        self.assertEqual(len(mapped), 2)

if __name__ == '__main__':
    unittest.main()
