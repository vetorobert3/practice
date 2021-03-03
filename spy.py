def uncover_spy(n, trust):
    # key is person int, value is list of people this person trusts
    cache = {}
    # key is person int, value is amount of people that trust this person
    trusted_by = {}
    # holds id of potential spies (needs to have only one spy for their to be a spy)
    spy_list = []
    # fill up dictionaries
    for person in range(1, n + 1):
        cache[person] = []
        trusted_by[person] = 0
    # tuple first value is person, second is person that person trusts
    # add second person to first person's list of people they trust
    # then increment count of second persons dict of people who trust them
    for pair in trust:
        cache[pair[0]].append(pair[1])
        trusted_by[pair[1]] += 1
    # check if person DOESN'T trust anyone AND that everyone trusts THEM
    for person in cache:
        # 1. Doesnt trust anyone 2. Everyone trusts them
        if len(cache[person]) == 0 and trusted_by[person] == (n - 1):
            spy_list.append(person)
    # 3. Works alone
    # only return spy if spy list is exactly 1
    if len(spy_list) == 1:
        return spy_list[0]
    return -1
test = uncover_spy(4, [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]])

print(uncover_spy(2, [[1, 2]]))