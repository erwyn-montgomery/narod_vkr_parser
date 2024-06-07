import fitz
from helper_functions.pdf_text_check import pdf_has_text


class PDFPadawan:

    def __init__(self):
        self._common = False
        self._ex = ["pdf"]
        self._doc = None
        self._error_log = {}

    def load_doc(self, path):
        try:
            self._doc = fitz.open(path)
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | pdf | {path} | {e}\n")

    @property
    def doc(self):
        return self._doc
    
    @property
    def error_log(self):
        return self._error_log
    
    def get_doc_text(self):
        text = ""
        try:
            for page in self.doc:
                text += page.get_text()
            text = f"'{text}'"
            return text
        except Exception as e:
            pass

    def get_meta_inf(self, path):
        meta = {}
        self.load_doc(path)
        try:
            doc_data = self.doc.metadata
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | pdf | {path} | {e}\n")
        if self.doc:
            if doc_data["title"]:
                meta["title"] = doc_data["title"]
            if doc_data["author"]:
                meta["author"] = doc_data["author"]
            meta["page_count"] = self.doc.page_count
            if pdf_has_text(path):
                meta["text_layer"] = True
                try:
                    meta["text"] = self.get_doc_text()
                except Exception as e:
                    with open("log_file.txt", "a") as f:
                        f.write(f"Error | pdf | {path} | {e}\n")
                try:
                    meta["char_count"] = len(meta["text"])
                except Exception as e:
                    with open("log_file.txt", "a") as f:
                        f.write(f"Error | pdf | {path} | {e}\n")
                try:
                    meta["word_count"] = len(meta["text"].split())
                except Exception as e:
                    with open("log_file.txt", "a") as f:
                        f.write(f"Error | pdf | {path} | {e}\n")
            else:
                meta["text_layer"] = False
        return meta