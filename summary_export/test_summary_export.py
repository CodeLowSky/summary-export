import unittest
import summary_export

class TestSummaryExport(unittest.TestCase):
	def setUp(self):
		try:
			self.summary = summary_export.Summary('169812TN.txt')
		except:
			self.summary = summary_export.Summary('summary_export/169812TN.txt')

	def test_get_order_number(self):
		self.assertEqual('4026252', self.summary.order_number[0])

	def test_get_parent_lpn(self):
		self.assertEqual('BUD322890', self.summary.parent_lpn[0])

	def test_get_product_id(self):
		self.assertEqual('6684MC1543', self.summary.product_id[0])

	def test_get_quantity(self):
		self.assertEqual('1', self.summary.quantity[0])

	def test_get_serial_number(self):
		self.assertEqual('13-54889346', self.summary.serial_number[0])

if __name__ == '__main__':
    unittest.main()
