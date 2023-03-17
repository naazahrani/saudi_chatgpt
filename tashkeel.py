from farasa.diacratizer import FarasaDiacritizer

tashkeela = FarasaDiacritizer()

def tashkeel(text):
    text = tashkeela.diacritize(text)
    return text

