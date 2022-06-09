def calculate_years(database, dic, percentage):
    #[{'name': 'Carlos Orejuela', 'age': 19, 'carreer': 'Industrial Engineer', 'salary': 2256, 
    # 'yrs_tobuyhouse': 18, 'yrs_tobuycar': 8}]
    for i in database:
        for good, value in dic.items():
            save = i['salary']*percentage
            good_years = int((value / save) / 12)
            i[f'yrs_tobuy{good}'] = good_years
    print(database)

def improve_your_finances(nested_list):
    print("""
The most recommended in the personal finance is to save 30% of your salary.
From here you can save to buy a new house, a new car, etc.
And this program calculates how many years each person can buy it. 
""")
    percentage_saving = 0.3
    house_price = int(input("House's price: "))
    car_price = int(input("Car's price: "))
    dic_goods = {
        'house': house_price,
        'car': car_price,
    }
    calculate_years(nested_list, dic_goods, percentage_saving)

def carreer_and_salary(dic, number):
    carreer = {
        1: ['Industrial Engineer', 2256],
        2: ['Architect', 2206],
        3: ['Management', 1200],
        4: ['Data Science', 8333],
    }
    for k, v in carreer.items():
        if k == number:
            dic['carreer'] = v[0]
            dic['salary'] = v[1]

def database(nested_list):
    #neste_list = [{'name': 'Carlos', 'age': 19, 'carreer': 'Architect', 'salary': 2206}]
    for i in nested_list:
        if i['name'][0] == 'C':
            carreer_and_salary(i, 1)
        elif i['name'][0] == 'M':
            carreer_and_salary(i, 2)
        elif i['name'][0] == 'L':
            carreer_and_salary(i, 3)
        elif i['name'][0] == 'G':
            carreer_and_salary(i, 4)
    improve_your_finances(nested_list)

def str_name_age(figure_or_character):
    # ['c', 'a', 'r', 'l', 'o', 's'] -> figure_or_character = 'Carlos'
    # ['1', '9'] -> int(figure_or_character) = 19
    figure_or_character = "".join(figure_or_character)
    if figure_or_character.isnumeric():
        return int(figure_or_character)
    else:
        figure_or_character = figure_or_character.strip()
        return figure_or_character

def check_character_or_number(var_1):
    # 'Carlos, 19' -> characters_name_list = ['c', 'a', 'r', 'l', 'o', 's']
    # 'Carlos, 19' -> figure_name_list = ['1', '9']
    characters_name_list = []
    figure_age_list = []
    for character in var_1:
        if (character.isnumeric() == False
            and character != ','):
            characters_name_list.append(character)
        elif character.isnumeric():
            figure_age_list.append(character)
        else:
            continue
    return characters_name_list, figure_age_list

def structure_data(data):
    #First: dic = {'name': 'Carlos', 'age': 19}
    #Second: final_list = [{'name': 'Carlos', 'age': 19},
    #{'name': 'Fernando', 'age': 22}, ...]
    final_list = []                         
    for i in data:                          # i = 'Carlos Orejuela, 19' 
        dic = {}
        name_or_age = check_character_or_number(i)
        name = str_name_age(name_or_age[0])
        dic['name'] = name  
        age = str_name_age(name_or_age[1])
        dic['age'] = age
        final_list.append(dic)
    database(final_list)

def run():
    with open("./database.txt", 'r', encoding="utf-8") as f:
        data = [i.strip("\n") for i in f]
    structure_data(data)

if __name__=='__main__':
    run()