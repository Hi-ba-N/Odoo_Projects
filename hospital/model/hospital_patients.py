from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    age = fields.Integer("Age")
    blood_group = fields.Selection(
        string='Blood Group',
        selection=[("A+ve", "A +ve"), ("A-ve", "A-ve"), ("O+ve", "O+ve"), ("O-ve", "O-ve")])
    sequence = fields.Char("Sequence")
    gender = fields.Selection(
        string='Gender',
        selection=[("female", "Female"), ("male", "Male")])
    dob = fields.Date("DOB")


 #    import models, fields
 #    class ResConfigSettings(models.TransientModel):
 #
 #    _inherit = 'res.config.settings'
 # my_boolean_field = fields.Boolean(string="My Boolean Field",
 #                                          config_parameter='my_module.my_boolean_field')
 #
 #
 #    def set_values(self):
 #
 # super(ResConfigSettings, self).set_values(self.env[
 #        'ir.config_parameter'].set_param('my_module.my_boolean_field',
 #                                         self.my_boolean_field)
 #
 #
 #    @api.model
 #
 #
 #
 #    def get_values(self):
 #
 #     res = super(ResConfigSettings,
 #                      self).get_values() res.update(my_boolean_field =
 #    self.env['ir.config_parameter'].get_param('my_module.my_boolean_field',
 #                                              default=False),return res