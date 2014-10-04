from app import app
from config import config_path

app.config.from_object(config_path)

app.run(
    host='0.0.0.0',
    port=5000,
    debug=app.config['DEBUG']
)