from celery import shared_task
from celery.utils.log import get_task_logger

from viewflow.flow import flow_job

logger = get_task_logger(__name__)

@shared_task
@flow_job
def perform_scan(command):
    #assert 
    logger.info(command)
    print("job done! [{}]".format(command))
    return "job done! [{}]".format(command)
