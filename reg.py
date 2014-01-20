import re
import urllib2
import sys

def kurz(mena):
    html_content = urllib2.urlopen('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp').read()
    text = re.search(r'(?P<Mnozstvo>\d+)</td><td>' + mena + r'</td><td align="right">(?P<Kurz>\d+,\d+)</td>', html_content)
    mnozstvo = float(text.group('Mnozstvo'))
    kurz = float(text.group('Kurz').replace(",", "."))
    return kurz/mnozstvo

print kurz(sys.argv[1])

