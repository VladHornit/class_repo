class Citizen:
    def __init__(self, house, trip, diet):
        self.house = house
        self.trip = []
        self.diet = diet

    def compute_carbon_foorprint(self, compute_diet_carbon_footprint, compute_house_footprint, compute_trip_footprint):
        human_carbon_footprint = compute_diet_carbon_footprint + compute_house_footprint + compute_trip_footprint
        return human_carbon_footprint

class Diet:
    def __init__(self, diet_type, distance_from_farm):
        self.diet_type = diet_type
        self.distance_from_farm = distance_from_farm

    def compute_diet_carbon_footprint(self, diet_type, distance_from_farm):
        diet_carbon_footprint = 1000 * (distance_from_farm / 100)
        if diet_type == "vegetarian":
            compute_diet_carbon_footprint = 5 * diet_carbon_foorprint / 6
        else:
            compute_diet_carbon_footprint = 3 * diet_carbon_foorprint / 4
        return compute_diet_carbon_footprint

class House:
    def __init__(self, flat, size, heating_temperature):
        self.flat = flat
        self.size  = size
        self.heating_temperature = heating_temperature


    def compute_house_footprint(self, flat, size, heating_temperature):
        footprint = (heating_temperature - 17) * 10 * size
        if flat == "flat":
            compute_house_footprint = 2 * footprint / 3
        return compute_house_footprint


class Trip:
    def __init__(self, type, distance):
        self.type = type
        self.distance = distance

    def compute_trip_footprint(self, type, distance):
        if type == "plane":
            compute_trip_footprint = (distance / 100) * 10
        elif type == "car":
            compute_trip_footprint = (distance / 100) * 8
        else:
            compute_trip_footprint = (distance / 100) * 0.2
        return compute_trip_footprint



citizen_1 = Citizen("flat", "Kyiv", "organik")
diet_citizen_1 = Diet("organik", 100)
flat_1 = House("flat", 50, 20)
trip_1 = Trip("plane", 2500)

#print(citizen_1.compute_carbon_foorprint())
#print(diet_citizen_1.diet_type)
#print(diet_citizen_1.compute_diet_carbon_footprint)
