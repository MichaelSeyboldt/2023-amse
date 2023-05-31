import unittest
from pathlib import Path

class TestFetchDE(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("de.sqlite").is_file())


class TestFetchUS(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("us.sqlite").is_file())



class TestAnalysis(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("results.sqlite").is_file())


if __name__ == '__main__':
	print("testing " )
	unittest.main()
