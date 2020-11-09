# Wikidata Search Program


**Description**

The program is aimed to provide the ability to search in Wikidata database for sensors that are used in smart fisheries. The program has the flexibility to search by item ID and
keywords. Also, it has an option for listing items that are instance of a sensor (Q167676). The program will display the following information for the searched item, which are the item id, label, description, picture (If available), and aliases (If available).

The program uses the SPARQL data service from qwikidata python package. SPARQL is an RDF query language. Wikidata provides an SPARQL endpoint that allows programs to interact with the database.

**Required Libraries**

* *qwikidata.sparql* – A python package that allows you to interact with Wikidata
* *pandas* – A python package that provide data structures for data analysis, time series, and statistics


**Run Instructions**

1. Run the main.py in your favorite python editor or via the command line by typing python main.py
2. Choose one of the options by typing the number of that option, e.g. 1, 2, 3, or 4. Below are the options:
* Option 1: Search by a keyword in the description of items in Wikidata database
* Option 2: Search by item id
* Option 3: List items that are instance of a sensor
* Option 4: Exit
3. Then, provide a word or an item ID (e.g. Q167676)if you chose option 1 or 2
4. The output will be saved as a csv file called results.csv
