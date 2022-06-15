import os
import shutil
import time

from const import AB_COPY, MSG_COPY, MSG_PATH, MSG_FILE, AB_PATH, AB_FILE


def copy(path, file_name, copy_name, copy_path=None):
    if not copy_path:
        copy_path = path
    shutil.copy(os.path.join(path, file_name), os.path.join(copy_path, copy_name))


def get_largest_dir(path):
    dir_wo = [d for d in os.listdir(path) if d != ".DS_Store"]
    if len(dir_wo) > 1:
        max_size = 0
        chosen_d = ""
        for d in dir_wo:
            size = 0
            for path, _, files in os.walk(os.path.join(path, d)):
                for f in files:
                    size += os.stat(os.path.join(path, f)).st_size
            if size > max_size:
                max_size = size
                chosen_d = d
    else:
        chosen_d = dir_wo[0]
    return chosen_d


def prepare_files():
    copy(MSG_PATH, MSG_FILE, MSG_COPY)
    ab_path = os.path.join(AB_PATH, get_largest_dir(AB_PATH))
    copy(ab_path, AB_FILE, AB_COPY, AB_PATH)


def load_status(start, df):
    print(
        f"{df.shape[0]:,} messages loaded successfully in {round(time.time() - start, 1)} seconds!"
    )
