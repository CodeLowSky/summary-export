import sys
import os
import unittest

try:
    import summary_export
except:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
    import summary_export
    
class TestSummaryExport(unittest.TestCase):
	def setUp(self):
		try:
			self.summary = summary_export.Summary('./data/test_data.txt')
		except:
			self.summary = summary_export.Summary('../data/test_data.txt')

	def test_get_order_number(self):
		self.assertEqual('1234567', self.summary.order_number[0])

	def test_get_parent_lpn(self):
		self.assertEqual('DUMMYLPN1', self.summary.parent_lpn[0])

	def test_get_product_id(self):
		self.assertEqual('DUMMYPID12', self.summary.product_id[0])

	def test_get_quantity(self):
		self.assertEqual('1', self.summary.quantity[0])

	def test_get_serial_number(self):
		self.assertEqual('11-11111111', self.summary.serial_number[0])

if __name__ == '__main__':
    unittest.main()
