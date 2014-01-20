# Encoding: UTF-8

import re
import urllib2
import sys

if len(sys.argv) == 1:
    print "Tento program vracia kurz zvolenej meny v korunach, argument sa zadava az po zavolani programu, napriklad reg.py USD"
    
else:

    def kurz(mena):
        html_content = urllib2.urlopen('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp').read()
        # re.escape vsetky specialne znaky opatri lomitkom, aby sa nebrali ako regularne vyrazy
        text = re.search(r'<td>(?P<Stat>[^<]+)</td><td>(?P<Nazov_meny>[^<]+)</td><td align="right">(?P<Mnozstvo>\d+)</td><td>' + re.escape(mena) + r'</td><td align="right">(?P<Kurz>\d+,\d+)</td>', html_content)
        if text == None:
            print "Mena " + sys.argv[1] + " nie je v zozname!"
        else:
            stat = text.group('Stat')
            nazov_meny = text.group('Nazov_meny')
            mnozstvo = float(text.group('Mnozstvo'))
            kurz = float(text.group('Kurz').replace(",", "."))
            return '{stat}: {mnozstvo} {mena}({nazov_meny})={kurz} Kč'.format(stat=stat, mnozstvo=mnozstvo, mena=sys.argv[1].upper(), nazov_meny=nazov_meny, kurz=kurz)

    print kurz(sys.argv[1].upper())

