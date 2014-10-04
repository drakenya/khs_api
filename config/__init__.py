import os

environment = os.getenv('ENVIRONMENT', 'local')
config_path = 'config.%s' % environment