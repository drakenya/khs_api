from app import app as application
from config import config_path

application.config.from_object(config_path)

if __name__ == "__main__":
  application.run(
    host='0.0.0.0',
    port=5000,
    debug=application.config['DEBUG']
  )
