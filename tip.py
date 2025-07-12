def main():
    amount = dollar(input("How much is your meal? "))
    percent = percentage(input("How much tip will you be leaving? "))

    tip = amount * percent
    print(f"The tip will amount to: ${tip:.2f}")

def dollar(d):
    return float(d.strip().replace("$", ""))

def percentage(p):
    return float(p.strip().replace("%", "")) / 100

if __name__ == "__main__":
    main()