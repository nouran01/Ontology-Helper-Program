from qwikidata.sparql import (get_subclasses_of_item,return_sparql_query_results)
import pandas as pd

def searchByKeyword(keyword):
##        Search by a keyword ID (e.g. sensor )
##
##        Returns:
##        The query response as a dictionary 
        
        sparql_query = """
        SELECT ?item ?itemLabel ?itemDescription ?article ?part
        (GROUP_CONCAT(DISTINCT ?alias; separator=" | ") as ?aliases) WHERE{
        ?item ?label "%s"@en.  
        ?article schema:about ?item .
        ?article schema:inLanguage "en" .
        ?article schema:isPartOf <https://en.wikipedia.org/>. 
        OPTIONAL {?item skos:altLabel ?alias FILTER (LANG (?alias) = "en")}
        OPTIONAL
        { ?item  wdt:P361  ?part}
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }    
        } GROUP BY ?item ?itemLabel ?itemDescription ?article ?part
        """%keyword
        response = return_sparql_query_results(sparql_query)
        return response

def searchByID(itemID):
##        Search by an item ID (e.g. Q167676 )
##
##        Returns:
##        The query response as a dictionary 
        
        
        sparql_query = """
        SELECT  ?item ?itemLabel ?itemDescription ?partOf ?image  ?article (GROUP_CONCAT(DISTINCT ?alias; separator=" | ") as ?aliases)
        WHERE
        { ?article schema:about ?item;
                   schema:inLanguage "en";
                   schema:isPartOf <https://en.wikipedia.org/>
        BIND(wd:%s AS ?item)
        OPTIONAL {?item skos:altLabel ?alias FILTER (LANG (?alias) = "en")}
        OPTIONAL { ?item  wdt:P18  ?image }
        OPTIONAL { ?item  wdt:P361  ?partOf}
        SERVICE wikibase:label
                 { bd:serviceParam
                   wikibase:language  "en"
                 }
         }
        GROUP BY ?item ?itemLabel ?itemDescription  ?partOf ?image ?article
        """%itemID
        response = return_sparql_query_results(sparql_query)
        return response
        
def listSensorItems():
##        List items that are instance of a sensor (Q167676)
##
##        Returns:
##        The query response as a dictionary 
        
        
	sparql_query = """
        SELECT ?sensor ?sensorLabel ?sensorDescription ?img
        WHERE {
             ?sensor wdt:P31 wd:Q167676.
             OPTIONAL{?sensor wdt:P18 ?img}
             SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
              }
        """
	response = return_sparql_query_results(sparql_query)
	return response

def save(file,data):
        """
        This method saves the output of a sparql query to csv file
        """
        cols = data['head']['vars']
        out = []
        for row in data['results']['bindings']:
                item = []
                for c in cols:
                    item.append(row.get(c, {}).get('value'))
                out.append(item)
        df = pd.DataFrame(out, columns=cols)
        df.to_csv("{}.csv".format(file),index=False)

def main():
        print("Ontology Helper")
        while True:
                print("\nProgram options: \n 1.Search by a keyword \n 2.Search by item id \n 3.List items that are instance of a sensor \n 4.Exit\n ")
                option = input("Please choose an option:")
                valid_input = ["1","2","3","4"]
                while option not in valid_input:
                        print("Please enter a valid option!")
                        option = input("Please choose an option:")
                
                if option =="1":
                        keyword = input("Please enter a keyword to search:")
                        output = searchByKeyword(keyword)
                        print("Saving search results..")
                        save("results",output)
                        print("The file has been exported!")

                elif option =="2":
                        itemID = input("Please enter an item ID to lookup:")
                        output = searchByID(itemID)
                        print("Saving search results..")
                        save("results",output)
                        print("The file has been exported!")
                        
                elif option =="3":
                        output = listSensorItems()
                        print("Saving search results..")
                        save("results",output)
                        print("The file has been exported!")
                else:
                        break

if __name__ == "__main__":
    main()



