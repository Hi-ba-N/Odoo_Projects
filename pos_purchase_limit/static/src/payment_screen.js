/** @odoo-module */
//console.log('checkkk thisssss')
import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
     async _processData(loadedData) {
        await super._processData(...arguments);
//        console.log('loaded data',loadedData)
        }
});



