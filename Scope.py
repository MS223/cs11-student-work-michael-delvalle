# my_list = ['a', 'b', 'c', 'd']
# # input: a list of strings
# # output: None
# def my_function(list_argument):
# 	list_argument[0] = 'z'
# print(my_list)
# my_function(my_list)
# print(my_list)

# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
#It prints out the list 1,2,3,4,5 but replaced the 4 with "yo"

var_1 = "kittens" #Global
var_2 = "cookies" #Global
# input: a string
# output: a string
def my_function(my_favorite_things): #Global
    song_lyrics = "rain drops on roses," #Local
    combined_song = song_lyrics + my_favorite_things #Local
    return combined_song
# input: a string
# output: a string
def my_function_2(item, item2): #Global
    full_lyrics = item + "on " + item2 #Local
    full_song = my_function(full_lyrics) #Local
    return full_song
my_song = my_function_2(var_1, var_2) #global

var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    elif favorite_pet == var_2:
        print("My favorite pet is the dog.")
    var_2 = "cat"

print_out_my_favorite(var_1)
print(var_2)

#var_2 is repeated/defined multiple times. You can make it an elif statement

