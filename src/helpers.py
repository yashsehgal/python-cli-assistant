
class helpers:
  def __init__(self):
    self.access = True
    
  def checkForEmptyStringsInArray(self, arrayOfStrings):
    for STRING in range(len(arrayOfStrings)):
      if arrayOfStrings[STRING] == None or arrayOfStrings[STRING] == "":
        return "HasEmptyString"
      return "DoNotHavEmptyString"
    
  def checkEmptyString(self, stringToBeChecked):
    if stringToBeChecked == None or stringToBeChecked == "":
      return "StringIsEmpty"
    return "StringIsNotEmpty"
  
  