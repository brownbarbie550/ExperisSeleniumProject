#objects exercise 4
from importlib.metadata import files

#this class is used to create hard disk objects
#hard disk attributes are: size, files (a dictionary- key: file_name, value: file size
#methods: add_file, del_file, update_file, used_space, free_space
from python_experis.File import File
class Hard_Disk:

    def __init__(self, size):
        """__init__ create an empty hard disk:
        initializes the attribute: size
        the attribute files is a list that will be empty when the HD is created"""
        if type(size) != int:
            raise TypeError("disk size mjust be int")
        if size < 0:
            size = 0
        self.disk_size = size
        self.files = []

    def space_used(self):
        """returns the sum of all the file sizes
        go through the list of files and sum the size of each file object"""
        sum_sizes = 0
        for file in self.files:
            sum_sizes += file.size
        return sum_sizes

    def space_free(self):
        return self.disk_size - self.space_used()

    def add_file(self, file):
        """add file will add a file to the dictionary if it doesn't exist and
        if there is enough space, return a boolean value if it succeeded or not"""
        #check the type of argument: file
        if type(file) == str:
            raise TypeError("invalid file")
        if file in self.files:
            print(f"{file.name},{file.suffix} already exists")
            return False

        #check if there is no space for the file
        if self.space_free() < file.size:
            print(f"no space for file: {file.name}.{file.suffix}")
            return False

        #all valid - add the file to the files dictionary
        self.files.append(file)
        return True


    def del_file(self, file:File):
        """delete a file from the dictionary if the file exists
        return a boolean value if it succeeded or not"""
        if file in self.files:
            self.files.remove(file)
            return True

        print(f"{file.name}.{file.suffix} doesn't exist")
        return False

    def update_file(self, file: File):
        """update a file in the list:
        if the file exists and there is enough space - update to the new size, otherwise
        print a message return a boolean value if it succeeded or not"""
        #check if the file doesn't exist in the list
        if file not in self.files:
            print(f"error: file {file.name}.{file.suffix} doesn't exist")
            return False

        #find the file in the list
        file_index = self.files.index(file)

        #check if there is not enough space for the new size
        if self.space_free() + self.files[file_index].size < file.size :
            print(f"no space for updating file: {file.name}.{file.suffix}")
            return False

        #all valid - update the file size
        self.files[file_index] = file
        return True

    def biggest_file(self):
        """returns the file with highest size"""
        return max(self.files)

    def __str__(self):
        return f"HD: size {self.disk_size} \n{self.files} used space:{self.space_used()} free space:{self.space_free()}"

if __name__ == "__main__":
    hd1 = Hard_Disk(200)
    file1 = File("file1", "docx", 30)#create a disk with size 1000 GB
    file2 = File("file1", "txt", 60)#create a disk with size 1000 GB
    file3 = File("file1", "txt", 20)#create a disk with size 1000 GB
    file4 = File("file4", "txt", 20)

    hd1.add_file(file1)
    hd1.add_file(file2)
    hd1.add_file(file3)
    print(hd1)
    file1 = File("file1", "docx", 110)
    hd1.update_file(file1)
    print(hd1)
    print(hd1.biggest_file())

    hd1.add_file(file2)
    hd1.add_file(file4)
    print(hd1)
    hd1.del_file(file1)
    print(hd1)
