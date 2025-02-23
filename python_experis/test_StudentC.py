from unittest import TestCase
from StudentC import StudentC
from unittest import mock
from unittest.mock import patch


class TestStudentC(TestCase):
    def setUp(self):
        self.studs = StudentC(123456789, 25, "barbie")
        self.studs1 = StudentC(123321789, 25, "brown")
        self.studs2 = StudentC(123423589, 25, "dagi")
        self.studs3 = StudentC(129126789, 25, "habesha")


    def tearDown(self):
        print("it is tear down")

    def test_init_(self):
        self.assertEqual(123456789, self.studs.id_num)
        self.assertEqual(25, self.studs.age)
        self.assertEqual("barbie", self.studs.stud_name)
        self.assertEqual({}, self.studs.grades)


    def test_init_id_num_invalid(self):
        with self.assertRaises(TypeError):
            file = StudentC("123456789", "25", "barbie")

    def test_init_invalid_age(self):
        with self.assertRaises(TypeError):
            file = StudentC(123456789, "25", "barbie")

    def test_negative_age(self):
        with self.assertRaises(TypeError):
            file = StudentC(123456789, 5, "barbie")

    def test_stud_name_invalid(self):
        with self.assertRaises(TypeError):
            file = StudentC(123456789, 25, "barbie")



    def add_grade_valid(self):
        student = StudentC("12334567", 25, "dagi")
        student.add_grade("math", 100)
        self.assertEqual(student.grades, 100)

    def add_grade_invalid(self):
        student = StudentC("12334567", 25, "dagi")
        student.add_grade("math", -100)
        self.assertEqual(student.grades, 0)


    # @mock.patch('StudentC.StudentC.average', return_value={123456789: 74, 321654987:74, 456896523:80})
    def test_average_valid(self):
        self.studs.grades = [74,84,80]
        expected_avg = (74 + 84 + 80) / 3
        self.assertEqual(self.studs.average, expected_avg)



    #
    # def test_calc_factor(self):
    #     self.fail()
    #
    # def test_average(self):
    #     self.fail()
