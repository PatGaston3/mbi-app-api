import unittest
from api import api


class ApiUnitTest(unittest.TestCase):
    # Validation Failures
    def test_validate_mbi_invalid_length_l_t_11(self):
        self.assertEqual(api.validate_mbi("19SB"), False)

    def test_validate_mbi_invalid_length_g_t_11(self):
        self.assertEqual(api.validate_mbi("2GJ7DD1RV73G"), False)

    def test_validate_mbi_invalid_excluded_chars_s(self):
        self.assertEqual(api.validate_mbi("2SJ7DD1RV73"), False)

    def test_validate_mbi_invalid_excluded_chars_l(self):
        self.assertEqual(api.validate_mbi("2LJ7DD1RV73"), False)

    def test_validate_mbi_invalid_excluded_chars_o(self):
        self.assertEqual(api.validate_mbi("2OJ7DD1RV73"), False)

    def test_validate_mbi_invalid_excluded_chars_i(self):
        self.assertEqual(api.validate_mbi("2IJ7DD1RV73"), False)

    def test_validate_mbi_invalid_excluded_chars_b(self):
        self.assertEqual(api.validate_mbi("2BJ7DD1RV73"), False)

    def test_validate_mbi_invalid_excluded_chars_z(self):
        self.assertEqual(api.validate_mbi("2ZJ7DD1RV73"), False)

    def test_validate_mbi_valid_group_c(self):
        self.assertEqual(api.validate_mbi("GGJ7DD1RV73"), False)

    def test_validate_mbi_valid_group_n(self):
        self.assertEqual(api.validate_mbi("2GJNDDNRVNN"), False)

    def test_validate_mbi_valid_group_an(self):
        self.assertEqual(api.validate_mbi("21L71N11173"), False)

    def test_validate_mbi_valid_group_a(self):
        self.assertEqual(api.validate_mbi("2GJ7DD12273"), False)

    # Validation Success
    def test_validate_mbi_valid(self):
        self.assertEqual(api.validate_mbi("6AY0WP2AT46"), True)


if __name__ == '__main__':
    unittest.main()
