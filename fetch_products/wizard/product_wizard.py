# coding: utf-8
from odoo import fields, models
import xmlrpc.client

from odoo.addons.base.controllers.rpc import RPC_FAULT_CODE_WARNING
from odoo.exceptions import ValidationError


class ProductWizard(models.TransientModel):
    """This model is used for creating wizard """
    _name = 'product.wizard'
    _description = "Product Wizard"

    url_db1 = fields.Char('From URL')
    db_1 = fields.Char("DB Name")
    username_db_1 = fields.Char('Username')
    password_db_1 = fields.Char('Password')

    url_db2 = fields.Char('Current DB URL',
                          default=lambda self: self.get_base_url(),
                          readonly=True)
    db_2 = fields.Char(" Current DB Name",
                       default=lambda self: self.env.cr.dbname, readonly=True)
    username_db_2 = fields.Char('Current DB Username',
                                default=lambda self: self.env.user.login,
                                readonly=True)

    def action_fetch_product(self):
        """ Action to fetch Products from Odoo 16 instance"""
        try:
            common_1 = xmlrpc.client.ServerProxy(
                '{}/xmlrpc/2/common'.format(self.url_db1))
            models_1 = xmlrpc.client.ServerProxy(
                '{}/xmlrpc/2/object'.format(self.url_db1))
            password_db_2 = 'abc'
            common_2 = xmlrpc.client.ServerProxy(
                '{}/xmlrpc/2/common'.format(self.url_db2))
            models_2 = xmlrpc.client.ServerProxy(
                '{}/xmlrpc/2/object'.format(self.url_db2))
            uid_db1 = common_1.authenticate(self.db_1, self.username_db_1,
                                            self.password_db_1, {})
            print(uid_db1)
            uid_db2 = common_2.authenticate(self.db_2, self.username_db_2,
                                            password_db_2, {})
            print(uid_db2)
            if not uid_db1:
                raise ValidationError(
                    "Credentials are not valid")
            # db_1_products = models_1.execute_kw(self.db_1, uid_db1, self.password_db_1,
            #                                     'product.template', 'search_read',
            #                                     [[]], {
            #                                         'fields': ['id', 'name'
            #                                                    ]})
            # print(db_1_products)
            #
            # for product in db_1_products:
            #     new_products = models_2.execute_kw(self.db_2, uid_db2, password_db_2,
            #                                        'product.template',
            #                                        'create',
            #                                        [[product]])
            #     print(new_products)
        except xmlrpc.client.Fault as e:
            print(e)
            raise ValidationError(
                e.faultString)








        # all_id = models_2.execute_kw(db_2, uid_db2, password_db_2,
        #                              'product.template', 'search', [[]])
        # print(all_id)
        # for product in all_id:
        #     models_2.execute_kw(db_2, uid_db2, password_db_2, 'product.template',
        #                         'unlink',
        #                         [[product]])
