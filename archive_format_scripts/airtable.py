api_key = "pateJHFHWXxnTByKo.e66614d6f6e5444b37ed7b3ec9bb75b875a37c667436ba2579cdcf2711cb6eed"

from pyairtable import Table
table = Table(api_key, 'appsMAV1KTqDGA5m2', 'responses')
# print(table.all())
EXCLUDED_KEYS = ["userName","userId","archivePermission"]


def archive_answer(data):
    print("Archive Answer : ".format(data))
    new_row = table.create({"name":data["userName"]})
    for k, v in data.items():
        print(k, v)
        print(new_row)
        if k not in EXCLUDED_KEYS:
            table.update(new_row["id"], {k: v})



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
  "countryName": "44",
  "archivePermission":"1",
  "lang" : "en"
}
)
    except Exception as e:
        print(e)
