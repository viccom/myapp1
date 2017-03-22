# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals
import frappe
import json
import requests
from frappe import throw, msgprint, _
from frappe.model.document import Document
from frappe.utils import cint

@frappe.whitelist(allow_guest=True)
def test():
	r = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
	if r:
		return json.dumps(r);