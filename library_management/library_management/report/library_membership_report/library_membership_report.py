import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": "Membership ID",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Library Membership",
            "width": 150
        },
        {
            "label": "Member ID",
            "fieldname": "library_member",
            "fieldtype": "Link",
            "options": "Library Member",
            "width": 140
        },
        {
            "label": "Full Name",
            "fieldname": "full_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "From Date",
            "fieldname": "from_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "To Date",
            "fieldname": "to_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Paid",
            "fieldname": "paid",
            "fieldtype": "Check",
            "width": 80
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 110
        }
    ]

def get_data(filters):
    conditions = {}

    if filters.get("library_member"):
        conditions["library_member"] = filters.get("library_member")

    if filters.get("paid"):
        conditions["paid"] = filters.get("paid")

    if filters.get("from_date"):
        conditions["from_date"] = [">=", filters.get("from_date")]

    if filters.get("to_date"):
        conditions["to_date"] = ["<=", filters.get("to_date")]

    records = frappe.db.get_all(
        "Library Membership",
        fields=["name", "library_member", "full_name", "from_date", "to_date", "paid", "docstatus"],
        filters=conditions,
        order_by="creation desc"
    )

    # Map numeric docstatus to readable status names
    status_map = {0: "Draft", 1: "Submitted", 2: "Cancelled"}
    for row in records:
        row["status"] = status_map.get(row.docstatus, "Draft")

    return records