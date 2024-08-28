/** @odoo-module */
console.log('dkjefkfh')
import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.ProductBoM = publicWidget.Widget.extend({
    selector: '.oe_website_sale',

//    events: {
//        'click .oe_cart': '_onCartClick',
//    },

//    _onCartClick: function (ev) {
        start:function(){
        this._super.apply(this,arguments);
        console.log('djs')
        this._getBomDetails();
},
        _getBomDetails:  function(){
        console.log('njdjd')
        const products = this.$el.find("#cart_products")
        console.log(products)

//        const productId = $(this.currentTarget).data('product-id');
//        console.log(productId)
//        if (productId) {
//            jsonrpc('/get_product_bom', { params: { product_id: productId } })
//             console.log('Result:', result);
//                .then(result => {
//                    if (result.bom_data && result.bom_data.length) {
//                        this._displayBoMData(productId, result.bom_data);
//                    }
//                });
//        }
    },

//    _displayBoMData: function (productId, bomData) {
//        const $bomContainer = $('<div/>', { class: 'product_bom_data' });
//
//        bomData.forEach(bom => {
//            $bomContainer.append(`
//                <div class="bom_item">
//                    <strong>Product:</strong> ${bom.name} <br>
//                    <strong>Quantity:</strong> ${bom.quantity}
//                </div>
//            `);
//        });
//
//        this.$el.find('.oe_cart_product[data-product-id="' + productId + '"] .product_name')
//            .after($bomContainer);
//    },

});

export default publicWidget.registry.ProductBoM;
