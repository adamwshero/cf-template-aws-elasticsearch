def get_log_config(log_level="DEBUG"):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime) %(filename) %(funcName) %(levelname) %(lineno) %(module) %(message) %(name) %(stack_info) %(pathname) %(process) %(processName) %(thread) %(threadName)',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'json',
                'stream': 'ext://sys.stdout'
            }
        },
        'loggers': {
            'root': {
                'level': log_level,
                'handlers': ['console']
            }
        }
    }
