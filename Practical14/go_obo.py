import datetime 
import matplotlib.pyplot as plt

import xml.dom.minidom
before_1=datetime.datetime.now()
#Get all the 'term' elements of go_obo.xml
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
#count the occurrences of each of the three ontology
molecular_function=0
biological_process=0
cellular_component=0
for element in terms:
	if element.getElementsByTagName('namespace')[0].firstChild.nodeValue=='molecular_function':
		molecular_function+=1
	elif element.getElementsByTagName('namespace')[0].firstChild.nodeValue=='biological_process':
		biological_process+=1
	elif element.getElementsByTagName('namespace')[0].firstChild.nodeValue=='cellular_component':
		cellular_component+=1
print(f'The number of GO terms within molecular function: {molecular_function}\n\
The number of GO terms within biological process: {biological_process}\n\
The number of GO terms within cellular components: {cellular_component}')
after_1=datetime.datetime.now()
#calculate the time taken
time_1=after_1-before_1
print(f'The time taken for DOM to complete the task: {time_1}')
#Generate a bar plot
Ontology = ['molecular function','biological process','cellular_component']
Frequency = [molecular_function,biological_process,cellular_component]
plt.bar(Ontology, Frequency, color=['steelblue'])
plt.xlabel('Ontology')
plt.ylabel('Frequency')
plt.title('The Frequency of GO Terms Within Each of the Three Ontology')
plt.show()
plt.clf()
 
import xml.sax
before_2=datetime.datetime.now()
#Define a custom ContentHandler
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.contentData = ""  
        self.molecular_function = 0
        self.biological_process = 0
        self.cellular_component = 0
    # Called when an element starts
    def startElement(self, tag, attributes):
        self.currentData = tag
        self.contentData = ""  
    # Called when an element ends
    def endElement(self, tag):
        if tag == "namespace":
            content = self.contentData.strip()
            if content == "molecular_function":
                self.molecular_function += 1
            elif content == "biological_process":
                self.biological_process += 1
            elif content == "cellular_component":
                self.cellular_component += 1
        self.currentData = ""
	#Ectract content
    def characters(self, content):
        if self.currentData == "namespace":
        	self.contentData += content
			
#Open the file go_obo.xml
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler=GOHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')
print(molecular_function)
print(f'The number of GO terms within molecular function: {Handler.molecular_function}\n\
The number of GO terms within biological process: {Handler.biological_process}\n\
The number of GO terms within cellular components: {Handler.cellular_component}')
after_2=datetime.datetime.now()
#calculate the time taken
time_2=after_2-before_2
print(f'The time taken for DOM to complete the task: {time_2}')
#Generate a bar plot
Ontology = ['molecular function','biological process','cellular_component']
Frequency = [Handler.molecular_function,Handler.biological_process,Handler.cellular_component]
plt.bar(Ontology, Frequency, color=['steelblue'])
plt.xlabel('Ontology')
plt.ylabel('Frequency')
plt.title('The Frequency of GO Terms Within Each of the Three Ontology')
plt.show()
plt.clf()
 
#Compare the time taken
if time_1<time_2:
	print("DOM API ran faster.")
else:
    print("SAX API ran faster.")
