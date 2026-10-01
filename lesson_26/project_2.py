def check_prime_or_composite(num):
    if num <= 1:
        return "neither prime nor composite"

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "composite"

        return "prime"

def main():
    try:
        user_input = int(input("Enter a positive whole number: "))
        result = check_prime_or_composite(user_input)
        print(f"The number {user_input} is {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()