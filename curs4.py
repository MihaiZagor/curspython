# Curs 4 - memory savers
import copy

players = [{
    "first_name": "John",
    "last_name": "Doe",
    "rank": 3
}, {
    "first_name": "Kevin",
    "last_name": "McDonald",
    "rank": 1

}, {
    "first_name": "John",
    "last_name": "Ronnie",
    "rank": 2
}
]
sorted_players = sorted(players, key=lambda player: player["rank"])
print(sorted_players)


def check_top_3_players(player):
    updated_player = copy.deepcopy(player)
    updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
    return updated_player


players_with_top_3_value = map(check_top_3_players, players)
print(list(players_with_top_3_value))

first_list = [x for x in range(10)]
second_list = [x for x in range(10, 100, 10)]
third_list = [x for x in range(100, 1000, 100)]


for zip_item in zip(first_list, second_list, third_list):
    first_element, second_element, third_element = zip_item
    print(first_element, second_element, third_element)


first_list = [x for x in range(10)]
even_square_numbers = [ x ** 2 for x in first_list if x % 2 == 0 and x > 0]
print(even_square_numbers)


with open("hello.txt", "w") as file:
    file.write("Hello World!")
