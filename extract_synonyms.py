import json

dictionary_file = open('eng_synonyms.json')
synonyms_file = open('synonyms.txt', 'a')

dictionary_json = json.load(dictionary_file)

for value in dictionary_json:
    line = ""
    line += value
    line += ", "
    for synonym in dictionary_json[value]:
        line += synonym
        line += ", "
    line_length = len(line)
    line = line[:line_length-2]
    line += "\n"
    
    synonyms_file.write(line)
        

dictionary_file.close()
synonyms_file.close()