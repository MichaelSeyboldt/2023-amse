.PHONY: clean

all: de.sqlite us.sqlite

%.csv:
	python3 download1.py

%.mdb:
	python3 download2.py

de.sqlite: ca_a1.csv  ca_a2.csv  ga_b1.csv  ga_b2.csv
	python3 convert1.py

us.sqlite: avall.mdb Pre2008.mdb
	python3 convert2.py

evaluate: de.sqlite us.sqlite
	python3 evaluate.py

clean:
	rm -f *.csv *.mdb *.sqlite *.zip
