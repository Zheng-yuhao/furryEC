import logging

# 这里会取到dev.py下的配置中的loggers下的django
log = logging.getLogger('django')
# log主要是给exception用 → 因为报错必然会被exception捕捉到(除了严重的没有被捕捉到的错误)
