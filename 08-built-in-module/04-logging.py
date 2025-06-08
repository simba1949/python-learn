import logging

# 配置日志 logging.basicConfig()
# level=logging.DEBUG：配置日志级别
# filename='log/example.log' 配置日志文件
# filemode='a' 配置日志文件追加模式
# format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' 配置日志格式
logging.basicConfig(level=logging.WARNING, filename='log/example.log', encoding='utf-8', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
log.debug("This is a debug message")
log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")
log.critical("This is a critical message")
