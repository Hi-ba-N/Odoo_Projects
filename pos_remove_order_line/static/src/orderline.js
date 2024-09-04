/** @odoo-module */
console.log('order line patch')
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {

RemoveLine(){

       const currentOrder = this.env.services.pos.get_order();
       console.log(currentOrder)
       console.log('this line name: ',this.props.line.productName)
       console.log('orderline',currentOrder.orderlines.find((line)=>line.full_product_name))
       const line = currentOrder.orderlines.find((line)=>line.full_product_name==this.props.line.productName)
       currentOrder.removeOrderline(line)


        }





});





















