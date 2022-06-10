#A los cuantos años tendrá su casa y su carro

def save_recommended(dic_unableperson, good_price):
    dic_percentage = {}
    save_percentage = 0.3
    years = 0
    for k, v in dic_unableperson.items():
        save = v*save_percentage
        years = int(round((good_price/save) / 12, 0))
        while (years > 10):
            save_percentage += 0.1
            save = v*save_percentage
            years = int(round((good_price/save) / 12, 0))
        if round(save_percentage, 0) < 0.8:
            dic_percentage[k] = (save_percentage*100)
    return dic_percentage

def unable_topayit(list, base, good_price):
    unable_person_topayit = {}
    for i in list:
        dic = {i: key['salary'] for key in base if key['yrs_tobuyhouse']>10 and i == key['name']}
        unable_person_topayit = unable_person_topayit | dic
    return save_recommended(unable_person_topayit, good_price)

def second_filter_data(database):
    print("""
If you want to save more to buy a house or car is fine, but save more than 80% of your salary isn't a good idea.
For this reason, is better if you don't buy that house or car.

SUITABLE CASES:
""")
    unprofitable_house = [person['name'] for person in database if person['yrs_tobuyhouse']>10]
    unprofitable_car = [person['name'] for person in database if person['yrs_tobuycar']>10]
    unable_person_house = unable_topayit(unprofitable_house, database, 120000)
    unable_person_car = unable_topayit(unprofitable_car, database, 55000)
    print('HOUSE---------------------------------------------')
    for key, value in unable_person_house.items():
        print(f"""{key} must save {value}% of his salary to buy the 120k house in less 10 years 
or equal to this amount
        """)
    print('CAR-----------------------------------------------')
    for key, value in unable_person_car.items():
        print(f"""{key} must save {value}% of his salary to buy the 55k car in less 10 years 
or equal to this amount
        """)

def first_filter_data(database):
    profitable_house = list(filter(lambda person : person['yrs_tobuyhouse'] <= 10, database))
    profitable_car = list(filter(lambda person : person['yrs_tobuycar'] <= 10, database))
    person_capable_house = list(map(lambda person: person['name'], profitable_house))
    person_capable_car = list(map(lambda person: person['name'], profitable_car)) 
    print(f"""
------------------------------------------------------------------------------    
People able to buy a $150k house in less than 10 years or equal to this amount 
and saving 30% of his salary: {person_capable_house}                           
------------------------------------------------------------------------------
""")
    print(f"""
------------------------------------------------------------------------------
People able to buy a $45k car in less than 10 years or equal to this amount 
and saving 30% of his salary: {person_capable_car}
------------------------------------------------------------------------------
""")
    second_filter_data(database)

def calculate_years(database, dic, percentage):
    #database = [{'name': 'Carlos Orejuela', 'age': 19, 'carreer': 'Industrial Engineer', 'salary': 2256, 
    # 'yrs_tobuyhouse': 18, 'yrs_tobuycar': 8}]
    for i in database:
        for good, value in dic.items():
            save = i['salary']*percentage
            good_years = int(round((value / save) / 12, 0))
            i[f'yrs_tobuy{good}'] = good_years
    print(f"""Database constructed: 
{database}""")
    first_filter_data(database)

def improve_your_finances(nested_list):
    print("""
The most recommended in the personal finance is to save 30% of your salary.
From here you can save to buy a new house, a new car, etc.
And this program calculates how many years each person can buy it. 
""")
    percentage_saving = 0.3
    try:
        house_price = 120000
        car_price = 55000         
        dic_goods = {
            'house': house_price,
            'car': car_price,
        }
        calculate_years(nested_list, dic_goods, percentage_saving)
    except ValueError:
        print("It's not allowed str")

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