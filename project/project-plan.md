# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes the location, severity and prevalence of  aircraft incidents and accidents in civil and commertial avaiation.
It shall visualize those informations on one or multiple maps.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps visualizing where, how offten and how severe different accidents in the aviation industry are. Ths may or may not help persons who are nervous about flying with their fear, or may shine ligth on some hotspots of incidents. 


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Bundesstelle für Flugunfalluntersuchung
* Metadata URL: https://mobilithek.info/offers/-5593625849824107584
* Data URL: https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_CA_A2-download.csv
* Data URL: https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_GA_B2-download.csv
* Data URL: https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_GA_A1-download.csv
* Data URL: https://www.bfu-web.de/DE/Publikationen/OpenData/Tabelle_GA_B1-download.csv
* Data Type: CSV

accidents and severe aviation incidents in Germany from 1998 to 2010 and from 2011 to 2022 

### Datasource2: NTSB
* Metadata URL: https://data.ntsb.gov/avdata
* Data URL: https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5Cavall.zip
* Data URL: https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5CPre2008.zip
* Data Type: mdb 

accidents and severe aviation incidents in the USA from 1982 to 2008 and from 2008

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

- [ ] #1  Import and merging pipeline  Datasource1 
- [ ] #2
3. Make src1 and 2 comparable
4. Check for discontinuities or other problems
5. Visualise Data on a Map
6. Visualise Hotspots and other interesting corelations
7. Add CI
8. Deploy to GH pages


