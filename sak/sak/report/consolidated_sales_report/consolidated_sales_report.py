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
	# shop_profiles = get_shop_profiles(filters)

	shop_profiles = ['Terminal North - Small Transaction Only', 'Terminal North - Large Transaction Only',
	 				 'Terminal Johar - Small Transaction Only', 'Terminal Johar - Large Transaction Only',
	 				 'Terminal Gulshan - Small Transaction Only', 'Terminal Gulshan - Large Transaction Only',
	 				 'Terminal Sehar - Small Transaction Only', 'Terminal Sehar - Large Transaction Only',
	 				 'Terminal Badar - Small Transaction Only', 'Terminal Badar - Large Transaction Only',
	 				 'Terminal Bahadurabad - Small Transaction Only', 'Terminal Bahadurabad - Large Transaction Only'
	 				]

	grand_totals = {"posting_date": f"<h3>Grand Totals</h3>", "pos_amount": 0.0, "so_amount":0.0, "tax_amount": 0.0, "grand_total": 0.0}
	branches = ["Gulshan", "Johar", "Badar", "Sehar", "North", "Bahadurabad"]
	if filters.get("branch"):
		branches = filter(lambda branch: branch == filters.get("branch"), branches)

	
	for branch in branches:
		if branch=="North":
			shop_profiles = ('Terminal North - Small Transaction Only', 'Terminal North - Large Transaction Only')
		if branch=="Johar":
			shop_profiles = ('Terminal Johar - Small Transaction Only', 'Terminal Johar - Large Transaction Only')
		if branch=="Gulshan":
			shop_profiles = ('Terminal Gulshan - Small Transaction Only', 'Terminal Gulshan - Large Transaction Only')
		if branch=="Sehar":
			shop_profiles = ('Terminal Sehar - Small Transaction Only', 'Terminal Sehar - Large Transaction Only')
		if branch=="Badar":
			shop_profiles = ('Terminal Badar - Small Transaction Only', 'Terminal Badar - Large Transaction Only')
		if branch=="Bahadurabad":
			shop_profiles = ('Terminal Bahadurabad - Small Transaction Only', 'Terminal Bahadurabad - Large Transaction Only')
		
		if branch=="North" and filters.get("pos_profile")=='Terminal North - Small Transaction Only':
			# shop_profiles = ('Terminal North - Small Transaction Only')
			shop_profiles = filter(lambda shop_profiles: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="North" and filters.get("pos_profile")=='Terminal North - Large Transaction Only':
			# shop_profiles = ('Terminal North - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Johar" and filters.get("pos_profile")=='Terminal Johar - Small Transaction Only':
			# shop_profiles = ('Terminal Johar - Small Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Johar" and filters.get("pos_profile")=='Terminal Johar - Large Transaction Only':
			# shop_profiles = ('Terminal Johar - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Gulshan" and filters.get("pos_profile")=='Terminal Gulshan - Small Transaction Only':
			# shop_profiles = ('Terminal Gulshan - Small Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Gulshan" and filters.get("pos_profile")=='Terminal Gulshan - Large Transaction Only':
			# shop_profiles = ('Terminal Gulshan - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Sehar" and filters.get("pos_profile")=='Terminal Sehar - Small Transaction Only':
			# shop_profiles = ('Terminal Sehar - Small Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)
		
		if branch=="Sehar" and filters.get("pos_profile")=='Terminal Sehar - Large Transaction Only':
			# shop_profiles = ('Terminal Sehar - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Badar" and filters.get("pos_profile")=='Terminal Badar - Small Transaction Only':
			# shop_profiles = ('Terminal Badar - Small Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Badar" and filters.get("pos_profile")=='Terminal Badar - Large Transaction Only':
			# shop_profiles = ('Terminal Badar - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)

		if branch=="Bahadurabad" and filters.get("pos_profile")=='Terminal Bahadurabad - Small Transaction Only':
			# shop_profiles = ('Terminal Bahadurabad - Small Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)
		
		if branch=="Bahadurabad" and filters.get("pos_profile")=='Terminal Bahadurabad - Large Transaction Only':
			# shop_profiles = ('Terminal Bahadurabad - Large Transaction Only')
			shop_profiles = filter(lambda shop: shop == filters.get("pos_profile"), shop_profiles)		
		
		branch_totals = {"posting_date": f"<h3 style='margin-left: 10px;'>{branch}</h3>", "pos_amount": 0.0, "so_amount":0.0, "tax_amount": 0.0, "grand_total": 0.0}

		for shop in shop_profiles:
			shop_row = {}
			data.append(shop_row)
			shop_totals = {"posting_date": f"<b style='margin-left: 15px;'>{shop}</b>", "pos_amount": 0.0, "so_amount":0.0, "tax_amount": 0.0, "grand_total": 0.0}
			pos_data = get_pos_data(filters, pos_conditions, shop)
			for pos in pos_data:
				pos_inv = {}
				pos_inv["posting_date"] = f"""<p style='margin-left: 20px;'>{pos.get("posting_date")}</p>"""
				pos_inv["pos_profile"] = pos.get("pos_profile")
				pos_inv["order_no"] = pos.get("name")
				pos_inv["transaction_type"] = "POS Invoice"
				# pos_inv["pos_amount"] = pos.get("net_total")
				pos_inv["pos_amount"] = pos.get("base_grand_total")
				# pos_inv["tax_amount"] = pos.get("total_taxes_and_charges")
				pos_inv["tax_amount"] = 0.0
				pos_inv["grand_total"] = pos.get("grand_total")
				pos_inv["status"] = pos.get("status")

				data.append(pos_inv)

				# shop_totals["pos_amount"] += float(pos.get("net_total"))
				shop_totals["pos_amount"] += float(pos.get("base_grand_total"))
				# shop_totals["tax_amount"] += float(pos.get("total_taxes_and_charges"))
				shop_totals["tax_amount"] += 0.0

			so_data = get_so_data(filters, so_conditions, shop)
			for order in so_data:
				so = {}
				so["posting_date"] = f"""<p style='margin-left: 20px;'>{order.get("transaction_date")}</p>"""
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
			
			branch_totals["pos_amount"] += shop_totals["pos_amount"] or 0.0
			branch_totals["so_amount"] += shop_totals["so_amount"] or 0.0
			branch_totals["tax_amount"] += shop_totals["tax_amount"] or 0.0
			branch_totals["grand_total"] += shop_totals["grand_total"]

			grand_totals["pos_amount"] += shop_totals["pos_amount"] or 0.0
			grand_totals["so_amount"] += shop_totals["so_amount"] or 0.0
			grand_totals["tax_amount"] += shop_totals["tax_amount"] or 0.0
			grand_totals["grand_total"] += shop_totals["grand_total"]
		data.append(branch_totals)
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
	if filters.get("branch")=="North":
		conditions += " and name in ('Terminal North - Small Transaction Only', 'Terminal North - Large Transaction Only')"
	if filters.get("branch")=="Johar":
		conditions += " and name in ('Terminal Johar - Small Transaction Only', 'Terminal Johar - Large Transaction Only')"
	if filters.get("branch")=="Gulshan":
		conditions += " and name in ('Terminal Gulshan - Small Transaction Only', 'Terminal Gulshan - Large Transaction Only')"
	if filters.get("branch")=="Sehar":
		conditions += " and name in ('Terminal Sehar - Small Transaction Only', 'Terminal Sehar - Large Transaction Only')"
	if filters.get("branch")=="Badar":
		conditions += " and name in ('Terminal Badar - Small Transaction Only', 'Terminal Badar - Large Transaction Only')"
	if filters.get("branch")=="Bahadurabad":
		conditions += " and name in ('Terminal Bahadurabad - Small Transaction Only', 'Terminal Bahadurabad - Large Transaction Only')"

	# if filters.get("branch")=="North" and filters.get("pos_profile")=='Terminal North - Small Transaction Only':
	# 	conditions += " and name = 'Terminal North - Small Transaction Only'"
	# if filters.get("branch")=="North" and filters.get("pos_profile")=='Terminal North - Large Transaction Only':
	# 	conditions += " and name = 'Terminal North - Large Transaction Only'"

	# if filters.get("branch")=="Johar" and filters.get("pos_profile")=='Terminal Johar - Small Transaction Only':
	# 	conditions += " and name = 'Terminal Johar - Small Transaction Only'"
	# if filters.get("branch")=="Johar" and filters.get("pos_profile")=='Terminal Johar - Large Transaction Only':
	# 	conditions += " and name = 'Terminal Johar - Large Transaction Only'"

	# if filters.get("branch")=="Gulshan" and filters.get("pos_profile")=='Terminal Gulshan - Small Transaction Only':
	# 	conditions += " and name = 'Terminal Gulshan - Small Transaction Only'"
	# if filters.get("branch")=="Gulshan" and filters.get("pos_profile")=='Terminal Gulshan - Large Transaction Only':
	# 	conditions += " and name = 'Terminal Gulshan - Large Transaction Only'"

	# if filters.get("branch")=="Sehar" and filters.get("pos_profile")=='Terminal Sehar - Small Transaction Only':
	# 	conditions += " and name = 'Terminal Sehar - Small Transaction Only'"
	# if filters.get("branch")=="Sehar" and filters.get("pos_profile")=='Terminal Sehar - Large Transaction Only':
	# 	conditions += " and name = 'Terminal Sehar - Large Transaction Only'"

	# if filters.get("branch")=="Badar" and filters.get("pos_profile")=='Terminal Badar - Small Transaction Only':
	# 	conditions += " and name = 'Terminal Badar - Small Transaction Only'"
	# if filters.get("branch")=="Badar" and filters.get("pos_profile")=='Terminal Badar - Large Transaction Only':
	# 	conditions += " and name = 'Terminal Badar - Large Transaction Only'"

	# if filters.get("branch")=="Bahadurabad" and filters.get("pos_profile")=='Terminal Bahadurabad - Small Transaction Only':
	# 	conditions += " and name = 'Terminal Bahadurabad - Small Transaction Only'"
	# if filters.get("branch")=="Bahadurabad" and filters.get("pos_profile")=='Terminal Bahadurabad - Large Transaction Only':
	# 	conditions += " and name = 'Terminal Bahadurabad - Large Transaction Only'"
	
	data = frappe.db.sql("""SELECT * FROM `tabPOS Profile` where disabled=0 {}""".format(conditions), as_dict=True)

	return data

def get_pos_data(filters, conditions, shop):

	# data = frappe.db.sql(""" select * from `tabPOS Invoice` 
	# 	where status not in ('Consolidated', 'Cancelled') and docstatus<2 and pos_profile='{}' {}""".format(shop, conditions), as_dict=True, debug=True)

	data = frappe.db.sql(""" SELECT posting_date, name, pos_profile, owner, base_grand_total, customer, is_return
		FROM
			`tabPOS Invoice`
		WHERE
			docstatus = 1 and pos_profile='{}' {}""".format(shop, conditions), as_dict=True, debug=True)

	return data

def get_so_data(filters, conditions, shop):

	data = frappe.db.sql(""" select * from `tabSales Order` where docstatus<=1 and pos_profile='{}' {}""".format(shop, conditions), as_dict=True, debug=True)

	return data

def get_pos_conditions(filters):
	conditions = ""
	if filters.get("start_date"):
		conditions += " and posting_date>='{}'".format(filters.get("start_date"))
	if filters.get("end_date"):
		conditions += " and posting_date<='{}'".format(filters.get("end_date"))
	if filters.get("branch")=="North":
		conditions += " and pos_profile in ('Terminal North - Small Transaction Only', 'Terminal North - Large Transaction Only')"
	if filters.get("branch")=="Johar":
		conditions += " and pos_profile in ('Terminal Johar - Small Transaction Only', 'Terminal Johar - Large Transaction Only')"
	if filters.get("branch")=="Gulshan":
		conditions += " and pos_profile in ('Terminal Gulshan - Small Transaction Only', 'Terminal Gulshan - Large Transaction Only')"
	if filters.get("branch")=="Sehar":
		conditions += " and pos_profile in ('Terminal Sehar - Small Transaction Only', 'Terminal Sehar - Large Transaction Only')"
	if filters.get("branch")=="Badar":
		conditions += " and pos_profile in ('Terminal Badar - Small Transaction Only', 'Terminal Badar - Large Transaction Only')"
	if filters.get("branch")=="Bahadurabad":
		conditions += " and pos_profile in ('Terminal Bahadurabad - Small Transaction Only', 'Terminal Bahadurabad - Large Transaction Only')"		
	
	return conditions

def get_so_conditions(filters):
	conditions = ""
	if filters.get("start_date"):
		conditions += " and transaction_date>='{}'".format(filters.get("start_date"))
	if filters.get("end_date"):
		conditions += " and transaction_date<='{}'".format(filters.get("end_date"))
	if filters.get("branch")=="North":
		conditions += " and pos_profile in ('Terminal North - Small Transaction Only', 'Terminal North - Large Transaction Only')"
	if filters.get("branch")=="Johar":
		conditions += " and pos_profile in ('Terminal Johar - Small Transaction Only', 'Terminal Johar - Large Transaction Only')"
	if filters.get("branch")=="Gulshan":
		conditions += " and pos_profile in ('Terminal Gulshan - Small Transaction Only', 'Terminal Gulshan - Large Transaction Only')"
	if filters.get("branch")=="Sehar":
		conditions += " and pos_profile in ('Terminal Sehar - Small Transaction Only', 'Terminal Sehar - Large Transaction Only')"
	if filters.get("branch")=="Badar":
		conditions += " and pos_profile in ('Terminal Badar - Small Transaction Only', 'Terminal Badar - Large Transaction Only')"
	if filters.get("branch")=="Bahadurabad":
		conditions += " and pos_profile in ('Terminal Bahadurabad - Small Transaction Only', 'Terminal Bahadurabad - Large Transaction Only')"
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
