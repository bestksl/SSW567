# @Author: HaoxuanLi  
# @Date 2/19/2019
# CWID: 10434197
from unittest import TestCase
from HW04 import HW4


class myTest(TestCase):
    def test_get_repo(self):
        self.assertNotEqual(0, len(HW4.get_repo("bestksl")))
