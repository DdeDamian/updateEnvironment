from lxml import etree

#Lee el XMl y loc arga en el arbol
originalDocument = etree.parse ( 'test.xml' )

nombre = originalDocument.findall ( "Root/source/name" )
test = "come caca \n"

print (originalDocument.Root)

print nombre 
print test

#Crea el docuemnto y lo abre para escritura
outputDocument = open ( 'homemade.xml', 'w' )

#Escribe los cambios en el xml
originalDocument.write ( outputDocument )
