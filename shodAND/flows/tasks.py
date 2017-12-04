from celery import shared_task
from celery.utils.log import get_task_logger

from base.models import Scan

import time

logger = get_task_logger(__name__)

@shared_task
def perform_scan(host, ports):
    #assert 
    new_scan = Scan(host=host, ports=ports)
    time.sleep(5)
    logger.info(host, ports)
    print("job done! [{} {}]".format(host, ports))
    return "job done! [{} {}]".format(host, ports)
