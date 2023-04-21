import csv

FILE_NAME = "zoo.csv"

class AnimalsChat:
    
    def getAnimals(feature):
        animals = parseCsv(FILE_NAME)

        found_animals = []
        feature_number = getHeader(FILE_NAME).index(feature)
        for animal in animals:
            if animal[feature_number] == "1":
                found_animals.append(animal[0])
        return found_animals


def parseCsv(fileName):
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        return list(reader)


def getHeader(fileName):
    return parseCsv(fileName)[0]