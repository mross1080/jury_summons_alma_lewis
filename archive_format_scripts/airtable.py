api_key = "pateJHFHWXxnTByKo.e66614d6f6e5444b37ed7b3ec9bb75b875a37c667436ba2579cdcf2711cb6eed"
import json
from pyairtable import Table
table = Table(api_key, 'appsMAV1KTqDGA5m2', 'responses')
# print(table.all())
EXCLUDED_KEYS = ["userName","userId","archivePermission"]
with open('country_json_data.json', 'r') as myfile:
    data=myfile.read()


answer_lookup = {
    "en": {
        "know_the_witness": {
            "1": "Yes",
            "2": "No",
        },
        "a3": {
            "1": "How you see and identify yourself",
            "2": "How others see and identify you",
            "3": "Both", 
            "4": "None of the above"
        },
        "last_names": {
            "0": "Anderson",
            "1": "Barret",
            "2": "Buck",
            "3": "Bell",
            "4": "Coats",
            "5": "Cary",
            "6": "Kerry",
            "7": "Duperton",
            "8": "Dipitón", 
            "9": "Dishmey", 
            "10": "Dishmer",
            "11": "Buck",
            "12": "Ejice",
            "13": "Fuchue",
            "14": "Forche",
            "15": "Green", 
            "16": "Hilton", 
            "17": "Henderson",
            "18": "Hopkins",
            "19": "James",
            "20": "Jhonson", 
            "21": "Jones", 
            "22": "King", 
            "23": "Kinxon", 
            "24": "Miller", 
            "25": "Nwes", 
            "26": "Punez", 
            "27": "Paul", 
            "28": "Robinson", 
            "29": "Relmon", 
            "30": "Schod", 
            "31": "Sarry", 
            "32": "Shepherd", 
            "33": "Sapher", 
            "34": "Wingth", 
            "35": "Williams", 
            "36": "Willmore", 
            "37": "None of the above" 
        },
    },
    "es": {
        "a1": {
            "1": "Si",
            "2": "No"
        },
        "a3": {
            "1": "Cómo te ves e identificas",
            "2": "Como otres te ven e identifican",
            "3": "Todo lo anterior",
            "4": "Ninguna de las anteriores"
        },
               
        "a2": {
            "0": "Anderson",
            "1": "Barret",
            "2": "Buck",
            "3": "Bell",
            "4": "Coats",
            "5": "Cary",
            "6": "Kerry",
            "7": "Duperton",
            "8": "Dipitón", 
            "9": "Dishmey", 
            "10": "Dishmer",
            "11": "Buck",
            "12": "Ejice",
            "13": "Fuchue",
            "14": "Forche",
            "15": "Green", 
            "16": "Hilton", 
            "17": "Henderson",
            "18": "Hopkins",
            "19": "James",
            "20": "Jhonson", 
            "21": "Jones", 
            "22": "King", 
            "23": "Kinxon", 
            "24": "Miller", 
            "25": "Nwes", 
            "26": "Punez", 
            "27": "Paul", 
            "28": "Robinson", 
            "29": "Relmon", 
            "30": "Schod", 
            "31": "Sarry", 
            "32": "Shepherd", 
            "33": "Sapher", 
            "34": "Wingth", 
            "35": "Williams", 
            "36": "Willmore", 
            "37": "None of the above" 
        },
    }
}



# parse file
country_index_score = json.loads(data)

def archive_answer(data):
    print("Starting Archive Process ")
    print("Archive Answer : ".format(data))
    try:
        data["countryName"] = country_index_score[data["countryName"]]["country_name"]
    except Exception as e:
        print(e)
    new_row = table.create({"name":data["userName"]})
    for k, v in data.items():
        # print(k, v)
        # print(new_row)
        if k not in EXCLUDED_KEYS:
            table.update(new_row["id"], {k: v})
    print("Completed Archival Process")



if __name__ == "__main__":
    try:
        archive_answer({
  "userName": "Steven Universe",
  "userId": "1",
  "a1": "1",
  "a2": "1",
  "a3": "1",
  "united_against_the": "country",
  "for_the_line_1": "people",
  "for_the_line_2": "state",
  "know_the_witness": "yes",
  "countryName": "4",
  "archivePermission":"1",
  "lang" : "en"
}
)
    except Exception as e:
        print(e)
