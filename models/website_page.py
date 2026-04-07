from odoo import models, api

class WebsitePage(models.Model):
    _inherit = 'website.page'

    def get_full_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return f"{base_url}{self.website_url}"

    @api.model_create_multi
    def create(self, vals_list):
        print("Here, After Creating A Page ---------------------------------------->")
        record = super().create(vals_list)
        full_url = record.get_full_url()
        record.env['google.indexing.api'].notify_google(full_url, action='URL_UPDATED')
        print("Here, record ++++++========+++++++++++++++++++++=============>", record)
        
        return record

    def write(self, vals_list):
        res = super().write(vals_list)
        for rec in self:
            full_url = rec.get_full_url()
            rec.env['google.indexing.api'].notify_google(full_url, action='URL_UPDATED')
        return res

    def unlink(self):
        for rec in self:
            full_url = rec.get_full_url()
            rec.env['google.indexing.api'].notify_google(full_url, action='URL_DELETED')
        return super().unlink()
