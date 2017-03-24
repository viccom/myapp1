# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals
import frappe
import json
import requests
from frappe import throw, msgprint, _
from frappe.model.document import Document
from frappe.utils import cint
from frappe.api import validate_oauth

validate_oauth()

@frappe.whitelist()
def test():
	r = frappe.db.get_single_value("IOT HDB Settings", "authorization_code")
	if r:
		return r