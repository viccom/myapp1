# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals
import frappe
import json
import requests
from frappe import throw, msgprint, _
from frappe.model.document import Document
from frappe.utils import cint
from frappe.api import validate_oaut

validate_oauth()

@frappe.whitelist()
def test():
	r = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
	#r = frappe.form_dict.user or frappe.form_dict.name
	if r:
		return r

