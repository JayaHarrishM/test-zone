import unittest as u
import sample1

class Testfunc(u.TestCase):
    def test_allfunctions(self):
        self.assertEqual(sample1.add(1,5),6)
        self.assertEqual(sample1.multiply(1,5),6)
        self.assertEqual(sample1.divide(1,5),0)
if __name__ == "__main__":
    u.main()