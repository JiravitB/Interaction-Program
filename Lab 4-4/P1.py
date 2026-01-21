"""
Jiravit Boonyaritchaikit
683040154-3
P1
"""

from room import Bedroom, Kitchen

bed = Bedroom(10,20,5)
print(bed.describe_room())
print(f"Bed size : {bed.bed_size} ft")
print(f"Reccommended lighting : {bed.get_recommended_lighting()} lumen / square foot ")
print()

Kitchen_True = Kitchen(15,25)
print("Kitchen with island")
print(Kitchen_True.describe_room())
print(f"Reccommended lighting : {Kitchen_True.get_recommended_lighting()} lumen / square foot ")
island1,wall1 = Kitchen_True.calculate_counter_space()
print(f"Counter space : Wall {wall1}, Island {island1}")
print()

Kitchen_False = Kitchen(15,25,False)
print("Kitchen without island")
print(Kitchen_False.describe_room())
print(f"Reccommended lighting : {Kitchen_False.get_recommended_lighting()} lumen / square foot ")
island2,wall2 = Kitchen_False.calculate_counter_space()
print(f"Counter space : Wall {wall2}, Island {island2}")
print()

print(Kitchen_False.calculate_counter_space.__doc__)