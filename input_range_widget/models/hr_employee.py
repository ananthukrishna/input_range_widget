from odoo import models, fields, api, exceptions, _, SUPERUSER_ID
import datetime
from dateutil.relativedelta import relativedelta

class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    input_range = fields.Integer(string='Input Range',default=0)    