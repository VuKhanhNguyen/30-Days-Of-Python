strr = 'I am a teacher and I love to inspire and teach people'

# Chuyển về chữ thường
strr_lower = strr.lower()

# Lấy các từ duy nhất
unique_words = set(strr_lower.split())

# Lấy các ký tự duy nhất từ các từ duy nhất
unique_chars = set(''.join(unique_words))

print(unique_chars)