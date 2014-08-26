import os


def get_encodings():
    filelst = [item[:-3] for item in os.listdir(os.path.join(os.path.dirname(__file__))) if not item.endswith(".pyc")]
    return sorted(filelst)[1:]