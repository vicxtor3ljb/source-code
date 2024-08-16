# https://www.listendata.com/2024/01/4-ways-to-correct-grammar-with-python.html

"""
pip install pyaspeller
"""

from pyaspeller import YandexSpeller
def error_correct_pyspeller(sample_text):
    speller = YandexSpeller()
    fixed = speller.spelled(sample_text)
    return fixed

mytext = """I is testng grammar tool using python. It does not costt anythng."""
output_text = error_correct_pyspeller(mytext)
print(output_text)

