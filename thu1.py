import pandas as pd
import numpy as np

#đọc dữ liệu từ file
data = pd.read_csv('E:/C data/Numpy/Data Analyst/top_rated_9000_movies_on_TMDB.csv')

#chuyển dữ liệu thành mảng numpy
data_array = data.to_numpy()

data['release_date'] = pd.to_datetime(data['release_date'], format='%d/%m/%Y', errors='coerce')

def function_one():
    print("Tìm phim theo ngôn ngữ")
    #lấy ra các ngôn ngữ có trong bảng dữ liệu
    languages = data['original_language'].unique()
    print("Các ngôn ngữ có trong Data: ", languages)
    
    #nhập ngôn ngữ người dùng muốn tìm
    user_input_language = input("Nhập ngôn ngữ bạn muốn tìm: ")
    if user_input_language in languages:
        result = data[data['original_language'] == user_input_language]
        print("Các phim có ngôn ngữ '{}': ".format(user_input_language))
        
        result_array = result.to_numpy()
        for row in result_array:
            print(row)
    else:
        print("Ngôn ngữ không có trong dữ liệu")

def function_two():
    print("Tìm phim theo điểm đánh giá trung bình")
    try:
        #nhập điểm số cần tìm
        user_input_score = float(input("Nhập điểm số bạn muốn tìm: "))
        #chuyển dữ liệu sang mảng numpy
        avg_score = data['vote_average'].to_numpy()
        #tìm các điểm >= điểm nhập vào
        higher_score = avg_score >= user_input_score
        
        #lấy dữ liệu phim
        result = data[higher_score]
        
        if not result.empty:
            print("Các phim có điểm từ {:.1f}: ".format(user_input_score))
            
            result_array = result.to_numpy()
            for row in result_array:
                print(row)
        else:
            print("không có phim nào có điểm đánh giá cao hơn bạn chọn")
        
    except ValueError:
        print("Nhập điểm số hợp lệ")    

def function_three():
    print("Tìm phim theo năm sản xuất")
    year = int(input("Nhập năm bạn muốn tìm: "))
    
    # Lấy năm từ cột release_date
    release_years = data['release_date'].dt.year
    result = data_array[release_years == year]

    if result.size > 0:
        print(f"Các phim được phát hành trong năm {year}:")
        for row in result:
            print(row)
    else:
        print(f"Không tìm thấy phim nào phát hành trong năm {year}.")
               
def function_four():
    print("Tìm phim theo điểm phổ biến")
    try:
    
        #Nhập điểm đánh giá phổ biến
        user_input_popularity = float(input("Nhập điểm đánh giá mức độ phổ biến của phim: "))
    
        #lấy điểm pop
        popularity_score = data['popularity'].to_numpy()
    
        #so sánh điểm
        higher_popularity = popularity_score>= user_input_popularity
    
        result = data[higher_popularity]
    
        if not result.empty:
                print("Các phim có điểm đánh giá phổ biến (popularity) từ {:.1f}".format(user_input_popularity))
                result_array = result.to_numpy()
                for row in result_array:
                    print(row)
        else:
                print("Không có phim nào có điểm đánh giá phổ biến (popularity) lớn hơn {:.1f}".format(user_input_popularity))
    except ValueError:
        print("Nhập điểm đánh giá phổ biến hợp lệ")  

while True:
    try:
        print("Chọn chức năng khai thác thông tin phim")
        print("1. Tìm phim theo ngôn ngữ")
        print("2. Tìm phim theo điểm đánh giá trung bình")
        print("3. Tìm phim theo năm sản xuất")
        print("4. Tìm phim theo điểm phổ biến")
        print("5. Kết thúc")

        choice = int(input("Nhập lựa chọn của bạn: "))
        
        if choice == 1:
            function_one()
        elif choice == 2:
            function_two()
        elif choice == 3:
            function_three()
        elif choice == 4:
            function_four()
        elif choice == 5:
            print("Chương trình kết thúc.")
            break  # Thoát khỏi vòng lặp
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập từ 1 đến 5.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

