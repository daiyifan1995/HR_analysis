import csv


def readCsvToDictList(filename):
    file = open(filename,encoding="utf-8")
    dataset = []
    dictreader = csv.DictReader(file)
    for i in dictreader:
        dataset.append(i)  # reading to dict
    return dataset

def readCsvToList(filename):
    file = open(filename,encoding="utf-8")
    dataset = []
    reader = csv.Reader(file)
    for i in reader:
        dataset.append(i)  # reading to dict
    return dataset

def readCsvGetTitle(filename):
    file = open(filename,encoding="utf-8")
    reader = csv.reader(file)
    for i in reader:
        return i



