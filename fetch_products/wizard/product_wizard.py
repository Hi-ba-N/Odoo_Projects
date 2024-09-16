# coding: utf-8
from odoo import models
import xmlrpc.client


class ProductWizard(models.TransientModel):
    """This model is used for """
    _name = 'product.wizard'
    _description = "Product Wizard"

    def action_fetch_product(self):
        print('hello')
        url_db1 = "http://cybrosys:8016/"
        db_1 = 'odoo16'
        username_db_1 = 'odoo16'
        password_db_1 = 'cool'
        common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
        print(common_1)
        models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
        print(models_1)
        version_db1 = common_1.version()
        print(version_db1)

        url_db2 = "http://cybrosys:8017/"
        db_2 = 'db1'
        username_db_2 = 'odoo17'
        password_db_2 = 'cool'
        common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
        models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))
        version_db2 = common_2.version()

        uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
        print(uid_db1)
        uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})
        print(uid_db2)
