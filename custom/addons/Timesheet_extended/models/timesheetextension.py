from odoo import api, fields, models

class HrTimesheetSheet(models.Model):
	_inherit = "hr_timesheet_sheet.sheet"
	
   
	company_address = fields.Char("companyAddress", default=False)

	