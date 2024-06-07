import sys
import os

sys.path = [os.getcwd()] + sys.path

from staff.collector import Collector
from staff.jocasta_nu import JocastaNu
from staff.common_padawan import CommonPadawan
from staff.img_padawan import ImgPadawan
from staff.pdf_padawan import PDFPadawan
from staff.ms_padawans import *
from staff.html_padawan import HTMLPadawan


def get_database(filepath, dbname, user, password):
    try:
        my_collector = Collector()
        my_archivarius = JocastaNu()
        common = CommonPadawan()
        img = ImgPadawan()
        pdf = PDFPadawan()
        word = WordPadawan()
        excel = ExcelPadawan()
        ppt = PPtPadawan()
        html = HTMLPadawan()

        my_archivarius.add_padawan(common, img, pdf, word, excel, ppt, html)
        my_collector.archivarius = my_archivarius

        my_collector.connect_to_db(dbname=dbname, user=user, password=password)
        my_collector.collect_and_save_data(filepath)
        my_collector.commit_db(close_db=True)
    
    except Exception as e:
        with open("global_collect_log.txt", "w") as f:
            f.write(f"Error at collecting: {e}")


if __name__ == "__main__":
    get_database("/Users/ilias/Desktop/ADA/Thesis/narod/files",
                 dbname="narod_pg_small_sample",
                 user="narod_user",
                 password="*****")