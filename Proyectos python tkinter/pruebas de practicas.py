import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse("C:\\Users\\Luis Reyes\\Downloads\\cars.xml")
car_for_sale = tree.getroot()

for car in car_for_sale:
    if car.find("brand").text == "Ford" and car.find("model").text == "Mustang":
        car_for_sale.remove(car)
        break

new_car = xml.etree.ElementTree.Element("car")
xml.etree.ElementTree.SubElement(new_car, "id").text = 4
xml.etree.ElementTree.SubElement(new_car, "brand").text = "maserati"
xml.etree.ElementTree.SubElement(new_car, "model").text = "1970"
xml.etree.ElementTree.SubElement(new_car, "price", {"currency":"EUR"}).text = "10100"
car_for_sale.append(new_car)
tree.write("newcars.xml", method="")