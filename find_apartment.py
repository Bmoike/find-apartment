# apartment search 1 has no default values and prints the city, bedrooms, and price of apartment you are looking for
def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f"Welcome to GC Property Management! Looking up the listings in {city} for a {min_beds} bedroom apartment"
              f" that allows pets, all with a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up the listings in {city} for a {min_beds} bedroom apartment"
              f", all with a budget of {max_rent} per month...")


# apartment search 2 is same as 1 but has a default value for beds and pets
def apt_search2(city, max_rent, min_beds=1, pets_allowed=False):
    if pets_allowed:
        print(f"Welcome to GC Property Management! Looking up the listings in {city} for a {min_beds} bedroom apartment"
              f" that allows pets, all with a budget of {max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management! Looking up the listings in {city} for a {min_beds} bedroom apartment"
              f", all with a budget of {max_rent} per month...")


# call apartment 1 search
apt_search1("Huston", 1500, 2, pets_allowed=False)

# test default values of apartment 2 search function
apt_search2("Huston", 2500)
apt_search2("Huston", 2500, 3)
apt_search2("Huston", 2500, pets_allowed=True)
print()
# testing lambda functions
plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(30))

square_num = lambda x: x**2
print(square_num(4))

concatenate = lambda x: f"- {x}"
print(concatenate("hello"))

divide_by_three = lambda x: x/3
print(divide_by_three(9))
