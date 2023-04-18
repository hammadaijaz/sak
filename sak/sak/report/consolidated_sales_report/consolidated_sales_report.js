// Copyright (c) 2023, SRCA and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.require("assets/erpnext/js/financial_statements.js", function() {
frappe.query_reports["Consolidated Sales Report"] = {
	"filters": [
		{
			"fieldname": "start_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"width": 120,
			"default": frappe.datetime.month_start(),

		},
		{
			"fieldname": "end_date",
			"label": __("End Date"),
			"fieldtype": "Date",
			"width": 120,
			"default": frappe.datetime.month_end(),

		},
		{
			"fieldname": "branch",
			"label": "Branch",
			"fieldtype": "Select",
			"options": ["", "Gulshan", "Johar", "Badar", "Sehar", "North", "Bahadurabad"],
			"width": 120,
			"default": "",	
		},
		{
			"fieldname": "pos_profile",
			"label": "POS Profile",
			"fieldtype": "Link",
			"options": "POS Profile",
			"width": 120,	
		}
	],
	// "formatter": function (row, cell, value, columnDef, dataContext, default_formatter) {
    //     if (columnDef.df.fieldname == "posting_date") {
    //         value = dataContext.pos_profile;
    //         columnDef.df.is_tree = true;
    //     }

    //     value = default_formatter(row, cell, value, columnDef, dataContext);
    //     if (!dataContext.parent_account) {
    //         var $value = $(value).css("font-weight", "bold");
    //         if (dataContext.warn_if_negative && dataContext[columnDef.df.fieldname] < 0) {
    //             $value.addClass("text-danger");
    //         }

    //         value = $value.wrap("<p></p>").parent().html();
    //     }
    //     return value
    // },
    "tree": true,
    "name_field": "posting_date",
    "parent_field": "pos_profile",
    "initial_depth": 1
};
});