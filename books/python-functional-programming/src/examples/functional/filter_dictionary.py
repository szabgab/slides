def main():
    grades = {
        "math":  100,
        "biology": 53,
        "chemistry": 62,
        "art": 78,
        "history": 20,
    }
    print(grades)

    good_grades = {key: value for (key, value) in grades.items() if value >= 60}
    print(good_grades)

    bad_grades = {key: grades[key] for key in grades if grades[key] < 60}
    print(bad_grades)


main()
