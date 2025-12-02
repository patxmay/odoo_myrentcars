# -*- coding: utf-8 -*-
from odoo import http

class Vehicles(http.Controller):
    @http.route("/rentcars/allvehicles", type='http', auth='public', website=True)
    def list(self, **kwargs) :
        vehicle=http.request.env["rentcars.vehicle"]
        vehicles=vehicle.search([])
        return http.request.render("rentcars.vehicle_list_template",{"vehicles":vehicles})

    @http.route("/rentcars/allvehicles/<model('rentcars.vehicle'):vehicle>", type='http', auth="public", website=True)
    def detail(self, vehicle):
        return http.request.render("rentcars.vehicle_detail_template", {"vehicle": vehicle})
    