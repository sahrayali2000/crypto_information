from django.apps import AppConfig


class CryptoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto'

    def ready(self):
        from webscraping import updater
        from asset_info import crypto_updater
        updater.start()
        crypto_updater.start()
