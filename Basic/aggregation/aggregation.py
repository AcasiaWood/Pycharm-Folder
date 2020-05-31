# aggregate data type

aggregate = set('Aggregate')
print(aggregate)

# intersection, union, difference

first_aggregate = {1, 2, 3}
second_aggregate = {3, 4, 5}

# intersection

print(first_aggregate & second_aggregate, first_aggregate.intersection(second_aggregate))  # both results are the same

# union

print(first_aggregate | second_aggregate, first_aggregate.union(second_aggregate))  # both results are the same

# difference

print(first_aggregate - second_aggregate, first_aggregate.difference(second_aggregate))  # both results are the same
