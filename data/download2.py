#import wget
import zipfile 
from urllib import request
downloads = [("https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5Cavall.zip", "avdataPost08.zip"),
	("https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5CPre2008.zip", "avdataPre08.zip")]

for url, filename in downloads:
#	wget.download(url, filename)
	request.urlretrieve(url, filename)

with zipfile.ZipFile("avdataPost08.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
with zipfile.ZipFile("avdataPre08.zip", 'r') as zip_ref:
    zip_ref.extractall(".")

