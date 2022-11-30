import math

talents = float(input("Enter talents:"))
pound = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

kg_total = (((talents * 20 * 32 * 13.3) + (pound * 32 * 13.3) +(13.3 * lots)) / 1000)
kg = math.floor(kg_total)
gr = (kg_total - kg) * 1000
gr = round(gr,3)

print("The weight in modern units:")

print(f"{kg} kilograms {gr} grams.")


