.PHONY: clean

all: us.sqlite de.sqlite

%.csv:
	python3 download1.py

avall.mdb:
	python3 download2.py

de.sqlite: ca_a1.csv  ca_a2.csv  ga_b1.csv  ga_b2.csv
	python3 convert1.py

us.sqlite: avall.mdb
	python3 convert2.py

all: us.sqlite de.sqlite

clean:
	rm -f *.csv *.mdb *.sqlite
