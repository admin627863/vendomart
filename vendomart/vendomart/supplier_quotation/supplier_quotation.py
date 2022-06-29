import frappe
from datetime import date, datetime, timedelta
from frappe.utils import date_diff


def auto_share_document(doc, handler=""):
    frappe.share.add(doc.doctype, doc.name, doc.quotation_from, write=1, share=1,
				flags={"ignore_share_permission": True})