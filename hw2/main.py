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


filename = 'Recepts.txt'
recepts = make_book(filename)
#print(recepts)

def get_shop_list_by_dishes(dishes, person_count):
    ingred = {}
    for dish in dishes:
        for sostav in recepts[dish]:
            if sostav['ingredient_name'] in ingred:
                ingred[sostav['ingredient_name']]={'measure': sostav['measure'], 'quantity': ingred[sostav['ingredient_name']]['quantity']+sostav['quantity'] *  person_count}
            else:
                ingred[sostav['ingredient_name']] = {'measure': sostav['measure'], 'quantity': sostav['quantity'] * person_count}
    for ingredients in ingred:# сделал, чтобы вывод красивее
        print(f'{ingredients}: {ingred[ingredients]}')
    #print(ingred) если нужно прям как в задании вывести словарь
    return ingred

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

