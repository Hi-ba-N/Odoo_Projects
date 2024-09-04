/** @odoo-module */
console.log('Hello')
import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
export class ClearButton extends Component {
    static template = "pos_remove_order_line.ClearButton";
    setup() {
        this.pos = usePos();
    }
    click() {
       this.removeAllLine(false)
       console.log('remove all line')
    }
    removeAllLine(single){
//       console.log(single)
       const currentOrder = this.pos.get_order();
       const lines = currentOrder.get_orderlines();
       const selectedLine = currentOrder.get_selected_orderline();
       if (lines.length){
            if(!single){
                 lines.filter(line => line.get_product()).
                 forEach(line => currentOrder.removeOrderline(line));
            }
            else {
            currentOrder.removeOrderline(selectedLine)
            }

       }
       else{
                this.pos.popup.add(ErrorPopup, {
                title: _t("No Items"),
                body: _t("No Items to Remove"),
                });
       }

    }
   Onclick(){
      this.removeAllLine(true)
      console.log('single line remove')

    }
}
ProductScreen.addControlButton({ component: ClearButton });
































//    const currentOrder = this.pos.get_order();
//    const lines = currentOrder.get_orderlines();
//    const selectedLine = currentOrder.get_selected_orderline();
//    if (lines.length){
//const line = currentOrder.orderlines.find((line)=>line.full_product_name==this.props.line.productName)