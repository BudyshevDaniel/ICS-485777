import json
from zasoby import nounlist2
from ruh import nounlist1


def convertToJSON():
 with open("ruh.json", 'w') as write_file:
    json.dump(nounlist1, write_file)
def convertInJSON():
 with open("zasoby.json", 'w') as write_file:
    json.dump(nounlist2, write_file)