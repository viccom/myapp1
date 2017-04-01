# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _

def get_context(context):
	context.no_cache = 1
	#frappe.get_all()
	#frappe.get_doc("Wechat App", "test")
	#frappe.get_value("Wechat App", "test", "domain")
	#frappe.db.get_values("Wechat App", filters={"name": "test"}, fields=["name", "domain", "admin"] )
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context.doc = frappe.get_all("User")
	context.detail = frappe.get_doc("User", "3520845@qq.com")
	context.detaildict = frappe.get_doc("User", "3520845@qq.com").as_dict()

