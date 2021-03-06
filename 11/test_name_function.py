import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin嘛"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像Janis 2 Joplin嘛"""
        formatted_name = get_formatted_name('janis','joplin',"2")
        self.assertEqual(formatted_name,'Janis 2 Joplin')
unittest.main()
