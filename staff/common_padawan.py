import os
import time
from helper_functions.humanize_size import humanize_size
import pathlib


class CommonPadawan:

    def __init__(self):
        self._common = True

    @property
    def error_log(self):
        return self._error_log

    def get_common_meta_inf(self, path):
        meta = {}
        try:
            meta["size"] = os.path.getsize(path)
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | common | {path} | {e}\n")
        try:
            meta["size_h"] = humanize_size(meta["size"])
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | common | {path} | {e}\n")
        try:
            meta["creation_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.ctime(os.stat(path).st_birthtime))
        except Exception as e:
            pass
        try:
            meta["modification_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.ctime(os.path.getmtime(path)))
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | common | {path} | {e}\n")
        try:
            meta["ext"] = pathlib.Path(path).suffix[1:].lower()
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | common | {path} | {e}\n")
        return meta