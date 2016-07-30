import errno
import os


def ensure_dir(path):
    """os.makedirs without EEXIST."""
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def package_dir():
    return os.path.normpath(os.path.join(__file__, '..', '..', '..'))
