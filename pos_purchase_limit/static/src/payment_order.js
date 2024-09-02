/** @odoo-module */
console.log(' check')
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";

patch(Order.prototype, {
async pay() {
console.log(this)
if (!this.partner) {
  this.env.services.popup.add(ErrorPopup, {
                title: _t("No Customer"),
                body: _t("Select a Customer."),
            });
        }
        else {
        console.log(this.partner.name)
        const limit = this.partner.purchase_limit
        console.log('limit',limit)
        const customer = this.partner.activate_purchase_limit
        console.log(customer)
        console.log('total',this.get_total_with_tax())
         if (customer==true && this.get_total_with_tax() > limit){
           this.env.services.popup.add(ErrorPopup, {
                title: _t("Purchase Limit"),
                body: _t("Purchase Limit Amount %s Exceeded.",limit),
            });
          }
          else{
          return super.pay(...arguments);
          }



 }
}






})

