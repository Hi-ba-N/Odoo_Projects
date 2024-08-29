/** @odoo-module */
console.log('checkkk')
import { patch } from "@web/core/utils/patch";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
patch(ProductCard.prototype, {
//     async _processData(loadedData) {
//        await super._processData(...arguments);
//            console.log(loadedData)
//
//    },


 getDisplayData() {
       return {
            ...super.getDisplayData(),
           product_rating: this.get_product().product_rating,
       };

       }
//        console.log(loadedData)
});