import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# This method runs automatically right before saving to the database
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name or ''}".strip()