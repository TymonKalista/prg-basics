class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f"Distance: {self.distance} km")
        print(f"Rate: {self.rate_per_km} €/km")
        print(f"Fare: {self.fare} €")



def main():
    taxi1 = TaxiRide(rate_per_km=2)  
    taxi2 = TaxiRide(rate_per_km=2.5)  
    
   
    taxi1.calculate_fare(10)  
    taxi2.calculate_fare(15)  
    
    
    print("Receipt for Taxi 1:")
    taxi1.print_receipt()
    
    print("\nReceipt for Taxi 2:")
    taxi2.print_receipt()
   

if __name__ == "__main__":
    main()
