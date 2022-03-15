import sys
from bs4 import BeautifulSoup
with open(sys.argv[1]) as f:
    print(BeautifulSoup(f.read(), 'html.parser').prettify())

