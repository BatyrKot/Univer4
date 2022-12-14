import re
import urllib.request

tel_nums = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()

pattern = r'(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta ' \
          r'org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span ' \
          r'class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt ' \
          r'class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd ' \
          r'class=\"spec__value\"[^\w]*>|<p>[^\w]*)([^<]*\b) '

match = re.findall(pattern, tel_nums)
print(match)