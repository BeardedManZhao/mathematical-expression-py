import logging
# import os
import sys
from datetime import datetime

now = datetime.now()
# if not os.path.exists('./logs'):
#     os.mkdir('./logs')
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info("+============================== Welcome to [mathematical expression] ==============================+")
logging.info("+ \tStart time " + str(now))
logging.info("+ \tCalculation component manager initialized successfully")
logging.info("+ \tFor more information, see: https://github.com/BeardedManZhao/mathematical-expression-py")
logging.info("+--------------------------------------------------------------------------------------------------+")
