def main():
    number = int(input("Please enter a number: "))
    parity = even_or_odd(number)
    print(parity)


def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
if __name__ == "__main__":
    main()