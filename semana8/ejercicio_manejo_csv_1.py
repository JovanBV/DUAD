import csv


def type_information(game_list):
    for dictionary in game_list:
        for key in dictionary:
            dictionary[key] = input(f'Type the {key}: ')


def create_dictionaries(game_list, game_headers, amount_of_games):
    while len(game_list) < amount_of_games:
        game_list.append(dict.fromkeys(game_headers))


def write_csv_file(file_path, game_list, game_headers):
    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, game_headers)
        writer.writeheader()
        writer.writerows(game_list)


def request_amount_of_games():
    while True:
        try:
            amount_of_games = int(input('Type the amount of games you want to list: '))
            if amount_of_games > 0:
                return amount_of_games
        except:
            print('Please enter a number greater than 0.')


def main():
    game_headers = ['Name', 'Genre', 'Developer', 'Classification ESRB']
    game_list = []
    amount_of_games = 0
    file_path = 'C:/Users/jovan/Documents/Python//games_list.txt'

    amount_of_games = request_amount_of_games()
    create_dictionaries(game_list, game_headers, amount_of_games)
    type_information(game_list)
    write_csv_file(file_path, game_list, game_headers)

main()