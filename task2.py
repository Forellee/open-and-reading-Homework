from task1 import read_cookbook

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook('recipes.txt')
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list

if __name__ == '__main__':
    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    for item, details in result.items():
        print(f"{item}: {details}")
