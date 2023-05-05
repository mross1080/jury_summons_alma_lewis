api_key = "pateJHFHWXxnTByKo.e66614d6f6e5444b37ed7b3ec9bb75b875a37c667436ba2579cdcf2711cb6eed"

from pyairtable import Table
table = Table(api_key, 'appsMAV1KTqDGA5m2', 'responses')
# print(table.all())
new_row = table.create({"name":"dssdd3"})
print(new_row)
table.update(new_row["id"], {"q1": "Hello"})
table.update(new_row["id"], {"q2": "ByeHello"})