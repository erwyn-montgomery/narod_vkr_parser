from helper_functions.walking_files import walking_files
import time
import psycopg2
import re


class Collector:
    def __init__(self):
        self._cols = ["file_id", "size", "size_h", "modification_date", "html_code", "title", "author", "page_count",
                      "text_layer", "text", "char_count", "word_count", "rows", "columns",
                      "slides_count", "image_height", "image_width", "image_format", "image_mode", "exif",
                      "exif_make", "exif_model", "exif_software", "exif_orientation", "exif_datetime",
                      "exif_artist", "exif_copyright", "exif_hostcomputer"]
        self._archivarius = None
        self._data_list = []
        self.con = None
        self.cur = None
        self._file_ptrn = re.compile(r"file_\d+_\d+_(\d+)\.?")
    
    @property
    def archivarius(self):
        return self._archivarius
    
    @archivarius.setter
    def archivarius(self, a):
        self._archivarius = a

    def connect_to_db(self, dbname, user, password, host="localhost", port="5432"):
        """
        Функция для коннекта к БД.
        """
        self.con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.con.cursor()

    def commit_db(self, close_db=False):
        """
        Функция для коммита и закрытия БД.
        """
        if self.cur:
            self.con.commit()
        if self.con and close_db:
            self.con.close()

    def parse_file_id(self, path):
        result = re.search(self._file_ptrn, path).group(1)
        return result

    def collect_and_save_data(self, path):
        if self._archivarius:
            with open("collect_log.txt", "a") as f:
                cur_time = time.localtime()
                cur_time = time.strftime("%Y-%m-%d %H:%M:%S", cur_time)
                f.write(f"Beginning collecting at {cur_time}\n\n")
            query_add = "INSERT INTO file_meta_info ( \
                file_id, size, size_h, modification_date, html_code, title, author, page_count, \
                text_layer, text, char_count, word_count, rows, columns, slides_count, \
                image_height, image_width, image_format, image_mode, exif, \
                exif_make, exif_model, exif_software, exif_orientation, exif_datetime, \
                exif_artist, exif_copyright, exif_hostcomputer \
                ) VALUES (%s);" % ", ".join(list(["%s"]*len(self._cols)))
            for f, p in walking_files(path):
                try:
                    file_id = self.parse_file_id(f)
                    local_dict = {"file_id": file_id, "filename": f, "filepath": p}
                    local_dict.update(self._archivarius.get_meta(p))
                    local_list = [local_dict.get(el, None) for el in self._cols]
                    self.cur.execute(query_add, local_list)
                    self.commit_db()
                    loc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    with open("collect_log.txt", "a") as f:
                        f.write(f"Success | collecting | {p} | {loc_time}\n")
                except Exception as e:
                    self.con.rollback()
                    loc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    with open("collect_log.txt", "a") as f:
                        f.write(f"Error | collecting | {p} | {loc_time} | {e}\n")
            
