from PIL import Image
from PIL.ExifTags import TAGS
from helper_functions.convert_to_datetime import convert_to_timestamp


class ImgPadawan:
    
    def __init__(self):
        self._common = False
        self._ex = ["apng", "avif", "gif", "jpg", "jpeg", "jfif",
                    "pjpeg", "pjp", "png", "svg", "webp", "bmp",
                    "ico", "cur", "tif", "tiff"]
        self._error_log = {}
        self._image = None

    def load_img(self, path):
        try:
            self._image = Image.open(path)
        except:
            pass

    @property
    def error_log(self):
        return self._error_log
        
    def get_exif(self):
        try:
            exif = {}
            exif_data = self._image.getexif()
            for tag_id in exif_data:
                tag = TAGS.get(tag_id, tag_id)
                data = exif_data.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                exif[tag] = data
            exif.pop("ImageWidth", None)
            exif.pop("ImageLength", None)
            if exif:
                return exif
            else:
                return None
        except:
            pass
    
    def get_meta_inf(self, path):
        meta = {}
        try:
            self.load_img(path)
            meta["image_size"] = f"{self._image.width}x{self._image.height}"
            meta["image_height"] = self._image.height
            meta["image_width"] = self._image.width
            meta["image_format"] = self._image.format
            meta["image_mode"] = self._image.mode
            exif = self.get_exif()
            if exif:
                try:
                    meta["exif"] = str(exif)
                    meta["exif_make"] = exif.get("Make")
                    meta["exif_model"] = exif.get("Model")
                    meta["exif_software"] = exif.get("Software")
                    meta["exif_orientation"] = exif.get("Orientation")
                    meta["exif_datetime"] = convert_to_timestamp(exif.get("DateTime"))
                    meta["exif_artist"] = exif.get("Artist")
                    meta["exif_copyright"] = exif.get("Copyright")
                    meta["exif_hostcomputer"] = exif.get("HostComputer")
                except Exception as e:
                    pass
        except Exception as e:
            with open("log_file.txt", "a") as f:
                f.write(f"Error | img | {path} | {e}\n")

        return meta