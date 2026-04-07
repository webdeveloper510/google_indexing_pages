from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging
import base64
import tempfile
import os
from odoo import models, api

_logger = logging.getLogger(__name__)

class GoogleIndexingApi(models.Model):
    _name = 'google.indexing.api'
    _description = 'Google Indexing API Helper'

    @api.model
    def notify_google(self, url, action='URL_UPDATED'):
        try:
            config = self.env['ir.config_parameter'].sudo()
            key_data = config.get_param('google_indexing_pages.json_key_binary')
            key_filename = config.get_param('google_indexing_pages.json_key_filename')

            if not key_data or not key_filename:
                _logger.warning("Google Indexing: JSON key file not configured.")
                return

            temp_path = os.path.join(tempfile.gettempdir(), key_filename)
            with open(temp_path, 'wb') as f:
                f.write(base64.b64decode(key_data))

            credentials = service_account.Credentials.from_service_account_file(
                temp_path,
                scopes=['https://www.googleapis.com/auth/indexing']
            )
            service = build('indexing', 'v3', credentials=credentials)
            body = {'url': url, 'type': action}
            response = service.urlNotifications().publish(body=body).execute()
            _logger.info("Google Indexing API notified: %s", response)

        except Exception as e:
            _logger.error("Error notifying Google Indexing API: %s", e)

