class Citizen:
    def __init__(self, house, trip, diet):
        self.house = house
        self.trip = []
        self.diet = diet

    def compute_carbon_footprint(self):
        #human_carbon_footprint =  House.compute_house_footprint(self.house) + Trip.compute_trip_footprint(self.trip) + Diet.compute_diet_carbon_footprint(self.diet)
        house_footprint =  self.house.compute_house_footprint()
        result_trip_footprint = self.trip[0].compute_trip_footprint()
        diet_footprint = self.diet.compute_diet_carbon_footprint()
        human_carbon_footprint = house_footprint + diet_footprint
        #print(house_footprint)
        #print(trip_footprint)
        #print(diet_footprint)
        return human_carbon_footprint


class Diet:
    def __init__(self, diet_type, distance_from_farm):
        self.diet_type = diet_type
        self.distance_from_farm = distance_from_farm

    def compute_diet_carbon_footprint(self):
        diet_footprint = 1000 * (self.distance_from_farm / 100)
        if self.diet_type == "vegetarian":
            diet_carbon_footprint = 5 * diet_footprint / 6
        else:
            diet_carbon_footprint = 3 * diet_footprint / 4
        return diet_carbon_footprint

class House:
    def __init__(self, flat, size, heating_temperature):
        self.flat = flat
        self.size  = size
        self.heating_temperature = heating_temperature


    def compute_house_footprint(self):
        footprint = (self.heating_temperature - 17) * 10 * self.size
        if self.flat == "flat":
            house_footprint = 2 * footprint / 3
        return house_footprint


class Trip:
    def __init__(self, type, distance):
        self.type = type
        self.distance = distance

    def compute_trip_footprint(self):
        if self.type == "plane":
            trip_footprint = (self.distance / 100) * 10
        elif self.type == "car":
            trip_footprint = (self.distance / 100) * 8
        else:
            trip_footprint = (self.distance / 100) * 0.2
        return trip_footprint



diet_1 = Diet("organik", 100)
flat_1 = House("flat", 50, 20)
trip_1 = Trip("plane", 2500)
citizen_1 = Citizen(flat_1, trip_1, diet_1)

print(diet_1.compute_diet_carbon_footprint())
print(flat_1.compute_house_footprint())
print(trip_1.compute_trip_footprint())

#print(citizen_1.house)
print(citizen_1.compute_carbon_footprint())

#print(diet_1.compute_diet_carbon_footprint("organik", 100))
#print(flat_1.compute_house_footprint("flat", 50, 20))
#print(trip_1.compute_trip_footprint("plane", 2500))

#print(citizen_1.diet)


#diet_citizen_1.compute_diet_carbon_footprint()
#citizen_1.compute_carbon_foorprint()
#trip_1.compute_trip_footprint(trip_1)
#citizen_1.diet.compute_diet_carbon_footprint()


#flat_1.compute_house_footprint()
#trip_1.compute_trip_footprint()
#citizen_1.compute_carbon_foorprint()
#print(citizen_1.compute_carbon_foorprint())

#print(diet_citizen_1.compute_diet_carbon_footprint)
#print(diet_citizen_1.diet_type)

#print(flat_1.compute_house_footprint)
#print(trip_1.compute_trip_footprint)
#print(citizen_1.compute_carbon_foorprint(diet_citizen_1, flat_1, trip_1))
