/** @odoo-module */
console.log('order line patch')
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {

RemoveLine(){
//console.log('this',this)

       const currentOrder = this.env.services.pos.get_order();
//       const line =currentOrder.orderlines

       console.log('current order',currentOrder)
/
//       console.log(lines)
//       const selectedLine = currentOrder.get_selected_orderline();
//                   currentOrder.removeOrderline(line)



       }





});