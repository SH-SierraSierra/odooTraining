# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Task(models.Model):
    _name = 'coop.task'
    _description = 'Coop Task Management'
    
    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Task Description', required=True)
    
    task_type = fields.Selection(string='Task Type', 
                                 selection=[('unloading', 'Unloading Product'),
                                           ('restocking', 'Restocking Product'),
                                           ('reshelving', 'Reshelving Product'),
                                           ('register', 'Working Cash Register'),
                                           ('inventory', 'Take inventory'),
                                           ('cleaning', 'Cleaning the Store'),
                                           ('other', 'Other')], copy=False)
    start_time = fields.Datetime(string='Start Time')
    stop_time = fields.Datetime(string='Stop Time')
    is_repeating_task = fields.Boolean(string='Repeating')
    repeating_type = fields.Selection(string='Task Interval', 
                                 selection=[('never', 'Never'),
                                           ('hourly', 'Hourly'),
                                           ('daily', 'Daily'),
                                           ('weekly', 'Weekly'),
                                           ('fortnightly', 'Fortnightly'),
                                           ('monthly', 'Monthly')], copy=False)
    state = fields.Selection(string='Task State', 
                             selection=[('draft', 'Draft'),
                                       ('ready', 'Ready'),
                                       ('in_progress', 'In Progress'),
                                       ('done', 'Done')], copy=False, default='draft')
    leader = fields.Char(string='Task Leader')
    
    @api.onchange('leader')
    def _onchange_leader(self):
        self.state = 'ready'
        
    @api.constrains('start_time', 'stop_time')
    def _check_start_time_stop_time(self):
        for record in self:
            if record.start_time > record.stop_time:
                raise ValidationError('Start time must be before stop time')