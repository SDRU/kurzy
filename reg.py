import re
import urllib2
import sys

def kurz(mena):
    html_content = urllib2.urlopen('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp').read()
    text = re.search(r'(\d+)</td><td>' + mena + r'</td><td align="right">(\d+,\d+)</td>', html_content)
    mnozstvo = float(text.group(1))
    kurz = float(text.group(2).replace(",", "."))
    return kurz/mnozstvo

print kurz(sys.argv[1])

