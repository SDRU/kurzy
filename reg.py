import re
import urllib2

def kurz(mena):
    html_content = urllib2.urlopen('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.jsp').read()

    #print html_content
    
    return re.search('<td>' + mena + r'</td><td align="right">(\d+,\d+)</td>', html_content).group(1)


print kurz('USD')



