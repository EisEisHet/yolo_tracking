__version__ = '10.0.12'

from pathlib import Path

from boxmot.strongsort.strong_sort import StrongSORT
from boxmot.ocsort.ocsort import OCSort as OCSORT
from boxmot.bytetrack.byte_tracker import BYTETracker
from boxmot.botsort.bot_sort import BoTSORT
from boxmot.deepocsort.ocsort import OCSort as DeepOCSORT
from boxmot.deep.reid_multibackend import ReIDDetectMultiBackend

from boxmot.tracker_zoo import create_tracker, get_tracker_config


__all__ = '__version__',\
          'StrongSORT', 'OCSORT', 'BYTETracker', 'BoTSORT', 'DeepOCSORT'
