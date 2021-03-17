
def ExtractDataFromFile():
   YearsList = [] 
   ManufacturersList =[]
   ModelsList = []
   DescriptionsList = []
   TransmissionsList =[]
   TransmissionTypesList = []
   EnginesCapacityList = []
   FuelTypesList = []

   FileHandler = open("carsData.txt", "r")
   CarsData = FileHandler.readlines()
   FileHandler.close()
   
   for data in CarsData:
      car_data = data.split("*")
      YearsList.append(car_data[0])
      ManufacturersList.append(car_data[1])
      ModelsList.append(car_data[2])
      DescriptionsList.append(car_data[3])
      TransmissionsList.append(car_data[4])
      TransmissionTypesList.append(car_data[5])
      EnginesCapacityList.append(car_data[6])
      FuelTypesList.append(car_data[7])

   return YearsList, ManufacturersList, ModelsList, DescriptionsList, TransmissionsList, TransmissionTypesList, EnginesCapacityList, FuelTypesList


def NumberOfAutomaticTransmissions(transmission_types):
   count = 0
   for transmission_type in transmission_types:
      if transmission_type.lower() == "automatic":
         count += 1
   
   return count
   
def FindAverageEngineCapacityForMercedesCars(engine_capacity, manufacturers):
   engine_capacity_total = 0
   total = 0
   for manufacturer in manufacturers:
      if manufacturer == "Mercedes-Benz":
         index = manufacturers.index(manufacturer)
         engine_capacity_total += float(engine_capacity[index])
         total += 1
   average_engine_capacity = (engine_capacity_total) / total
   
   return average_engine_capacity
   

def main():
  
   years_list, manufacturers_list, models_list, descriptions_list, transmissions_list, transmission_types_list, engines_capacity_list, fuel_types_list = ExtractDataFromFile()
   automatic_transmissions = NumberOfAutomaticTransmissions(transmission_types_list)
   Mercedes_Benz_average_capacity = FindAverageEngineCapacityForMercedesCars(engines_capacity_list, manufacturers_list)
   

   for year in years_list:
      print(year)
   
   for manufacturer in manufacturers_list:
      print(manufacturer)
      
   for model in models_list:
      print(model)
      
   for description in descriptions_list:
      print(description)
      
   for transmission in transmissions_list:
      print(transmission)
      
   for transmission_type in transmission_types_list:
      print(transmission_type)
      
   for engine_capacity in engines_capacity_list:
      print(engine_capacity)
      
   for fuel_type in fuel_types_list:
      print(fuel_type)

   print("\n")
   
   print("There are " + str(automatic_transmissions) + " automatic transmissions.")
   print(Mercedes_Benz_average_capacity)
   
main()
