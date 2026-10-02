record_ids = [101, 102, 103, 104, 105, 106]

record_ids.append(107)

batch_one: list[int] = record_ids[0:4]

first_id, second_id, *rest_ids = record_ids

print(f"batch_one: {batch_one}")
print(F"first and second: {first_id} {second_id}")
print(F"rest_id: {rest_ids}")