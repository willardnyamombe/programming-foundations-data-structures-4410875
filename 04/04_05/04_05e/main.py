# longest answer
# def has_unique_characters(data):
#     my_data_set = set()
#     the_list = []
#     for char in data:
#         my_data_set.add(char)
#         the_list.append(char)
#     if len(the_list) != len(my_data_set):
#         return False
#     else:
#         return True
    
# shortest answer
def has_unique_characters(data):
    unique_set = set(data)
    return len(unique_set) == len(data)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
