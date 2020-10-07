config = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'console': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }, 'file': {
        'class': 'app.logging.handlers.MakeDirTimedRotatingFileHandler',
        'filename': 'logs/app_log.log',
        'when': 'D',
        'interval': 1,
        'formatter': 'default',
        'backupCount': 15
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
}
