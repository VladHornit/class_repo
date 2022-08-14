class Citizen:
    def __init__(self, house, trip, diet):
        self.house = house
        self.trip = []
        self.diet = diet

    def compute_carbon_foorprint(self, diet_carbon_footprint, house_footprint, trip_footprint):
        human_carbon_footprint = result_diet_carbon_footprint + house_footprint + trip_footprint
        return human_carbon_footprint

class Diet:
    def __init__(self, diet_type, distance_from_farm):
        self.diet_type = diet_type
        self.distance_from_farm = distance_from_farm

    def compute_diet_carbon_footprint(self, diet_type, distance_from_farm):
        diet_footprint = 1000 * (self.distance_from_farm / 100)
        if diet_type == "vegetarian":
            result_diet_carbon_footprint = 5 * diet_foorprint / 6
        else:
            result_diet_carbon_footprint = 3 * diet_foorprint / 4
        return result_diet_carbon_footprint

class House:
    def __init__(self, flat, size, heating_temperature):
        self.flat = flat
        self.size  = size
        self.heating_temperature = heating_temperature


    def compute_house_footprint(self, flat, size, heating_temperature):
        footprint = (heating_temperature - 17) * 10 * self.size
        if flat == "flat":
            house_footprint = 2 * footprint / 3
        return house_footprint


class Trip:
    def __init__(self, type, distance):
        self.type = type
        self.distance = distance

    def compute_trip_footprint(self, type, distance):
        if type == "plane":
            trip_footprint = (self.distance / 100) * 10
        elif type == "car":
            trip_footprint = (self.distance / 100) * 8
        else:
            trip_footprint = (self.distance / 100) * 0.2
        return trip_footprint



diet_citizen_1 = Diet("organik", 100)
flat_1 = House("flat", 50, 20)
trip_1 = Trip("plane", 2500)
citizen_1 = Citizen(flat_1, trip_1, diet_citizen_1)

diet_citizen_1.compute_diet_carbon_footprint
flat_1.compute_house_footprint
trip_1.compute_trip_footprint
citizen_1.compute_carbon_foorprint
print(citizen_1.compute_carbon_foorprint)

#print(diet_citizen_1.compute_diet_carbon_footprint)
#print(diet_citizen_1.diet_type)

#print(flat_1.compute_house_footprint)
#print(trip_1.compute_trip_footprint)
#print(citizen_1.compute_carbon_foorprint(diet_citizen_1, flat_1, trip_1))
