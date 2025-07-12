def main():
    grade = int(input("What was your score? "))
    result = grade_result(grade)
    print(result)

def grade_result(score):
    if 90 <= score <= 100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":  
    main()