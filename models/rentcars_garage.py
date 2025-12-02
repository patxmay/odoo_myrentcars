# -*- coding: utf-8 -*-
from odoo import models, fields, api

# modèle « Garage » qui permet de  stocker des informations sur des emplacements.Chaque véhicule est garé dans un garage.

class Garage(models.Model):
    _name = 'rentcars.garage'
    _description = 'A garage is a location for vehicle'

    # champs qui constituent la classe
    name = fields.Char("Nom")
    active=fields.Boolean("Actif ?", default=True)
    address_street = fields.Char("Adresse")
    address_zipcode = fields.Char("Code postal")
    address_city = fields.Char("Ville")
    places_max = fields.Integer("Nombre de places")

    # Relation garage/vehicle
    vehicle_ids = fields.One2many("rentcars.vehicle","garage_id",string="Parc de véhicules")
    
    # related
    # vehicle_cover=fields.Binary(related="vehicle_id.thumbnail", string="vehicle_cover")
    