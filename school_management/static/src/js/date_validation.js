/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.AgeCalculator = publicWidget.Widget.extend({
    selector: '.oe_student_website',
    events: {
        'change #dob': '_onDobChange',
    },

    _onDobChange: function (ev) {
        Console.log('work')
        const dobInput = $(ev.currentTarget);
        console.log(dobInput)
        const dob = new Date(dobInput.val());
        const today = new Date();


        let age = today.getFullYear() - dob.getFullYear();


        if (dob >= today) {
            alert("Choose a valid date");
            dobInput.val('');
            $('#age').val('');
        } else {
            $('#age').val(age);
        }
    },
});
