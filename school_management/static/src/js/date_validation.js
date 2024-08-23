/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";
publicWidget.registry.AgeCalculator = publicWidget.Widget.extend({
    selector: '.oe_student_website',
    events: {
        'change #dob': '_onDobChange',
    },

    _onDobChange: function (ev) {
//        console.log('work')
        const dobInput = $(ev.currentTarget);
        console.log('input',dobInput)
        const dob = new Date(dobInput.val());
        console.log('dob',dob)
        const today = new Date();


        let age = today.getFullYear() - dob.getFullYear();
         console.log('age',age)

        if (dob >= today) {
            console.log('if')
            alert("Choose a valid date");
            dobInput.val('');
            $('#age').val('');
        } else {
            console.log('elseeee')

//            console.log(this.$el.find('#ages'))
            this.$el.find('#ages').val(age)

//            $('#age').val(age);
        }
    },
});
