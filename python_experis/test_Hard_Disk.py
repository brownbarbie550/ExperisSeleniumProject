from unittest import TestCase
from File import File
from Hard_Disk import Hard_Disk
from unittest import mock
from unittest.mock import patch



class TestHard_Disk(TestCase):

    def setUp(self):
        self.hd = Hard_Disk(300)
        self.file1 = File("file1", "txt", 50)
        self.file2 = File("file1", "py", 70)
        self.file3 = File("file1", "docx", 20)

    def test_init_valid(self):
        self.assertEqual(300,self.hd.disk_size)
        self.assertEqual([], self.hd.files)

    def test_init_invalid_size_type(self):
        with self.assertRaises(TypeError):
            hd = Hard_Disk("200")

    def test_init_invalid_negative_size(self):
        hd = Hard_Disk(-50)
        self.assertEqual(0, hd.disk_size)


    def test_space_used1(self):
        """check used space for hard disk with some files"""
        self.hd.files = [self.file1, self.file2, self.file3]
        print("xxxxxxxx",self.hd.space_used())
        self.assertEqual(140, self.hd.space_used())

    def test_used_space_empty_hd(self):
        self.assertEqual(0, self.hd.space_used())

    def test_used_space_full_hd(self):
        """create files that will use all the hard disk space and test space_used"""
        file1 = File("aaa", "txt", 100)
        file2 = File("bbb", "txt", 100)
        file3 = File("ccc", "txt", 100)
        self.hd.files = [file1,file2,file3]
        self.assertEqual(300, self.hd.space_used())




    @mock.patch('Hard_Disk.Hard_Disk.space_used', return_value=280)
    def test_free_space_few_files(self, mock_space_used):
        """test a case with a few files in the hd"""
        mock_space_used.return_value = 200
        self.assertEqual(100, self.hd.space_free())
        mock_space_used.return_value = 160
        self.assertEqual(140, self.hd.space_free())

    @mock.patch('Hard_Disk.Hard_Disk.space_used', return_value=300)
    def test_free_space_full_hd(self, mock_space_used):
        """test a case with a few files in the hd"""
        self.assertEqual(0, self.hd.space_free())
        mock_space_used.assert_called_once_with() #check that the mocked method is called once

    def test_free_space_empty_hd(self):
        with patch('Hard_Disk.Hard_Disk.space_used') as mock_space_used:
            mock_space_used.return_value = 0
            self.assertEqual(300, self.hd.space_free())
            mock_space_used.assert_called_once_with()  # check that the mocked method is called once



    @mock.patch('Hard_Disk.Hard_Disk.space_free', return_value=300)
    @mock.patch('Hard_Disk.Hard_Disk.space_used', return_value=0)
    def test_add_file_valid1(self, mock_space_used, mock_space_free):
        """add file to a hard disk that is not empty"""
        # self.assertEqual("first file", self.hd.add_file(self.file1))
        self.hd.files = [self.file1, self.file2]
        self.assertTrue(self.hd.add_file(self.file3))
        self.assertEqual([self.file1, self.file2, self.file3], self.hd.files)

    def test_add_file_file_exists(self):
        """try to add a file that already exists"""
        self.hd.files = [self.file1, self.file2]
        self.assertFalse(self.hd.add_file(self.file2))
        self.assertEqual([self.file1, self.file2], self.hd.files)

    def test_add_file_disk_no_space(self):
        """try to add a file when there is no space"""
        self.hd.files = [self.file1, self.file2, self.file3]
        file = File("aaa", "txt", 170)
        self.assertFalse(self.hd.add_file(file))
        self.assertEqual([self.file1, self.file2, self.file3], self.hd.files)

    def test_add_file_invalid_file(self):
        """try to add invalid file to the hard disk"""
        with self.assertRaises(TypeError):
            self.hd.add_file("file1")

    def test_add_file_reach_disk_size(self):
        """in this case the new file size equals the free space"""
        self.hd.files = [self.file1, self.file2, self.file3]
        file = File("aaa", "txt", 160)
        self.assertTrue(self.hd.add_file(file))
        self.assertEqual([self.file1, self.file2, self.file3, file], self.hd.files)












    # def test_del_file(self):
    #     self.fail()
    #
    # def test_update_file(self):
    #     self.fail()
    #
    # def test_biggest_file(self):
    #     self.fail()
