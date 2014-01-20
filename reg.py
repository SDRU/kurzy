import re
import urllib2
import sys

if len(sys.argv) == 1:
    print "Tento program vracia kurz zvolenej meny v korunach, argument sa zadava az po zavolani programu, napriklad reg.py USD"
    
else:

    def kurz(mena):
        html_content = urllib2.urlopen('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp').read()
        text = re.search(r'(?P<Mnozstvo>\d+)</td><td>' + mena + r'</td><td align="right">(?P<Kurz>\d+,\d+)</td>', html_content)
        if text == None:
            print "Mena " + sys.argv[1] + " nie je v zozname!"
        else:
            mnozstvo = float(text.group('Mnozstvo'))
            kurz = float(text.group('Kurz').replace(",", "."))
            return kurz/mnozstvo

    print kurz(sys.argv[1])

