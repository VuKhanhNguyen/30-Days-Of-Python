#numpy
'''numpy là một trong những thư viện phổ biến nhất trong cộng đồng học máy (machine learning) và khoa học dữ liệu (data science).

NumPy là gói cơ bản cho tính toán khoa học với Python.

một đối tượng mảng N chiều mạnh mẽ

các hàm tinh vi (hỗ trợ phát sóng - broadcasting)

công cụ để tích hợp mã C/C++ và Fortran

các khả năng đại số tuyến tính, biến đổi Fourier, và tạo số ngẫu nhiên hữu ích '''

import webbrowser
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]
for url in url_lists:
    webbrowser.open_new_tab(url)
    
# để xóa 1 packet thì dùng pip uninstall tên packet

# pip list # để xem các packet đã cài đặt

# pip show tên packet # để xem thông tin chi tiết về 1 packet đã cài đặt

# pip show --verbose tên packet # để xem thông tin chi tiết về 1 packet đã cài đặt, bao gồm cả các packet phụ thuộc (dependencies) của nó
    
# pip freeze # để xem danh sách các packet đã cài đặt và phiên bản của chúng, có thể dùng để tạo file requirements.txt    
    
    
# request
# pip install requests # để cài đặt thư viện requests, một thư viện phổ biến để gửi yêu cầu HTTP trong Python
#trong requests modules có các phương thức như:
#get() # để gửi yêu cầu GET đến một URL và nhận phản hồi từ máy chủ
#status_code() # để kiểm tra mã trạng thái của phản hồi từ máy chủ, cho biết yêu cầu đã thành công hay không
#text() # để lấy nội dung của phản hồi dưới dạng chuỗi văn bản
#headers() # để lấy thông tin tiêu đề của phản hồi từ máy chủ, bao gồm các thông tin như loại nội dung, mã trạng thái, v.v.
#json() # để chuyển đổi nội dung của phản hồi thành định dạng JSON


import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response) # <Response [200]>
print(response.status_code) # 200 # mã trạng thái 200 cho biết yêu cầu đã thành công
print(response.headers) # thông tin tiêu đề của phản hồi từ máy chủ
print(response.text)    # nội dung của phản hồi dưới dạng chuỗi văn bản

import requests
url = 'https://restcountries.com/v3.1/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])
# với json() ta có thể chuyển đổi nội dung của phản hồi thành định dạng JSON, giúp dễ dàng xử lý dữ liệu hơn
# với html, xml, txt,... thì có thể dùng text() để lấy nội dung của phản hồi dưới dạng chuỗi văn bản



'''from pythonLearning.30daysofPython.30_Days_Of_Python_NVK.30_Days_Of_Python.day20_python_packet_manager import arithmetic'''













