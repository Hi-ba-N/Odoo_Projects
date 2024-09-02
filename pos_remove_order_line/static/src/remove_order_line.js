/** @odoo-module */
console.log('Hello')
import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
export class ClearButton extends Component {
    static template = "pos_remove_order_line.ClearButton";
    setup() {
        this.pos = usePos();
    }
    async click() {
    console.log('button click')
    }
}
ProductScreen.addControlButton({ component: ClearButton });
