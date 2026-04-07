from odoo import models, api, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_indexing_json_key = fields.Binary("Google JSON Key File")

    def set_values(self):
        super().set_values()
        config = self.env['ir.config_parameter'].sudo()

        if self.google_indexing_json_key:
            config.set_param('google_indexing_pages.json_key_binary', self.google_indexing_json_key)

    @api.model
    def get_values(self):
        res = super().get_values()
        config = self.env['ir.config_parameter'].sudo()
        res.update(
            google_indexing_json_key=config.get_param('google_indexing_pages.json_key_binary'),
        )
        return res
