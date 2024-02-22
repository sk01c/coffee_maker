flight_costs = {
    "milan": 70,
    "peru": 600,
    "ibiza": 110,
    "goa": 700,
    "california": 900,
    "thailand": 400
}

hotel_costs = {
    "milan": 100,
    "peru": 60,
    "ibiza": 40,
    "goa": 40,
    "california": 150,
    "thailand": 20
}

car_costs = {
    "milan": 50,
    "peru": 20,
    "ibiza": 30,
    "goa": 20,
    "california": 80,
    "thailand": 20
}

city_flight = input("Please enter where you would like to fly out of the following destinations:\n milan, peru, ibiza, goa, california, thailand \n").lower()
num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Please enter the number of days you will need a car: "))

def hotel_cost(num_nights, city_flight):
    return num_nights * hotel_costs.get(city_flight, 0)

def plane_cost(city_flight):
    return flight_costs.get(city_flight, 0)

def car_rental(rental_days, city_flight):
    return rental_days * car_costs.get(city_flight, 0)

def holiday_cost():
    return hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days, city_flight)

print("\n")
print(f"Hotel cost for {num_nights} nights in {city_flight.capitalize()}: £{hotel_cost(num_nights=num_nights, city_flight=city_flight)}")
print(f"Plane cost for the destination {city_flight.capitalize()}: £{plane_cost(city_flight=city_flight)}")
print(f"Car rental for {rental_days} days: £{car_rental(rental_days=rental_days, city_flight=city_flight)}")
print("\n")
print(f"The total price for the holiday: £{holiday_cost()}")
