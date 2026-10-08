frappe.query_reports["Library Membership Report"] = {
    "filters": [
        {
            "fieldname": "library_member",
            "label": __("Library Member"),
            "fieldtype": "Link",
            "options": "Library Member"
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "paid",
            "label": __("Paid Only"),
            "fieldtype": "Check"
        }
    ]
};
