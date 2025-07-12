def main():
    name = input("Hey, what is your name? ").strip().title()
    name = greet(name)
    print(name)

def greet(name):
    return f"Hey, {name}"

if __name__ == "__main__":
    main()