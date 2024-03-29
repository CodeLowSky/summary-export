import openpyxl
import argparse
import os

PID_OFFSET = -1
QUANTITY_OFFSET = 2

class Summary:
	def __init__(self, input):
		self.input = input
		self._read_summary()
		self._get_indices()
		self.order_number = self._get_vals(self.idx_order)
		self.parent_lpn = self._get_vals(self.idx_lpn)
		self.product_id = self._get_vals(self.idx_pid+PID_OFFSET)
		self.quantity = self._get_vals(self.idx_qty+QUANTITY_OFFSET)
		self.serial_number = self._get_vals(self.idx_sn)
		
	def _read_summary(self):
		with open(self.input, encoding = "ISO-8859-1") as file:
			self.summary = file.readlines()
			
	def _get_indices(self):
		for text in self.summary:
			if text.find('Order#') != -1:
				self.idx_order = text.find('Order#')
				self.idx_lpn = text.find('LPN')
				self.idx_pid = text.find('Product ID')
				self.idx_qty = text.find('Qty')
				self.idx_sn = text.find('Serial No.')

	def _get_vals(self, idx):
		val = []
		for text in self.summary:
			if text[1:7].isdigit(): #line starts with blank + order number
				val.append(text[idx:].split(' ')[0].strip())
			
		return val

class Worksheet:
	def __init__(self):
		self.wb = openpyxl.Workbook()
		self.ws = self.wb.active
		self.row = 1

	def save(self):
		self.wb.save('summary.xlsx')

	def import_summary(self, summary):
		self._write_to_worksheet(summary.order_number, 'A')
		self._write_to_worksheet(summary.parent_lpn, 'B')
		self._write_to_worksheet(summary.product_id, 'C')
		self._write_to_worksheet(summary.quantity, 'D')
		self._write_to_worksheet(summary.serial_number, 'E')
		
	def _write_to_worksheet(self, vals, col):
		for idx, val in enumerate(vals):
			cell = col+str(self.row+idx)
			self.ws[cell] = val

parser = argparse.ArgumentParser(description='Process Summary files to Excel Sheet.')
parser.add_argument('-p', '--path', type=str, default=".", help='Input path to summary files, default is the current path')
	
def main():
	args = parser.parse_args()
	path = args.path
	summarys = []

	for filename in os.listdir(path):
		if filename.lower().endswith(".txt"):
			file = os.path.join(os.path.abspath(path), filename)
			print("Found: {}".format(file))
			summarys.append(Summary(file))
			continue
		else:
			continue

	worksheet = Worksheet()

	for summary in summarys:
		worksheet.import_summary(summary)

	try:
		worksheet.save()
		print("Summary export successful!")
	except PermissionError as e:
		print("Error: {} still open!".format(e))

if __name__ == '__main__':
	main()
