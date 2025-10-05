def assign_students_to_sections(sections, *students):
    dict1 = {}
    dict2 = {}

    for i in range(len(sections)):
        dict1[sections[i]] = i

    for i in sections:
        dict2[i] = []

    for i in students:
        sum = 0
        for j in i:
            sum += ord(j)
        correction = sum % len(sections)
        for key, value in dict1.items():
            if value == correction:
                dict2[key].append(i)

    print(dict2)

assign_students_to_sections ('ABCDE', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace')