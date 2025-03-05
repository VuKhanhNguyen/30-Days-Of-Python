my_dict = {"a": 1, "b": 2, "c": 3}

# Xóa và lấy giá trị của key "b"
value = my_dict.pop("b")
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# Xóa một key không tồn tại với giá trị mặc định
value = my_dict.pop("d", "Not Found")
print(value)  # Output: Not Found