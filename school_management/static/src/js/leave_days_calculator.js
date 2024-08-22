/** @odoo-module **/

    import publicWidget from "@web/legacy/js/public/public_widget";
    console.log('leave ')
    publicWidget.registry.LeaveDaysCalculator = publicWidget.Widget.extend({
        selector: '.oe_leave_form',
        events: {
            'change #start_date, #end_date': '_onDatesChanged',
        },

        _onDatesChanged: function (ev) {
           console.log('date change')
            const startDate = new Date($('#start_date').val());
            const endDate = new Date($('#end_date').val());
              if (startDate && endDate) {
              if(startDate<=endDate){
              total= this._calculateTotalDays(startDate,endDate)
              console.log('total',total)
              console.log(this.$el.find('#total'))
              this.$el.find('#total').val(total)
}
else{
    alert("Choose a valid date");}

        }
        },

        _calculateTotalDays: function (startDate, endDate) {
          console.log('function')
            let totalDays = 0;
            let currentDate = startDate;


            while (currentDate <= endDate) {
                const dayOfWeek = currentDate.getDay();
                console.log(dayOfWeek)
                if (dayOfWeek != 0 && dayOfWeek != 6) {
                console.log('if')
                    totalDays++;
                    console.log(totalDays)


                }

             currentDate.setDate(currentDate.getDate() + 1);
            }
//            console.log(this.$el.find('#total'))
//            this.$el.find('#total').val(totalDays)
          return totalDays


        },
});
