import fileinput

food = []
allergens_set = set()
ingredients_set = set()
for line in fileinput.input():
    data = line.strip().split(" (contains ")
    ingredients = set(data[0].split(" "))
    allergens = set(data[1][:-1].split(", "))

    ingredients_set |= ingredients
    allergens_set |= allergens
    food.append((ingredients, allergens))


allergen_dict = dict()
for ingredients, allergens in food:
    for allergen in allergens:
        if allergen not in allergen_dict:
            allergen_dict[allergen] = ingredients_set

        allergen_dict[allergen] = allergen_dict[allergen] & ingredients

found = dict()
found_new = True
while found_new:
    found_new = False

    for allergen, ingredients in allergen_dict.copy().items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            found[ingredient] = allergen
            found_new = True
            del allergen_dict[allergen]

            for allergen_to_update in allergen_dict.keys():
                allergen_dict[allergen_to_update].discard(ingredient)

print(','.join(sorted(found.keys(), key=lambda x: found[x])))
