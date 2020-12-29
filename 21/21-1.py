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

        print(allergen_dict)
        allergen_dict[allergen] = allergen_dict[allergen] & ingredients
        print(allergen_dict)

found = dict()
found_new = True
while found_new:
    found_new = False

    for allergen, ingredients in allergen_dict.copy().items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            found[allergen] = ingredient
            found_new = True
            del allergen_dict[allergen]

            for allergen_to_update in allergen_dict.keys():
                allergen_dict[allergen_to_update].discard(ingredient)

not_found = ingredients_set - set(found.values())
count = 0
for ingredients, _ in food:
    for ingredient in ingredients:
        if ingredient in not_found:
            count += 1
print(count)
