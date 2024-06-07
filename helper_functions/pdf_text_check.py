import fitz


def pdf_has_text(filepath):
    """
    Функция частично скопирована из https://medium.com/quantrium-tech/identifying-text-based-and-image-based-pdfs-using-python-10dba29a02b4
    """

    pdf = fitz.open(filepath)
    res = []
    
    for page in pdf:
        image_area = 0.0
        text_area = 0.0
        
        for b in page.get_text("blocks"):
            if "<image:" in b[4]:
                r = fitz.Rect(b[:4])
                image_area = image_area + abs(r)
            else:
                r = fitz.Rect(b[:4])
                text_area = text_area + abs(r)
        if text_area != 0.0:
            res.append(1)
        else:
            res.append(0)  

    return_value = res.count(0) / len(res)
    return return_value < 1
