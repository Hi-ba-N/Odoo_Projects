
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    specialization = fields.Many2many('hospital.specialization', string="Specialization")



 # WHERE sl.start_date >= %s AND sl.end_date <= %s
# <div class="backtosnippet">
# <a href="/" class="reverse_link">Back</a>
# </div>



    # @http.route(['/room/<int:id>'], type='http', auth='user', website=True)
    # def get_room_data(self, **post):
    #     room = (request.env['hostel.room'].
    #             browse(post.get('id')))
    #     return request.render('hostel_management.room_data_snippet',
    #                          {'room':room})

#     / **
#
#     @odoo - module * /
#
#     import publicWidget
#     from
#     "@web/legacy/js/public/public_widget";
#     import
#     {jsonrpc}
#     from
#     "@web/core/network/rpc_service";
#
#     publicWidget.registry.ProductBoM = publicWidget.Widget.extend({
#         selector: '.oe_website_sale',
#
#         start: function() {
#             this._super.apply(this, arguments);
#     console.log('Widget initialized');
#     this._getBomDetails();
#     },
#
#     _getBomDetails: function()
#     {
#         console.log('Fetching BoM details');
#     // Find
#     all
#     products in the
#     cart
#     const $products = this.$el.find("#cart_products .product");
#
#     // Iterate
#     over
#     each
#     product and fetch
#     its
#     BoM
#     $products.each((index, element) = > {
#         const
#     productId = $(element).data('product-id'); // Get
#     product
#     ID
#     from the element
#     if (productId) {
#     jsonrpc('/get_product_bom', {params: {product_id: productId}})
#     .then(result= > {
#     if (result.bom_data & & result.bom_data.length)
#     {
#         this._displayBoMData(productId, result.bom_data, $(element));
#     }
#     });
#     }
#     });
#     },
#
#     _displayBoMData: function(productId, bomData, $productElement) {
#         const $bomContainer = $('<div/>', {
#
#     class: 'product_bom_data'
#
#     });
#     console.log('Displaying BoM data for product ID:', productId);
#
#     bomData.forEach(bom= > {
#     $bomContainer.append(`
#                          < div
#
#     class ="bom_item" >
#
#     < strong > Product: < / strong > ${bom.name} < br >
#     < strong > Quantity: < / strong > ${bom.quantity}
#
# < / div >
# `);
# });
#
# // Append
# BoM
# data
# after
# the
# product
# description in the
# cart
# $productElement.find('.product_description').after($bomContainer);
# },
# });
#
# export
# default
# publicWidget.registry.ProductBoM;
