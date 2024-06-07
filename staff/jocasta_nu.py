import pathlib


class JocastaNu:
    
    def __init__(self):
        self._common_padawan = None
        self._padawans = {}
        self._total_padawans = []
    
    def add_padawan(self, *padawans):
        for padawan in padawans:
            if padawan._common:
                self._common_padawan = padawan
                self._total_padawans.append(padawan)
            else:
                exs = padawan._ex
                for ex in exs:
                    self._padawans[ex] = padawan
                self._total_padawans.append(padawan)
    
    @property
    def padawans(self):
        return self._total_padawans

    def common_meta(self, path):
        common_meta_dict = {}
        if self._common_padawan:
            results = self._common_padawan.get_common_meta_inf(path)
            common_meta_dict.update(results)
        return common_meta_dict
    
    def get_meta_inf(self, path):
        meta_dict = {}
        ex = pathlib.Path(path).suffix[1:].lower()
        if ex in self._padawans:
            results = self._padawans[ex].get_meta_inf(path)
            meta_dict.update(results)
        return meta_dict
    
    def get_meta(self, path):
        meta = {}
        meta.update(self.common_meta(path))
        meta.update(self.get_meta_inf(path))
        return meta