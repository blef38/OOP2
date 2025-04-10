def make_book(filename):
    recepts_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            if i < len(lines):
                ingredient_count = int(lines[i].strip())
                i += 1
                ingredients = []
                for k in range(ingredient_count):
                    if i < len(lines):
                        ingredient_list = lines[i].strip().split('|')
                        ingredient_name = ingredient_list[0].strip()
                        quantity = float(ingredient_list[1].strip())
                        measure = ingredient_list[2].strip()
                        ingredients.append({
                            'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure
                        })
                        i += 1
                recepts_dict[dish_name] = ingredients
                i+=1
    return recepts_dict


filename = 'recepts.txt'
recepts = make_book(filename)
print(recepts)

