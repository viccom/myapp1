# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "myapp1",
			"color": "green",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("myapp1")
		}
	]
