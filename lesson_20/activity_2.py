country_code= {
    "USA":"+1",
    "UK":"+41",
    "India":"+91",
    "Pakistan":"+92"
}
while True:
    inp=input("Enter which country's code do you need? (type q to quit): ")
    if inp.lower()=="q":
        print("bye")
        break
    elif inp in country_code:
        print(f"the code for {inp} is {country_code[inp]}")
    else:
        print(f"country {inp} not availible")