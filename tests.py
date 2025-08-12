import unittest
from functions.get_file_content import get_file_content
from functions.config import MAX_FILE_SIZE

class TestGetFilesInfo(unittest.TestCase):

    def test_get_file_content(self):
        test_cases = [
            #("calculator", "lorem.txt", MAX_FILE_SIZE + 500, "truncated"),
            ("calculator", "main.py", MAX_FILE_SIZE + 500, "truncated"),
            ("calculator", "pkg/calculator.py", MAX_FILE_SIZE + 500, "truncated"),
            ("calculator", "\\bin\\cat", MAX_FILE_SIZE + 500, "Error"),
            ("calculator", "pkg/does_not_exist.py", MAX_FILE_SIZE + 500, "Error")
        ]

        for working_directory, file_path, size, contains in test_cases:
            with self.subTest(working_directory=working_directory, file_path=file_path):
                contents = get_file_content(working_directory, file_path)
                self.assertLess(contents.__len__(), size)
                if contents.__len__() >= MAX_FILE_SIZE:
                    self.assertIn(contains, contents)
                elif contains == "Error":
                    self.assertIn(contains, contents)
                print(contents)




if __name__ == '__main__':
    unittest.main()