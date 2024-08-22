/** @odoo-module **/

    import publicWidget from "@web/legacy/js/public/public_widget";


    publicWidget.registry.LeaveDaysCalculator = publicWidget.Widget.extend({
        selector: '#total',
        events: {
            'change #start_date, #end_date': '_onDatesChanged',
        },

        _onDatesChanged: function () {
            const startDate = new Date($('#start_date').val());
            const endDate = new Date($('#end_date').val());

            if (startDate && endDate) {
                let totalDays = this._calculateTotalDays(startDate, endDate);
                $('#total').val(totalDays);
            }
        },

        _calculateTotalDays: function (startDate, endDate) {
            let totalDays = 0;
            let currentDate = startDate;

            while (currentDate <= endDate) {
                const dayOfWeek = currentDate.getDay();

                if (dayOfWeek !== 0 && dayOfWeek !== 6) {
                    totalDays++;
                }

                currentDate.setDate(currentDate.getDate() + 1);
            }

            return totalDays;
        },
    });
});