import frappe


@frappe.whitelist()
def get_employee_details(com):
    # return  frappe.db.sql(f"""SELECT name,first_name FROM `tabEmployee` where owner='Administrator'""", as_dict =True )
	emp=frappe.db.get_list('Employee',
		filters={
			'company_name': {com}
		},
		fields=['name', 'first_name'],
		order_by='name desc',
		start=10,
		page_length=20,
		as_list=True
	)
	return emp
