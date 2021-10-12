from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        counter = int(file.readline())
        
        temp_list = []
        for item in range(counter):
            name, quantity_1, measure_1 = file.readline().split('|')
            temp_list.append(
                {'ingredient_name': name.strip(), 'quantity': quantity_1.strip(), 'measure': measure_1.strip()} 
            )
        cook_book[recipe_name] = temp_list
        
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            # print(dish)
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in cooking_list:
                    val = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                    cooking_list[ingr['ingredient_name']] = val
                else:
                    cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return(cooking_list)            


print(get_shop_list_by_dishes(['Омлет','Фахитос'], 2))