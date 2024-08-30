/** @odoo-module */
console.log('checkkk')
import { patch } from "@web/core/utils/patch";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
patch(ProductCard.prototype, {
setup(){
super.setup(...arguments)
           product_rating: this.get_ProductRating()

},
 getDisplayData() {
       return {
            ...super.getDisplayData(),
           product_rating: this.get_ProductRating()


       };
       },
              get_ProductRating(){

       return this.product.product_rating
       }


// getDisplayData() {
//       return {
//            ...super.getDisplayData(),
//           product_rating: this.get_ProductRating()
//       };
//        console.log('return')
//       },
//       get_ProductRating(){
//       console.log(this)
//       return "abc"
//       }



})