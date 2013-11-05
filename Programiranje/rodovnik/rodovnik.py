import xml.dom.minidom
def izpis(oseba):
    otroci = [otrok for otrok in oseba.childNodes if otrok.nodeType == otrok.ELEMENT_NODE]
    print(oseba.getAttribute("ime"))
    for otrok in otroci:
        izpis(otrok)
r = open("C:\\Users\\dujo\\PycharmProjects\\rodovnik.xml")
rodovnik = xml.dom.minidom.parse(r)
karelVeliki = rodovnik.firstChild
izpis(karelVeliki)

#def prestejPotomce(oseba):
#    otroci = [otrok for otrok in oseba.childNodes if otrok.nodeType == otrok.ELEMENT_NODE]
#    potomcev = len(otroci)
#    for otrok in otroci:
#        potomcev += prestejPotomce(otrok)
#    return potomcev
#print(prestejPotomce(karelVeliki))

#def izpisiOtroke(oseba):
#    otroci = [otrok for otrok in oseba.childNodes if otrok.nodeType == otrok.ELEMENT_NODE]
#    if otroci:
#        print ("%s je imel %s po imenu %s." % (
#            oseba.getAttribute("ime"),
#            "otroka" if len(otroci)<=2 else "otroke",
#            ", ".join(otrok.getAttribute("ime") for otrok in otroci)))
#        for otrok in otroci:
#            izpisiOtroke(otrok)
#izpisiOtroke(karelVeliki)

#def izpisZamik(oseba,nivo):
#    otroci = [otrok for otrok in oseba.childNodes if otrok.nodeType == otrok.ELEMENT_NODE]
#    print("    "*nivo + oseba.getAttribute("ime"))
#    for otrok in otroci:
#        izpisZamik(otrok,nivo+1)
#print(izpisZamik(karelVeliki,0))