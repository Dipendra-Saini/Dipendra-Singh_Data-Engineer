"""
In this file, I have give basic configuration to logging and
provided the format to content that save into my log file
"""

import os
import logging

formatter = "%(asctime)s : %(levelname)s : %(module)s : %(message)s"
logging.basicConfig(filename="D:\\#PD\\DLTINS_20210117_01of01\\project\\mylog.log",
                    level=logging.DEBUG,
                    format=formatter)
log = logging.getLogger()

# print(log.level)
