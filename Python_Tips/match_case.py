lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "Java":
        print("You can become a mobile app developer")

    case _:
        print("The language doesn't matter, what matters is solving problems.")