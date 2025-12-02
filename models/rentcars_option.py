# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Nous allons créer un modèle « option », qui permet de stocker des informations sur les véhicules :
# est-ce que le véhicule a une boîte automatique, un radar de recul, un gps intégré, etc ...

class Option(models.Model):
    _name = 'rentcars.option'
    _description = 'Options de véhicule'
    
    # champs qui constituent la classe
    active=fields.Boolean("Actif ?", default=True)
    name = fields.Char("Name")
    category = fields.Selection([("security", "Sécurité"), ("confort", "Confort"), ("aestheticism", "Estéthique")])
    description= fields.Char("Description")

    # Relation Many2Many Vehicle/Option
    vehicle_ids = fields.Many2many("rentcars.vehicle",string="Véhicule avec option")

