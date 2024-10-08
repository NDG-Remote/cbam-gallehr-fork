# Copyright (c) 2024, phamos GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Good(Document):
	def validate(self):
		self.get_responsible_employee()
		self.split_good()

	def before_save(self):
		if self.is_data_confirmed == True:
			self.status = "Done"

	def get_responsible_employee(self):
		if self.supplier and not self.employee:
			supplier_doc = frappe.get_doc("Supplier", self.supplier)
			for child in supplier_doc.employees:
				if child.is_main_contact == True:
					main_contact = child.employee_number
					self.employee = main_contact

	def split_good(self):
		if self.good_values == "Various Components":
			total_raw_mass = sum(
				getattr(self, attr, 0) or 0
				for attr in [
					'split_raw_mass_1',
					'split_raw_mass_2',
					'split_raw_mass_3',
					'split_raw_mass_4',
					'split_raw_mass_5'
				]
			)
			next_highest_split_number = 0
			if total_raw_mass != self.raw_mass:
				original_raw_mass = self.raw_mass
				frappe.throw(f"The raw mass total of the components is not equal to the raw mass of the original good. <br><br> The total should be {original_raw_mass}, not {total_raw_mass}. <br><br> Please change the raw masses of the components and ensure that they add up to a total of {original_raw_mass}")
			else:
				self.status = "Done"
				if self.split_raw_mass_1 and self.split_raw_mass_1 != "0":
					new_good = frappe.new_doc("Good")
					new_good.master_reference_number_mrn = self.master_reference_number_mrn + "-" + f"{next_highest_split_number:02}"
					new_good.hand_over_date = self.hand_over_date
					new_good.article_number = self.article_number
					new_good.good_description = self.good_description
					new_good.customs_tariff_number = self.customs_tariff_number
					new_good.country_of_origin = self.country_of_origin
					new_good.shipping_country = self.shipping_country
					new_good.customs_procedure = self.customs_procedure
					new_good.raw_mass = self.split_raw_mass_1
					if self.responsibility_1 == "I'm the responsible Person":
						new_good.supplier = self.supplier
						new_good.employee = self.employee
					elif self.responsibility_1 == "Another employee is responsible":
						new_good.supplier = self.supplier
						new_good.employee = self.responsible_employee_1
					elif self.responsibility_1 == "Another supplier is responsible":
						new_good.supplier = self.responsible_supplier_1
						# ToDo new_good.employee = self.employee
					else:
						frappe.throw("Please select a responsibility")
					new_good.insert()
					next_highest_split_number += 1
				if self.split_raw_mass_2 and self.split_raw_mass_2 != "0":
					new_good = frappe.new_doc("Good")
					new_good.master_reference_number_mrn = self.master_reference_number_mrn + "-" + f"{next_highest_split_number:02}"
					new_good.hand_over_date = self.hand_over_date
					new_good.article_number = self.article_number
					new_good.good_description = self.good_description
					new_good.customs_tariff_number = self.customs_tariff_number
					new_good.country_of_origin = self.country_of_origin
					new_good.shipping_country = self.shipping_country
					new_good.customs_procedure = self.customs_procedure
					new_good.raw_mass = self.split_raw_mass_2
					if self.responsibility_2 == "I'm the responsible Person":
						new_good.supplier = self.supplier
						new_good.employee = self.employee
					elif self.responsibility_2 == "Another employee is responsible":
						new_good.supplier = self.supplier
						new_good.employee = self.responsible_employee_2
					elif self.responsibility_2 == "Another supplier is responsible":
						new_good.supplier = self.responsible_supplier_2
						# ToDo new_good.employee = self.employee
					else:
						frappe.throw("Please select a responsibility")
					new_good.insert()
					next_highest_split_number += 1
				if self.split_raw_mass_3 and self.split_raw_mass_3 != "0":
					new_good = frappe.new_doc("Good")
					new_good.master_reference_number_mrn = self.master_reference_number_mrn + "-" + f"{next_highest_split_number:02}"
					new_good.hand_over_date = self.hand_over_date
					new_good.article_number = self.article_number
					new_good.good_description = self.good_description
					new_good.customs_tariff_number = self.customs_tariff_number
					new_good.country_of_origin = self.country_of_origin
					new_good.shipping_country = self.shipping_country
					new_good.customs_procedure = self.customs_procedure
					new_good.raw_mass = self.split_raw_mass_3
					if self.responsibility_3 == "I'm the responsible Person":
						new_good.supplier = self.supplier
						new_good.employee = self.employee
					elif self.responsibility_3 == "Another employee is responsible":
						new_good.supplier = self.supplier
						new_good.employee = self.responsible_employee_3
					elif self.responsibility_3 == "Another supplier is responsible":
						new_good.supplier = self.responsible_supplier_3
						# ToDo new_good.employee = self.employee
					else:
						frappe.throw("Please select a responsibility")
					new_good.insert()
					next_highest_split_number += 1
				if self.split_raw_mass_4 and self.split_raw_mass_4 != "0":
					new_good = frappe.new_doc("Good")
					new_good.master_reference_number_mrn = self.master_reference_number_mrn + "-" + f"{next_highest_split_number:02}"
					new_good.hand_over_date = self.hand_over_date
					new_good.article_number = self.article_number
					new_good.good_description = self.good_description
					new_good.customs_tariff_number = self.customs_tariff_number
					new_good.country_of_origin = self.country_of_origin
					new_good.shipping_country = self.shipping_country
					new_good.customs_procedure = self.customs_procedure
					new_good.raw_mass = self.split_raw_mass_4
					if self.responsibility_4 == "I'm the responsible Person":
						new_good.supplier = self.supplier
						new_good.employee = self.employee
					elif self.responsibility_4 == "Another employee is responsible":
						new_good.supplier = self.supplier
						new_good.employee = self.responsible_employee_4
					elif self.responsibility_4 == "Another supplier is responsible":
						new_good.supplier = self.responsible_supplier_4
						# ToDo new_good.employee = self.employee
					else:
						frappe.throw("Please select a responsibility")
					new_good.insert()
					next_highest_split_number += 1
				if self.split_raw_mass_5 and self.split_raw_mass_5 != "0":
					new_good = frappe.new_doc("Good")
					new_good.master_reference_number_mrn = self.master_reference_number_mrn + "-" + f"{next_highest_split_number:02}"
					new_good.hand_over_date = self.hand_over_date
					new_good.article_number = self.article_number
					new_good.good_description = self.good_description
					new_good.customs_tariff_number = self.customs_tariff_number
					new_good.country_of_origin = self.country_of_origin
					new_good.shipping_country = self.shipping_country
					new_good.customs_procedure = self.customs_procedure
					new_good.raw_mass = self.split_raw_mass_5
					if self.responsibility_5 == "I'm the responsible Person":
						new_good.supplier = self.supplier
						new_good.employee = self.employee
					elif self.responsibility_5 == "Another employee is responsible":
						new_good.supplier = self.supplier
						new_good.employee = self.responsible_employee_5
					elif self.responsibility_5 == "Another supplier is responsible":
						new_good.supplier = self.responsible_supplier_5
						# ToDo new_good.employee = self.employee
					else:
						frappe.throw("Please select a responsibility")
					new_good.insert()
					next_highest_split_number += 1