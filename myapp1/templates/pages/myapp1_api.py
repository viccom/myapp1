# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import json
import frappe
import frappe.handler
import frappe.client
from frappe.utils.response import build_response
from frappe import _
from urlparse import urlparse
from urllib import urlencode

def handle():
    validate_oauth()

    parts = frappe.request.path[1:].split("/", 3)
    call = doctype = name = None

    if len(parts) > 1:
        call = parts[1]

    if len(parts) > 2:
        doctype = parts[2]

    if len(parts) > 3:
        name = parts[3]

    return build_response("json")



def validate_oauth():
	from frappe.oauth import get_url_delimiter
	form_dict = frappe.local.form_dict
	authorization_header = frappe.get_request_header("Authorization").split(" ") if frappe.get_request_header("Authorization") else None
	if authorization_header and authorization_header[0].lower() == "bearer":
		from frappe.integrations.oauth2 import get_oauth_server
		token = authorization_header[1]
		r = frappe.request
		parsed_url = urlparse(r.url)
		access_token = { "access_token": token}
		uri = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path + "?" + urlencode(access_token)
		http_method = r.method
		body = r.get_data()
		headers = r.headers

		required_scopes = frappe.db.get_value("OAuth Bearer Token", token, "scopes").split(get_url_delimiter())

		valid, oauthlib_request = get_oauth_server().verify_request(uri, http_method, body, headers, required_scopes)

		if valid:
			frappe.set_user(frappe.db.get_value("OAuth Bearer Token", token, "user"))
			frappe.local.form_dict = form_dict