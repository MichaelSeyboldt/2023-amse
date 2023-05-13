#import wget
from urllib import request
downloads = [("https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_CA_A2-download.csv?__blob=publicationFile&v=2", "ca_a2.csv"),
	("https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_CA_A1-download.csv?__blob=publicationFile&v=1", "ca_a1.csv"),
	("https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_GA_B1-download.csv?__blob=publicationFile&v=1", "ga_b1.csv"),
	("https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_GA_B2-download.csv?__blob=publicationFile&v=2", "ga_b2.csv") ]

for url, filename in downloads:
#	wget.download(url, filename)
	request.urlretrieve(url, filename)

