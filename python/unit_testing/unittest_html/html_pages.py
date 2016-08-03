import html as html_convertor

class FileAccessWrapper:
    def __init__(self, filename):
        self.filename = filename
        
    def open(self):
        return open(self.filename, "r")
    

class HtmlPagesCoverter:
    
    def __init__(self, file_access):
        """Read the file and note the positions of the page breaks
        so we can access them."""
        self.file_access = file_access
        self.breaks = [0]
        with self.file_access.open() as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    page_break_position = t.tell()
                    self.breaks.append(f.tell())
            self.breaks.append(f.tell())
            
    def get_html_page(self, page):
        """Return html page with the givem number (zero indexed)"""
        page_start = self.breaks[page]
        page_end = self.breaks[page+1]
        html = ""
        with self.file_access.open() as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                html += html_convertor.escape(line, quote=True)
                html += "<br />"
        return html
            
        