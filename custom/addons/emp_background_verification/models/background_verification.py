# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,RedirectWarning, ValidationError



class ReferralCategory(models.Model):
	_name = 'referral_category.referral_category'
	_rec_name = 'ref_category_name'

	ref_category_name = fields.Char(string="Referral Category Name", )



class reference_check_list(models.Model):
	_name = 'referral_check_list.referral_check_list'
	_rec_name = 'ref_check_name'
	

	ref_check_name = fields.Char(string="Reference Check Name",)
	reference_category = fields.Many2one('referral_category.referral_category',string ="Reference Category",)
	country_id = fields.Many2one('res.country', string='Country')

class emp_background_verification(models.Model):
	_name = 'emp_verification.emp_verification'
	
	graduation = fields.One2many('graduation.graduation','parent_id1',string="Graduation details" ,)
	passport_details = fields.One2many('passport.details','parent_id',string="Passport/Visa",)
	# postgraduation = fields.One2many('post_graduation.post_graduation','parent_id2',string="Post Graduation details")
	employment_details_id = fields.One2many(comodel_name='employment.details', inverse_name='parent_id', string='Employment Details Id',)
	employee_id = fields.Many2one('hr.employee',string="Employees", default=lambda self: self.env.user)
	ref_check_list = fields.Many2one('referral_category.referral_category', string="Reference check name")
	emp_reference_category = fields.Many2one('referral_check_list.referral_check_list', string="Reference check list")
	user_id = fields.Many2one('res.users', string="Users")
	#Address fields
	checklist = fields.Many2one('referral_check_list.referral_check_list',string="Residence check list")
	house_number = fields.Char(string="House number")
	address_line1 = fields.Text(string="Address Line1")
	address_line2 = fields.Text(string="Address Line2")
	state = fields.Many2one('res.country.state', string='State')
	country = fields.Many2one('res.country', string='Country')
	upload_file = fields.Binary(string="Upload File")
	file_name = fields.Char(string="File Name")


	was_an_employee = fields.Boolean('Previously worked in a company?')
	check_residence = fields.Boolean('To enter residence details,check the box',readonly=True,default=True)
	check_academic = fields.Boolean('To enter academic details,check the box',readonly=True,default=True)
	passport_check = fields.Boolean('To enter passport details,check the box')
		 
	sequence = fields.Integer(default=1)

	stage_id = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'),
							   ('verification', 'Verification'), ('approved', 'Approved')], string='Status',track_visibility='always', default='draft')


	@api.multi
	def action_confirm(self):
		for ver in self:
			if  ver.was_an_employee and ver.check_residence and ver.check_academic and ver.passport_check:
				if ver.graduation and ver.employment_details_id:
					self.stage_id = 'submitted'
				elif not ver.graduation:
					raise UserError(('Academic details are not filled'))
				if not ver.employment_details_id:
					raise UserError(('Employment details are not filled'))
	
	@api.onchange('file_name')
	def onchange_file_name(self):
		if self.file_name:
			fname = self.file_name
			temp = fname.split('.')
			ext = temp[-1]
			if ext not in ['pdf']:
				raise UserError(('File not in pdf'))

	
	# @api.one
	# def action_confirm(self):
	# 	for verification in self:
	# 		# print 'verification.house_number', verification.house_number
	# 		if not verification.house_number:
	# 			raise UserError(_('House number is empty'))
	# 	self.stage_id = 'submitted'

	# @api.onchange('house_number')
	# def onchange_house_number(self):
	# 	if not self.house_number:
	# 			warning_msg = {
	# 				'values': {'house_number':self.house_number},
	# 				'warning': {
	# 					'title': 'Validation Error',
	# 					'message': 'House number cannot be empty'
	# 				}
	# 			}
	# 			return warning_msg


class educational_qualification(models.Model):
	_name = 'graduation.graduation'

	parent_id1 = fields.Many2one('emp_verification.emp_verification',string="Graduation  details")
	university = fields.Char(string="University/Board",)
	year_of_passing = fields.Char(string="Year of passing", )
	college_name = fields.Char(string="College Name", )
	roll_no = fields.Char(string="University Seat Number", )
	college_address = fields.Char(string="College Address",)
	percentage = fields.Integer(string="Percentage/CGPA",)
	upload_file = fields.Binary(string="Upload File")
	file_name = fields.Char(string="File Name")


# class qualification_postgraduation(models.Model):
# 	_name = 'post_graduation.post_graduation'

# 	parent_id2 = fields.Many2one('emp_verification.emp_verification',string="Qualification")
# 	university = fields.Char(string="University/Board")
# 	year_of_passing = fields.Char(string="Year of passing", )
# 	college_name = fields.Char(string="College Name", )
# 	roll_no = fields.Char(string="University Seat Number", )
# 	college_address = fields.Char(string="College Address",)
# 	percentage = fields.Integer(string="Percentage/CGPA",)
# 	upload_file = fields.Binary(string="Upload File")
# 	file_name = fields.Char(string="File Name")


class EmploymentDetails(models.Model):
	_name = 'employment.details'

	parent_id = fields.Many2one('emp_verification.emp_verification', string='Previous employer details')
	emp_checklist = fields.Many2one('referral_check_list.referral_check_list',string='Previous employer details')
	# no_of_previous_employers = fields.Many2one('referral_check_list.referral_check_list',string="No of previous employers")
	company_address = fields.Char(string="Company Address")
	designation = fields.Many2one('hr.job', string="Designation")
	ctc = fields.Integer(string="CTC")
	date_of_joining = fields.Date(string="Date of joining")
	date_of_relieving = fields.Date(string="Date of relieving")
	reason = fields.Text(string='Reason for resignation')
	upload_letter = fields.Binary(string="Upload relieving letter")
	file_name1 = fields.Char(string="Upload relieving letter")

class PassportDetails(models.Model):
	_name = 'passport.details'
	
	parent_id = fields.Many2one('emp_verification.emp_verification', string='Passport/Visa')
	date_of_issue = fields.Date(string="Date of issue") 
	date_of_expiry = fields.Date(string="Date of Expiry")  