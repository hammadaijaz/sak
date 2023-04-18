import frappe

@frappe.whitelist()
def count_late_days(employee_name):
    employee_logs = frappe.db.get_all("Attendance", filters={'employee': employee_name}, fields=['status'])

    number_of_late_days = 0
    for record in employee_logs:
        if record == 'Present':
            number_of_late_days = number_of_late_days + 1
    return number_of_late_days    
 
 