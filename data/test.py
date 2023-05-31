import unittest
from pathlib import Path
import sqlalchemy as sqalch

class TestFetchDE(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("de.sqlite").is_file())
	
	def test_dbTablesExists(self):
		engine = sqalch.create_engine("sqlite:///de.sqlite")
		insp = sqalch.inspect(engine)
		self.assertTrue(insp.has_table("generalAviation"))
		self.assertTrue(insp.has_table("commercialAviation"))			

class TestFetchUS(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("us.sqlite").is_file())

	def test_dbTablesExists(self):
		engine = sqalch.create_engine("sqlite:///us.sqlite")
		insp = sqalch.inspect(engine)
		self.assertTrue(insp.has_table("events"))
		self.assertTrue(insp.has_table("aircraft"))			
		self.assertTrue(insp.has_table("injury"))

class TestAnalysis(unittest.TestCase):
	def test_dbExists(self):
		self.assertTrue(Path("results.sqlite").is_file())

	def test_dbTablesExists(self):
		engine = sqalch.create_engine("sqlite:///results.sqlite")
		insp = sqalch.inspect(engine)
		self.assertTrue(insp.has_table("incidentAnalysisUS"))
		self.assertTrue(insp.has_table("incidentAnalysisDE"))			
	
if __name__ == '__main__':
	print("testing " )
	unittest.main()
