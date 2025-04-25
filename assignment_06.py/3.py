class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit
        self.to_inches_factor = {
            "inches": 1, "feet": 12, "yards": 36, "miles": 63360,
            "millimeters": 0.0393701, "centimeters": 0.393701,
            "meters": 39.3701, "kilometers": 39370.1
        }
        self.length_in_inches = length * self.to_inches_factor[unit]
# to solve we convert all the units into inches and then convert al
    def to_feet(self):
        return self.length_in_inches / 12

    def to_meters(self):
        return self.length_in_inches / 39.3701

# Example usage
c = Converter(10, "feet")
print(c.to_feet())  # Output: 0.75 
print(c.to_meters())  # Output: ~0.2286