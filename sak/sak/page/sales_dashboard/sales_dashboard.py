import frappe
from frappe import _
import datetime
from frappe.utils import cstr, getdate, today
import json


@frappe.whitelist()
def get_sales_data(filters):
	if not filters:
		filters = {}
	filters = json.loads(filters)
	conditions = get_conditions(filters)

	data1 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-North" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data2 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-North Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data3 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-Gulshan" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data4 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS Terminal Gulshan Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data5 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-Sehar" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data6 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-Sehar Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data7 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-Badar" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data8 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS-Terminal-Badar Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data9 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS Terminal-Bahadurabad" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data10 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS Terminal Bhadrabad Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data11 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS Terminal - Johar" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)

	data12 = frappe.db.sql(""" SELECT is_pos, SUM(grand_total) FROM `tabSales Invoice`
		WHERE docstatus=1 AND pos_profile="POS Terminal Johar Without Tax" {} GROUP BY is_pos ORDER BY is_pos""".format(conditions), debug=False)


	

	datasets1 = []
	labels1 = []
	for d in data1:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels1.append(label)
		datasets1.append(d[1])

	datasets2 = []
	labels2 = []
	for d in data2:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels2.append(label)
		datasets2.append(d[1])

	datasets3 = []
	labels3 = []
	for d in data3:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels3.append(label)
		datasets3.append(d[1])

	datasets4 = []
	labels4 = []
	for d in data4:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels4.append(label)
		datasets4.append(d[1])

	datasets5 = []
	labels5 = []
	for d in data5:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels5.append(label)
		datasets5.append(d[1])

	datasets6 = []
	labels6 = []
	for d in data6:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels6.append(label)
		datasets6.append(d[1])

	datasets7 = []
	labels7 = []
	for d in data7:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels7.append(label)
		datasets7.append(d[1])

	datasets8 = []
	labels8 = []
	for d in data8:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels8.append(label)
		datasets8.append(d[1])

	datasets9 = []
	labels9 = []
	for d in data9:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels9.append(label)
		datasets9.append(d[1])

	datasets10 = []
	labels10 = []
	for d in data10:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels10.append(label)
		datasets10.append(d[1])

	datasets11 = []
	labels11 = []
	for d in data11:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels11.append(label)
		datasets11.append(d[1])

	datasets12 = []
	labels12 = []
	for d in data12:
		label = "Others"
		if d[0]==1:
			label = "POS"
		labels12.append(label)
		datasets12.append(d[1])
	return [{
			'labels': labels1,
			'datasets': [{'values': datasets1}]
			},
			{
			'labels': labels2,
			'datasets': [{'values': datasets2}]
			},
			{
			'labels': labels3,
			'datasets': [{'values': datasets3}]
			},
			{
			'labels': labels4,
			'datasets': [{'values': datasets4}]
			},
			{
			'labels': labels5,
			'datasets': [{'values': datasets5}]
			},
			{
			'labels': labels6,
			'datasets': [{'values': datasets6}]
			},
			{
			'labels': labels7,
			'datasets': [{'values': datasets7}]
			},
			{
			'labels': labels8,
			'datasets': [{'values': datasets8}]
			},
			{
			'labels': labels9,
			'datasets': [{'values': datasets9}]
			},
			{
			'labels': labels10,
			'datasets': [{'values': datasets10}]
			},
			{
			'labels': labels11,
			'datasets': [{'values': datasets11}]
			},
			{
			'labels': labels12,
			'datasets': [{'values': datasets12}]
			},
		]

def get_conditions(filters):
	conditions = ""
	if filters.get("period_group")=="Daily":
		conditions += " and posting_date = '{}'".format(today())
	if filters.get("period_group")=="Weekly":
		conditions += " and WEEK(posting_date)={}".format(datetime.date.today().isocalendar()[1])
	if filters.get("period_group")=="Monthly":
		conditions += " and MONTH(posting_date)={}".format(datetime.date.today().month)
	if filters.get("period_group")=="Yearly":
		conditions += " and YEAR(posting_date)={}".format(datetime.date.today().year)	
	return conditions
