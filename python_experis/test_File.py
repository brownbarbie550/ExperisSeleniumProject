from importlib.metadata import files
from unittest import TestCase
from python_experis.File import File

class TestFile(TestCase):
    def setUp(self):  #starts every test
        self.file = File("file1", "docx", 40)

    def tearDown(self):
        print("it is tear down")

    def test1_init_valid(self):
        """test a simple valid case of init"""
        self.assertEqual("file1", self.file.name)
        self.assertEqual("docx", self.file.suffix)
        self.assertEqual(40, self.file.size)

    def test_init_invalid_negative_size(self):
        """in case of a negative size, the size should be initialized to 0"""
        file = File("file1", "txt", -100)
        self.assertEqual(0, file.size)


    def tes_init_invalid_size_type(self):
        """in case of an invalid type of argument size. __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1","txt", "100")

    def test_init_invalid_name_type(self):
        """in case of an invalid type of argument name __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1", "txt", 100)

    def test_init_invalid_suffix_type(self):
        """in case of an invalid type of argument suffix __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1", [1,2,3,4,5.], 100)

    def test_init_invalid_suffix_short(self):
        with self.assertRaises(ValueError):
            file = File("file1", "s", 100)

    def test_init_invalid_suffix_long(self):
        with self.assertRaises(ValueError):
            file = File("file1", "abcdefghij", 100)





    def test_eq_valid(self):
        file = File("file1", "docx", 40)
        self.assertTrue(self.file == file)

    def test_eq_valid_different_size(self):
        file = File("file1", "docx", 40)
        self.assertTrue(self.file == file)

    def test_eq_valid_suffix_not_equal(self):
        file = File("file1", "txt", 40)
        self.assertFalse(self.file == file)

    def test_eq_valid_name_not_equal(self):
        file = File("file1", "docx", 40)
        self.assertFalse(self.file == file)

    def test_eq_not_valid(self):
        self.assertFalse(self.file == 10)

    def test_gt_valid_True(self):
        file = File("file1", "docx", 30)
        self.assertTrue(self.file > file)

    def test_gt_valid_False(self):
        file = File("file1", "docx", 50)
        self.assertFalse(self.file > file)

    def test_gt_invalid(self):
        with self.assertRaises(TypeError):
            print(self.file > 10)








