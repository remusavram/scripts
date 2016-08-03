import unittest
import os
import tempfile
import io

from html_pages import HtmlPagesCoverter, FileAccessWrapper

class HtmlPagesTest(unittest.TestCase):
    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w")
        f.write("plain text\n")
        f.close()
        converter = HtmlPagesCoverter(FileAccessWrapper(filename))
        new_text = converter.get_html_page(0)
        self.assertEqual("plain text<br />", new_text)
    
    def test_quotes_esccaped(self):
        converter = HtmlPagesCoverter(FakeFileWrapper("test with 'quotes'"))
        new_text = convertor.get_html_page(0)
        self.assertEqual("text with &#x27;quotes&#x27;<br />", new_text)
        
    def test_random_access_pages(self):
        converter = HtmlPagesCoverter(FakeFileWrapper("page one \nPAGE_BREAK\npage two\n"))
        new_text = convertor.get_html_page(1)
        self.assertEqual("page tow<br />", page_two)
        

class FakeFileWrapper:
    def __init__(self, text):
        self.text = text
        
    def open(self):
        return io.StringIO(self.text)