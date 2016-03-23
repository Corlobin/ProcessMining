from xml.dom.minidom import parse
import xml.dom.minidom

def findTextNodes(nodeList):
  for subnode in nodeList:
    if subnode.nodeType == subnode.ELEMENT_NODE:
      print "element node: " + subnode.tagName

      # call function again to get children
      findTextNodes(subnode.childNodes)

    elif subnode.nodeType == subnode.TEXT_NODE:
      return subnode.data
 
 
def main():
	dicFrequencias = {}
	DOMTree = xml.dom.minidom.parse("ex1.mxml")
	collection = DOMTree.documentElement
	if collection.hasAttribute("description"):
		print "Descricao: %s" % collection.getAttribute("description")
	tarefas = collection.getElementsByTagName("ProcessInstance")

	for tarefa in tarefas:
		print "** Tarefa **";
		print tarefa.getAttribute("id")
		for elemento in tarefa.getElementsByTagName('WorkflowModelElement'):
			texto = findTextNodes(elemento.childNodes)
			if not (texto in dicFrequencias):
				dicFrequencias[texto] = 0
			else:
				dicFrequencias[texto] += 1
	print dicFrequencias
main();