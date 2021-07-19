from datetime import datetime
from helpers import common_strings
from helpers.mongo_connection import db

# in v1 we do not do status returns if something is in progress for port scan as ePlace doesn't expect that, so once we
# have completed results we store them in database for a later retrieval, that's why we have an upsert=True argument
def v1_port_scan_db_addition(value, output):
    db.portScan.find_one_and_update({common_strings.strings['mongo_value']: value},
                                    {'$set': {'status': common_strings.strings['status_finished'],
                                              'timeStamp': datetime.utcnow(), 'output': output}}, upsert=True)