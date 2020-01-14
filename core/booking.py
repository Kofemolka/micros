from nameko.rpc import rpc

class BookingService:
    name = "booking"

    @rpc
    def find_by_plate_number(self, plate_number):
        return {
            "user_id" : 123,
            "plate_number" : plate_number
        }