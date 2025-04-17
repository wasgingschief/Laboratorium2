def main():
    name = input("Podaj swoje imię: ")
    age = int(input("Podaj swój wiek: "))

    if age >= 18:
        print(f"{name}, jesteś pełnoletni/a.")
    else:
        print(f"{name}, jesteś niepełnoletni/a.")

if __name__ == "__main__":
    main()
