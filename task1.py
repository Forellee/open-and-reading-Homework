def read_cookbook(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            num_ingredients = int(file.readline().strip())
            ingredients = []

            for _ in range(num_ingredients):
                line = file.readline()
                name, quantity, measure = map(str.strip, line.split('|'))
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            file.readline()  # пустая строка между блюдами

    return cook_book


if __name__ == '__main__':
    cookbook = read_cookbook('recipes.txt')
    for dish, ingredients in cookbook.items():
        print(dish)
        for ing in ingredients:
            print(f"  {ing}")
