from celery import shared_task
from celery.utils.log import get_task_logger

from base.models import Scan

import time

logger = get_task_logger(__name__)

@shared_task
def perform_scan(scan_id):
    time.sleep(2)

    assert scan_id and type(scan_id) == int, "Provided Scan id '{}' is not valid.".format(scan_id) 

    try:
        new_scan = Scan.objects.get(pk=scan_id)
    except:
        assert False, "Provided Scan with id #{} do not exist.".format(scan_id)

    try:
        # Execute the scan using the shodAND-scanner
        pass
    except:
        new_scan.state = "pending"
        new_scan.error = True
        new_scan.save()
        assert False, "Changes can't be saved for #{}.".format(scan_id)

    time.sleep(5)
    new_scan.state = "done"
    new_scan.error = False
    new_scan.result = "Sample result asdkajdasdjasdlj"

    new_scan.save()

    logger.info(scan_id)
    print("job done! [{} {}]".format(scan_id, "host"))
    return "job done! [{} {}]".format(scan_id, "host")
