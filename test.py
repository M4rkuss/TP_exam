import unittest
import index as app

class Test(unittest.TestCase):
	def test_count_sum(self):
		self.assertEqual(app.count_sum(3), 12)
		self.assertEqual(app.count_sum(5), 35)

if __name__ == '__main__':
    unittest.main()