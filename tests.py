import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    
    def test_get_files_info(self):
        self.maxDiff = None

        test_cases = [
                ("calculator", ".", 
                """Result for current directory:\n  - pkg: file_size=4096 bytes, is_dir=True\n  - tests.py: file_size=1390 bytes, is_dir=False\n  - main.py: file_size=600 bytes, is_dir=False"""
                ),

                ("calculator", "pkg", """Result for 'pkg' directory:\n  - render.py: file_size=788 bytes, is_dir=False\n  - calculator.py: file_size=1797 bytes, is_dir=False\n  - __pycache__: file_size=4096 bytes, is_dir=True"""
                ),

                ("calculator", "/bin", """Result for '/bin' directory:\n  - Error: Cannot list "/bin" as it is outside the permitted working directory"""
                ),

                ("calculator", "../", """Result for '../' directory:\n  - Error: Cannot list "../" as it is outside the permitted working directory""")
            ]

        for working_directory, directory, expected in test_cases:
            with self.subTest(working_directory=working_directory, directory=directory):
                result = get_files_info(working_directory, directory)
                self.assertEqual(result, expected)
                print(result)

if __name__ == '__main__':
    unittest.main()