import os


class CookBook:

    def __init__(self, file_size_local, file_path_local):
        self.cook_book_dict = {}
        with open(file_path_local, 'r') as file_local:
            for count in range(file_size_local):
                dish_local = Dish(file_local)
                self.cook_book_dict[dish_local.name] = dish_local.dish_list
        return


class Dish:

    def __init__(self, file_local):
        self.dish_list = []
        self.name = file_local.readline().strip()
        ingredients_count = int(file_local.readline().strip())
        for num in range(ingredients_count):
            current_ingredient = Ingredient(file_local).ingredient_dict
            self.dish_list += [current_ingredient]
        file_local.readline()
        return


class Ingredient:

    def __init__(self, file_local):
        self.ingredient_dict = {}
        ingredient_string = file_local.readline().strip()
        ingredient_list = ingredient_string.split(" | ")
        self.ingredient_dict = {'ingredient_name': ingredient_list[0], 'quantity': int(ingredient_list[1]),
                                'measure': ingredient_list[2]}
        return


def check_file_size(file_path_local):
    file_size_local = 0
    with open(file_path_local, 'r') as file:
        for line in file.readlines():
            if line.strip() == '':
                file_size_local += 1
    if file_size_local > 0:
        file_size_local += 1
    elif file_size_local == 0:
        with open(file_path_local, 'r') as file:
            if file.readline() != '':
                file_size_local += 1
    return file_size_local


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for count in range(int(len(dishes))):
        for key, value in cook_book.cook_book_dict.items():
            if key == dishes[count]:
                ingredients_list = value
                for i in range(int(len(ingredients_list))):
                    ingredients_list[i]['quantity'] *= person_count
                    if ingredients_list[i]['ingredient_name'] not in ingredients_dict.keys():
                        ingredients_dict[ingredients_list[i]['ingredient_name']] = {
                            'measure': ingredients_list[i].get('measure'),
                            'quantity': ingredients_list[i].get('quantity')}
                    else:
                        current_ingredient = ingredients_dict.get(ingredients_list[i]['ingredient_name'])
                        current_ingredient['quantity'] += ingredients_list[i].get('quantity')
    return ingredients_dict


# Основная часть программы
file_path_global = os.path.join(os.getcwd(), "Cook_book.txt")
file_size = check_file_size(file_path_global)

if file_size > 0:
    cook_book = CookBook(file_size, file_path_global)
    dishes_list = ['Омлет', 'Фахитос']
    print(get_shop_list_by_dishes(dishes_list, 2))
else:
    print('В книге нет рецептов')
