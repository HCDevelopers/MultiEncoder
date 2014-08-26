import os


def get_encryptions():
    filelst = [item[:-3] for item in os.listdir(os.path.join(os.path.dirname(__file__))) if not item.endswith(".pyc")]
    return sorted(filelst)[1:]