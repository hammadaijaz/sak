import frappe
from frappe import _
import datetime
from frappe.utils import cstr, getdate
import json


@frappe.whitelist()
def get_sales_data(filters):

	data1 = frappe.db.sql(""" SELECT SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-North" GROUP BY is_pos ORDER BY is_pos""", debug=True)
	


	

	datasets = []
	labels = []
	for d in data1:
		labels.append(d[0])
		datasets.append(d[1])

	return {
		'labels': labels,
		'datasets': [{'values': datasets}]
	}

def get_conditions(filters):
	conditions = ""
	return conditions


def get_co(filters):
	conditions = ""
	return conditions