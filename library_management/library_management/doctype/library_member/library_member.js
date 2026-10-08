frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        // Add button to create a new Library Membership linked to this member
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });

        // Add button to create a new Library Transaction linked to this member
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            });
        });
    }
});