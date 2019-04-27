"""Misc funcs
"""

import time
import logging

LOGGER = logging.getLogger("time")
LOGGER.setLevel(logging.DEBUG)

def timeit(f):
    """ Times function
    """
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        minutes_taken = (te - ts) / 60
        LOGGER.info(f"Completed {f.__name__} in {minutes_taken:.1} minutes")
        return result

    return timed
