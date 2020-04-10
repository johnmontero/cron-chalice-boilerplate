# Core imports
# Core imports
import os
from chalice import Chalice, Rate

# App level imports
from chalicelib.utils.config import get_config_env
from chalicelib.utils.exceptions import ExceptionHandler

# Main
app = Chalice(app_name='schedule-chalice-boilerplate')
app.debug = eval(os.getenv('DEBUG'))


@app.schedule(Rate(2, unit=Rate.MINUTES))
def handler(event):
    app.log.info('=== Iniciando Schedule Chalice Boilerplate ===')
    try:
        app.log.info('Procesando Tareas...')
    except Exception as e:
        app.log.info(f'{e}')

    app.log.info('=== Finalizando Schedule Chalice Boilerplate ===')