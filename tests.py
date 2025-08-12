import unittest
import os
from functions.write_file import write_file

class TestGetFilesInfo(unittest.TestCase):

    def test_write_file(self):
        test_cases = [
            ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
            ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
            ("calculator", "/tmp/temp.txt", "this should not be allowed"),
        ]

        for working_directory, file_path, content in test_cases:
            with self.subTest(working_directory=working_directory, file_path=file_path, content=content):
                with self.subTest(working_directory=working_directory, file_path=file_path, content=content):
                    result = write_file(working_directory, file_path, content)
                    file = os.path.abspath(os.path.join(file_path))
                    if os.path.exists(file):
                        with open(file, "r") as f:
                            c = f.read()
                            self.assertIn(content, c)
                            
                    print(result)

if __name__ == '__main__':
    unittest.main()