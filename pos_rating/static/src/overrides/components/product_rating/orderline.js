/** @odoo-module */
console.log('order')
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";
patch(Orderline.prototype, {
getDisplayData(){
return{
...super.getDisplayData(),
product_rating: this.getProductRating(),
};
},
console.log(this)
getProductRating(){
return this.product.product_rating
}

})