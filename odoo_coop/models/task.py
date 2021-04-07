# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'coop.task'
    _description = 'Coop Task Management'
    
    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Task Description', required=True)