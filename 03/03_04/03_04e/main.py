user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# O(n) option 1
# def update_preferences(user_pref):
#     new_user_pref = {}
#     for key, value in user_pref.items():
#         if value != None:
#             new_user_pref[key] = value
         
#     return new_user_pref

#option 2 comprehension
def update_preferences(user_pref):
         
    return { key: value for key, value in user_pref.items() if value is not None }

print(update_preferences(user_preferences))
