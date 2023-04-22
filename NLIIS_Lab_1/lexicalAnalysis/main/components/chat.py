import csv

FILE_NAME = "main\components\csv\zoo.csv"

class AnimalsChat:
    
    def getAnimals(self):
        table = parseCsv(FILE_NAME)

        animals = []
        for row in table:
            animals.append(row[0])

        animals.remove('animal_name')
        return animals
    

    def getFeatures(self):
        features = parseCsv(FILE_NAME)
        return features[0]


    def getAnimalsByFeature(self, feature):
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