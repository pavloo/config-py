from config_py.lib import import_config


import_config(globals(), package='my_module.', env_var='WSGI_ENV')
