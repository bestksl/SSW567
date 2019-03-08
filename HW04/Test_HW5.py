# @Author: HaoxuanLi  
# @Date 2/19/2019
# CWID: 10434197
from unittest import TestCase,mock
from unittest.mock import patch, Mock
from requests import get
from HW04 import HW5


class myTest(TestCase):

    @mock.patch('HW5.requests.get')
    def test_get_repo(self, mock_get_repo):
        raw_results = [{{'name': '810_final'}, {'name': 'fluskDemo'}, {'name': 'HadoopDemo'}, {'name': 'hobbymatcher'},
                        {'name': 'MapReduceDemo'}},
                       [[1, 1, 1], [1, 1, 1, 1, 1], [1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

        results = list([Mock(), Mock(), Mock(), Mock(), Mock(), Mock()])
        for i in range(0, 4):
            results[i].return_value = raw_results[i]
        mock_get_repo.side_effects = results
        self.assertNotEqual(0, len(HW5.get_repo("bestksl")))
