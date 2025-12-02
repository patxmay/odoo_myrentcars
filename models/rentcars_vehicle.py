# -*- coding: utf-8 -*-
from odoo import models, fields, api
# import de re pour RegularExpression et
# le module de gesiton des exceptions 
import re
from odoo.exceptions import ValidationError
# champ calcule
from datetime import date
from dateutil.relativedelta import relativedelta

class Vehicle(models.Model):
    
  _name = 'rentcars.vehicle'
  _description = 'Description of vehicle'
    
  active = fields.Boolean("Actif ?", default=True)
  immatriculation = fields.Char("Plaque minéralogique")
  date_purchased = fields.Date(string="Date d'achat")
  model = fields.Char("Modele")
  marque = fields.Char("Marque")
  age_vehicle=fields.Integer(compute="_age_vehicle", string="Age of vehicle (years)")
  
  thumbnail = fields.Binary("Thumbnail")

  # Relation vehicle/garage (cours3/Ex2)
  garage_id = fields.Many2one("rentcars.garage", string="Garage")
  
  # Relation Many2Many Vehicle/Option
  option_ids = fields.Many2many("rentcars.option",string="Options de vehicule" )
  
  # Cours 4 Paragrahe 1
  state = fields.Selection([('broken', 'En panne'),('repair', 'En cours de réparation'),('use', 'Utilisable')])
  
  broken_state = fields.Char(string='En cours de réparation', default='En cours de réparation')
  repair_state = fields.Char(string='En panne', default='En panne')
  use_state = fields.Char(string='Utilisable', default='Utilisable')
  
  # -------------------------------------------
  # controle plaque immat
  # -------------------------------------------
  def _check_immatriculation(self):
    # immat :  AA-123-AA
    self.ensure_one()  # vérifie que quel self contient 1 seul record.
    pattern=re.compile('^[A-Z]{2}-\d{3}-[A-Z]{2}$')
    return pattern.match(self.immatriculation)

  def button_check_immatriculation(self):
    for vehicle in self:
       if not vehicle.immatriculation:
        raise (ValidationError("Merci de renseigner la plaque d'immatriculation de votre véhicule"))
       if vehicle.immatriculation and not vehicle._check_immatriculation():
        raise ValidationError("La plaque d'immatriculation %s est invalide" % (vehicle.immatriculation))
    # comment utilser la concatenation avec python https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
    return True

  def action_set_use(self):
    return self.write({'state': 'use'})

  def action_set_repair(self):
    return self.write({'state': 'repair'})

  def action_set_broke(self):
    return self.write({'state': 'broken'})

  # -------------------------------------------
  # age vehicule
  # -------------------------------------------
  @api.depends('date_purchased')
  def _age_vehicle(self):
    for vehicle in self:
      TODAY = date.today()
      vehicle.age_vehicle = relativedelta(TODAY,vehicle.date_purchased).years


