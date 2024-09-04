/** @odoo-module */
console.log('order line patch')
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {

RemoveLine(){
//console.log('this',this)

       const currentOrder = this.env.services.pos.get_order();
//       const line =currentOrder.orderlines
         const line = currentOrder.orderlines.find((line)=>line.full_product_name==this.props.line.productName)
       console.log('current order',currentOrder)
//       console.log('line',line)
       console.log(this.props.line)

//       console.log(lines)
//       const selectedLine = currentOrder.get_selected_orderline();
                   currentOrder.removeOrderline(line)



       }





});