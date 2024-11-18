# Copyright (c) 2024, Ankush and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		server_charge = 0
		if len(self.ride_add_on) > 0:
			for rate in self.ride_add_on:
				server_charge += rate.amount

		# forumal Price Per Km) * (Estimated Km) + (Total Amount from Services Table))
		if server_charge > 0 and self.estimated_km > 0:
			self.total_amount = (self.price * self.estimated_km) + server_charge 








