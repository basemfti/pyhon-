def get_fuel_percentage(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if denominator == 0 or numerator > denominator:
            raise ValueError
        percentage = (numerator / denominator) * 100
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
             return(f"{round(percentage)}%")
    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        fraction = input("Fraction: ")
        percentage = get_fuel_percentage(fraction)
        if percentage is not None:
            print(percentage)
            break
        else:
            print("Invalid input. Please enter again.")

if __name__ == "__main__":
    main()
