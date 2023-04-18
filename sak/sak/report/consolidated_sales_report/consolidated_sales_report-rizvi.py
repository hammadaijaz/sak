# Copyright (c) 2023, SRCA and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cstr


def execute(filters=None):
	if not filters:
		filters = {}

	columns, data = get_columns(), []

	pos_conditions = get_pos_conditions(filters)
	so_conditions = get_so_conditions(filters)
	shop_profiles = get_shop_profiles(filters)

	grand_totals = {"posting_date": f"<b>Grand Totals</b>", "pos_amount": 0.0, "so_amount":0.0, "tax_amount": 0.0, "grand_total": 0.0}
	for shop in shop_profiles:
		shop_row = {}
		data.append(shop_row)
		shop_totals = {"posting_date": f"<b>{shop.name}</b>", "pos_amount": 0.0, "so_amount":0.0, "tax_amount": 0.0, "grand_total": 0.0}
		pos_data = get_pos_data(filters, pos_conditions, shop.name)
		for pos in pos_data:
			pos_inv = {}
			pos_inv["posting_date"] = pos.get("posting_date")
			pos_inv["pos_profile"] = pos.get("pos_profile")
			pos_inv["order_no"] = pos.get("name")
			pos_inv["transaction_type"] = "POS Invoice"
			pos_inv["pos_amount"] = pos.get("net_total")
			pos_inv["tax_amount"] = pos.get("total_taxes_and_charges")
			pos_inv["grand_total"] = pos.get("grand_total")
			pos_inv["status"] = pos.get("status")

			data.append(pos_inv)

			shop_totals["pos_amount"] += float(pos.get("net_total"))
			shop_totals["tax_amount"] += float(pos.get("total_taxes_and_charges"))

		so_data = get_so_data(filters, so_conditions, shop.name)
		for order in so_data:
			so = {}
			so["posting_date"] = order.get("transaction_date")
			so["pos_profile"] = order.get("pos_profile")
			so["order_no"] = order.get("name")
			so["transaction_type"] = "Sales Order"
			so["so_amount"] = order.get("net_total")
			so["tax_amount"] = order.get("total_taxes_and_charges")
			so["grand_total"] = order.get("grand_total")
			so["status"] = order.get("status")

			data.append(so)

			shop_totals["so_amount"] += float(order.get("net_total"))
			shop_totals["tax_amount"] += float(order.get("total_taxes_and_charges"))
		shop_totals["grand_total"] = shop_totals["pos_amount"] + shop_totals["so_amount"] + shop_totals["tax_amount"]
		data.append(shop_totals)
		grand_totals["pos_amount"] += shop_totals["pos_amount"] or 0.0
		grand_totals["so_amount"] += shop_totals["so_amount"] or 0.0
		grand_totals["tax_amount"] += shop_totals["tax_amount"] or 0.0
		grand_totals["grand_total"] += shop_totals["grand_total"]
	data.append(grand_totals)
	data.reverse()
	
	chart = get_chart_data(data[0])
	report_summary = get_report_summary(
		data[0]
	)
	return columns, data, None, chart, report_summary



def get_shop_profiles(filters):
	conditions = ""
	if filters.get("pos_profile"):
		conditions += " and name='{}'".format(filters.get("pos_profile"))
	data = frappe.db.sql("""SELECT * FROM `tabPOS Profile` where disabled=0 {}""".format(conditions), as_dict=True)

	return data

def get_pos_data(filters, conditions, shop):

	data = frappe.db.sql(""" select * from `tabPOS Invoice` 
		where status not in ('Consolidated', 'Cancelled') and docstatus<2 and pos_profile='{}' {}""".format(shop, conditions), as_dict=True, debug=True)

	return data

def get_so_data(filters, conditions, shop):

	data = frappe.db.sql(""" select * from `tabSales Order` where docstatus<2 and pos_profile='{}' {}""".format(shop, conditions), as_dict=True, debug=True)

	return data

def get_pos_conditions(filters):
	conditions = ""
	if filters.get("start_date"):
		conditions += " and posting_date>='{}'".format(filters.get("start_date"))
	if filters.get("end_date"):
		conditions += " and posting_date<='{}'".format(filters.get("end_date"))
	return conditions

def get_so_conditions(filters):
	conditions = ""
	if filters.get("start_date"):
		conditions += " and transaction_date>='{}'".format(filters.get("start_date"))
	if filters.get("end_date"):
		conditions += " and transaction_date<='{}'".format(filters.get("end_date"))
	return conditions


def get_columns():
	columns = [
		{
			'fieldname': 'posting_date',
			'label': _(""),
			'fieldtype': 'Data',
			'width': 200,
		},
		{
			'fieldname': 'pos_profile',
			'label': _("Shop"),
			'fieldtype': 'Data',
			'width': 200,
		},
		{
			'fieldname': 'order_no',
			'label': _("Order No"),
			'fieldtype': 'Data',
			'width': 200,
		},
		{
			'fieldname': 'transaction_type',
			'label': _("Transaction Type"),
			'fieldtype': 'Data',
			'width': 120,
		},
		{
			'fieldname': 'pos_amount',
			'label': _("POS Amount"),
			'fieldtype': 'Currency',
			'width': 160,
		},
		{
			'fieldname': 'so_amount',
			'label': _("SO Amount"),
			'fieldtype': 'Currency',
			'width': 160,
		},
		{
			'fieldname': 'tax_amount',
			'label': _("Tax Amount"),
			'fieldtype': 'Currency',
			'width': 160,
		},
		{
			'fieldname': 'grand_total',
			'label': _("Grand Total"),
			'fieldtype': 'Currency',
			'width': 160,
		},
		{
			'fieldname': 'status',
			'label': _("Status"),
			'fieldtype': 'Data',
			'width': 120,
		},
	]

	return columns


def get_report_summary(data):

	# frappe.log_error(data, "DATA In get report_summary")
	return [
		{"value": data.get("grand_total"), "label": _("Grand Total"), "indicator": "Green" if data.get("grand_total") > 0 else "Red", "datatype": "Currency", "currency": "PKR"},
		{
			"value": data.get('pos_amount'),
			"label": _("Point of Sale"),
			"indicator": "Green" if data.get("pos_amount") > 0 else "Red",
			"datatype": "Currency",
			"currency": "PKR",
		},
		{"value": data.get('so_amount'), "label": _("Sales Order"), "indicator": "Green" if data.get("so_amount") > 0 else "Red", "datatype": "Currency", "currency": "PKR"},
		{
			"value": data.get('tax_amount'),
			"label": _("Taxes"),
			"indicator": "Green" if data.get("tax_amount") < 0 else "Red",
			"datatype": "Currency",
			"currency": "PKR",
		},
	]

def get_chart_data(data):
	# labels = [d for d in data.keys()]
	labels = ["Sales Chart"]

	datasets = []
	datasets.append({"name": _("Grand Total"), "values": [data.get("grand_total")]})
	datasets.append({"name": _("Point of Sale"), "values": [data.get("pos_amount")]})
	datasets.append({"name": _("Sales Orders"), "values": [data.get("so_amount")]})
	datasets.append({"name": _("Taxes"), "values": [data.get("tax_amount")]})
		

	chart = {"data": {"labels": labels, "datasets": datasets}}
	chart["type"] = "bar"
	chart["colors"] = ["green", "blue", "orange", "red"]

	return chart