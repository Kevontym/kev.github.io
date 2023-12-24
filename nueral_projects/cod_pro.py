def open_or_senior(data):
    result = []

    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")

    return result

# Example usage:
data = [(40, 4), (20, 1), (56, 9), (55, 15), (30, 3)]
categories = open_or_senior(data)

print(categories)
