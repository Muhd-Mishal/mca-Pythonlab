my_dict={'apple':8,'banana':2,'orange':9,'grape':3}
ascending=dict(sorted(my_dict.items()))
descending=dict(sorted(my_dict.items(),reverse=True))
print("ascending order :",ascending)
print("descending order:",descending)