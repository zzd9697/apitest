import unittest
from test.case.basecase import BaseCase
from lib.db import check_signature


class TestSignature(BaseCase):
    def test_signature_insert_normal(self):
        case_data = self.get_case_data("test_signature_insert_normal")
        self.send_request(case_data)
        check_signature("8签名")


if __name__ == '__main__':
    unittest.main(verbosity=2)
