# Dictionary containing flight costs for various destinations
flight_costs = {
    "milan": 70,
    "peru": 600,
    "ibiza": 110,
    "goa": 700,
    "california": 900,
    "thailand": 400
}

# Dictionary containing hotel costs for various destinations
hotel_costs = {
    "milan": 100,
    "peru": 60,
    "ibiza": 40,
    "goa": 40,
    "california": 150,
    "thailand": 20
}

# Dictionary containing car rental costs for various destinations
car_costs = {
    "milan": 50,
    "peru": 20,
    "ibiza": 30,
    "goa": 20,
    "california": 80,
    "thailand": 20
}

# Prompt the user to input the destination city
city_flight = input("Please enter where you would like to fly out of the following destinations:\n milan, peru, ibiza, goa, california, thailand \n").lower()

# Prompt the user to input the number of nights they will stay at the hotel
num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))

# Prompt the user to input the number of days they will need a car
rental_days = int(input("Please enter the number of days you will need a car: "))

# Function to calculate hotel cost based on the number of nights and destination
def hotel_cost(num_nights, city_flight):
    return num_nights * hotel_costs.get(city_flight, 0)

# Function to retrieve plane cost based on the destination
def plane_cost(city_flight):
    return flight_costs.get(city_flight, 0)

# Function to calculate car rental cost based on the number of days and destination
def car_rental(rental_days, city_flight):
    return rental_days * car_costs.get(city_flight, 0)

# Function to calculate total holiday cost
def holiday_cost():
    return hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days, city_flight)

# Display individual costs and total holiday cost
print("\n")
print(f"Hotel cost for {num_nights} nights in {city_flight.capitalize()}: £{hotel_cost(num_nights=num_nights, city_flight=city_flight)}")
print(f"Plane cost for the destination {city_flight.capitalize()}: £{plane_cost(city_flight=city_flight)}")
print(f"Car rental for {rental_days} days: £{car_rental(rental_days=rental_days, city_flight=city_flight)}")
print("\n")
print(f"The total price for the holiday: £{holiday_cost()}")
