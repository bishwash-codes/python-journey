recipe = {"flour": (2, "cups"), "sugar": (1, "cup"), "eggs": (2, "count")}
print(recipe)


og_serving = float(input("enter original serving  "))
desired_serving = float(input("enter desired serving  "))
if og_serving == 0:
    print("error please enter data correctly")
else:
    scale_factor = desired_serving / og_serving
    print(scale_factor)
    for elmt, (quantity, unit) in recipe.items():
        scaled_quant = quantity * scale_factor
        if unit == "count":
            rounded = round(scaled_quant)
            print(elmt + ":", rounded)
        else:
            rounded = round(scaled_quant, 2)
            print(elmt + ":", rounded, unit)
