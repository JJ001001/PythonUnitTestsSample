import inc_dec    # The code to test
import unittest   # The test framework


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 4)

class Test_TestAssert(unittest.TestCase):
    def test_isEqual(self):
        self.assertEqual(4, 4)

    # Negative scernaio?
    def test_isNotEqual(self):
        self.assertNotEqual(3, 4)

class Test_Colleague_data_struture(unittest.TestCase):
    def test_firstname(self):
        e = "JohnSmith"
        a = inc_dec.firstname
        self.assertEqual(a,e) #test assert....(actual, expected)

    def test_firstname_maxlength(self):
        e = int(11)
        a = int(len(inc_dec.firstname))
        self.assertLessEqual(a,e) #test assert....(actual, expected)

    def test_firstname_greaterthanzero(self):
            e = int(0)
            a = int(len(inc_dec.firstname))
            self.assertGreaterEqual(a,e) #test assert....(actual, expected)
        


if __name__ == '__main__':
    unittest.main()