from bs4 import BeautifulSoup as BS
import re


class HTMLPadawan:
    
    def __init__(self) -> None:
        self._common = False
        self._ex = ["html", "htm"]
        self._soup = None
    
    @property
    def error_log(self):
        return self._error_log 

    def parse_site(self, path):
        try:
            with open(path) as f:
                self._soup = BS(f, "html.parser")
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | html | {path} | {e}\n")

    def get_meta_inf(self, path):
        meta = {}
        self.parse_site(path)
        text = None
        if self._soup:
            try:
                text = re.sub(r"\n+", r"\n", self._soup.get_text())
            except Exception as e:
                with open("log_file.txt", "a") as f:
                    f.write(f"Error | html | {path} | {e}\n")
            try:
                meta["html_code"] = self._soup.prettify()
            except Exception as e:
                with open("log_file.txt", "a") as f:
                    f.write(f"Error | html | {path} | {e}\n")
            try:
                meta["text"] = text
            except Exception as e:
                with open("log_file.txt", "a") as f:
                    f.write(f"Error | html | {path} | {e}\n")
            
        return meta