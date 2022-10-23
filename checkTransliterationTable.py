import json

fname = input("File to check? ")

schemaTableFile = open('schema.json')
schemaTable = json.load(schemaTableFile)
schemaTableFile.close()

transliterationTableFile = open(f'{fname}.json')
transliterationTable = json.load(transliterationTableFile)
transliterationTableFile.close()


print("Check Transliteration Table File >")
print(f'Name: {transliterationTable["languageinfo"]["name"]} (Schema: {schemaTable["languageinfo"]["name"]})')
print(f'Script: {transliterationTable["languageinfo"]["script"]} (Schema: {schemaTable["languageinfo"]["script"]})')
print(f'Encoding: {transliterationTable["languageinfo"]["encoding"]} (Schema: {schemaTable["languageinfo"]["encoding"]})')
print(f'Bare Maatras Included? {"YES" if transliterationTable["languageinfo"]["bare_maatras_included"] else "NO"} (Schema: {"YES" if schemaTable["languageinfo"]["bare_maatras_included"] else "NO"})')