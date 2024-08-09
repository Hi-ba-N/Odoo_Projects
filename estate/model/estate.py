from datetime import timedelta

from odoo import models, fields

class Estate(models.Model):
	_name ="estate"
	name = fields.Char("Title")
	description = fields.Text("Description")
	postcode = fields.Char("Post code")
	date_availability=fields.Date("Available from",default=fields.Date.today()+timedelta(days=92),copy=False)
	expected_price=fields.Float("Expected Price")
	selling_price=fields.Float("Selling Price",readonly=True,copy=False)
	bedrooms = fields.Integer("Bedrooms", default='2')
	facades = fields.Integer("Facades")
	garage=fields.Boolean("Garage")
	living_area= fields.Integer("Living Area(sqm)")
	garden_orientation = fields.Selection(
		string='garden_orientation',
		selection=[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")]
	)
	active = fields.Boolean("Active")
	status = fields.Selection(
		string='Status',
		selection=[("new", "New"), ("offer recieved", "Offer Recieved"), ("offer Accepted", "offer Accepted"),
				   ("sold", "Sold"), ('cancelled', 'Cancelled')], required=True, copy=False, default="new"
	)
	garden_area = fields.Integer("Garden Area")









