import frappe



def get_user_details(user_id):
    return frappe.db.sql(f"""Select FROM tabUser where owner='Administrator';""", as_dict=True)