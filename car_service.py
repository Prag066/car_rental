import datetime

class RentalCarService:
    def __init__(self):
        self.bookings = {}

    def register_rental(self, booking_number, customer_name, car_category, rental_time, car_mileage):
        if booking_number in self.bookings:
            raise ValueError("Booking number already exists")
        self.bookings[booking_number] = {
            'customer_name': customer_name,
            'car_category': car_category,
            'rental_time': rental_time,
            'car_mileage': car_mileage
        }
        return f"Rental registered with booking number: {booking_number}"

    def calculate_price_for_return(self, booking_number, return_time, return_mileage):
        if booking_number not in self.bookings:
            raise ValueError("Invalid booking number")

        booking = self.bookings[booking_number]
        car_category = booking['car_category']
        rental_time = booking['rental_time']
        car_mileage = booking['car_mileage']
        base_day_rental = 50
        kilometer_price = 0.2

        # Calculate rental duration in days
        rental_duration = (return_time - rental_time).days

        if car_category == 'Compact':
            price = base_day_rental * rental_duration
        elif car_category == 'Premium':
            number_of_kilometers = return_mileage - car_mileage
            price = base_day_rental * rental_duration * 1.2 + kilometer_price * number_of_kilometers
        elif car_category == 'Minivan':
            number_of_kilometers = return_mileage - car_mileage
            price = base_day_rental * rental_duration * 1.7 + kilometer_price * number_of_kilometers * 1.5
        else:
            raise ValueError("Invalid car category")

        del self.bookings[booking_number]
        return price

# Test cases
car_system = RentalCarService()

# Test U1: Rental registration
registration_response = car_system.register_rental(
    booking_number='B001',
    customer_name='John Doe',
    car_category='Compact',
    rental_time=datetime.datetime(2023, 6, 1),
    car_mileage=10000
)
print(registration_response)

# Test U2: Car Return
price = car_system.calculate_price_for_return(
    booking_number='B001',
    return_time=datetime.datetime(2023, 6, 5),
    return_mileage=10250
)
print(f'price of your ride is {price}')
