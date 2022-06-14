import unittest
from main import combineData


class MyTestCase(unittest.TestCase):
    def test_combineData(self):
        inputZipFilePath = 'C://Users//LENOVO//Desktop//filehandling//unit_test//test.zip'
        result = combineData(inputZipFilePath)
        self.assertTrue(type(result) == str)  # add assertion here


if __name__ == '__main__':
    unittest.main()
