import unittest
from manual import ManualCsvConverter


class MyTests(unittest.TestCase):

    def setUp(self):
        self.manual = ManualCsvConverter()

    def test_prepare_title(self):
        self.assertEqual(self.manual.prepare_title({"id,name,birth,salary,department"}),
                         {"id", "name", "birth", "salary", "department"})


    def test_convert_row_to_json(self):
        self.assertEqual(self.manual.convert_row_to_json("1,Ivan,1980,150000,1"), )

        
    def test_to_json(self):
        self.assertEqual(self.manual.to_json("id,name,birth,salary,department"
                                             "1,Ivan,1980,150000,1"
                                             "2,Alex,1960,200000,5"){"id" : "1",
                                                                             "name": "Ivan",
                                                                     "birth" : "1980",
                                                                     "salary" : "150000",
                                                                     "department" : "1"},
                                                                    {"id" : "2",
                                                                             "name": "Alex",
                                                                     "birth" : "1960",
                                                                     "salary" : "200000",
                                                                     "department" : "5"})


if __name__ == "__main__":
    unittest.main()
