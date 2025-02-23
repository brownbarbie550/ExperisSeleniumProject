from unittest import TestCase
from CourseC import CourseC
from StudentC import StudentC
from unittest import mock
from unittest.mock import patch


class TestCourseC(TestCase):

    def setUp(self):
        self.course1 = CourseC(1, "maths", 10)
        self.student1 = StudentC (123456789, 23, "maths")
        self.student2 = StudentC (789456123, 25, "QA")
        self.student3 = StudentC (321654987, 25, "english")
    def tearDown(self):
        print("tear down")



    @mock.patch('CourseC.CourseC.averages', return_value={123456789: 64, 321654987: 70, 789456123: 99})
    def test_valid_weak_students(self, mock_weak_stud):
        self.assertEqual([123456789], self.course1.weak_students())


    @mock.patch('CourseC.CourseC.averages', return_value={123456789: 74, 321654987:74, 456896523:80})
    def test_invalid_weak_students_2_with_lowest_avg(self, mock_student_avg):
        self.assertEqual([123456789,321654987], self.course1.weak_students())

    def test_empty_course(self):
        self.assertEqual(None, self.course1.averages())


    def test_add_student_valid(self):
        self.course1.add_student(self.student1)
        self.course1.add_student(self.student2)
        self.course1.add_student(self.student3)
        self.assertTrue([self.student1, self.student2, self.student3], self.course1.stud_list)















