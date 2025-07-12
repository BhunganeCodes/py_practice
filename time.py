def main():
    user_input = int(input("How many minutes would you like to convert? "))
    hours, minutes = time_to_convert(user_input)
    print(f"Your new time is {hours} hours and {minutes} minutes.")

def time_to_convert(total_minutes):
    hours = total_minutes // 60    # floor division to the lowest whole number
    minutes = total_minutes % 60    # modulo division to determine the remaining minutes
    return hours, minutes


if __name__ == "__main__":
    main() # type: ignore