class HolidayCostCalculator:
    def __init__(self):
        # Dictionary containing flight costs for various destinations
        self.flight_costs = {
            "milan": 70,
            "peru": 600,
            "ibiza": 110,
            "goa": 700,
            "california": 900,
            "thailand": 400
        }

        # Dictionary containing hotel costs for various destinations
        self.hotel_costs = {
            "milan": 100,
            "peru": 60,
            "ibiza": 40,
            "goa": 40,
            "california": 150,
            "thailand": 20
        }

        # Dictionary containing car rental costs for various destinations
        self.car_costs = {
            "milan": 50,
            "peru": 20,
            "ibiza": 30,
            "goa": 20,
            "california": 80,
            "thailand": 20
        }

    def hotel_cost(self, num_nights, city_flight):
        """Calculate hotel cost based on the number of nights and destination."""
        return num_nights * self.hotel_costs.get(city_flight, 0)

    def plane_cost(self, city_flight):
        """Retrieve plane cost based on the destination."""
        return self.flight_costs.get(city_flight, 0)

    def car_rental(self, rental_days, city_flight):
        """Calculate car rental cost based on the number of days and destination."""
        return rental_days * self.car_costs.get(city_flight, 0)

    def holiday_cost(self, num_nights, city_flight, rental_days):
        """Calculate total holiday cost."""
        return (
                self.hotel_cost(num_nights, city_flight) +
                self.plane_cost(city_flight) +
                self.car_rental(rental_days, city_flight)
        )


# Prompt the user to input the destination city
city_flight = input(
    "Please enter where you would like to fly out of the following destinations:\n milan, peru, ibiza, goa, california, thailand \n").lower()

# Prompt the user to input the number of nights they will stay at the hotel
num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))

# Prompt the user to input the number of days they will need a car
rental_days = int(input("Please enter the number of days you will need a car: "))

# Create an instance of HolidayCostCalculator
holiday_calculator = HolidayCostCalculator()

# Calculate individual costs and total holiday cost
total_cost = holiday_calculator.holiday_cost(num_nights, city_flight, rental_days)

# Display individual costs and total holiday cost
print("\n")
print(
    f"Hotel cost for {num_nights} nights in {city_flight.capitalize()}: £{holiday_calculator.hotel_cost(num_nights, city_flight)}")
print(f"Plane cost for the destination {city_flight.capitalize()}: £{holiday_calculator.plane_cost(city_flight)}")
print(f"Car rental for {rental_days} days: £{holiday_calculator.car_rental(rental_days, city_flight)}")
print("\n")
print(f"The total price for the holiday: £{total_cost}")
