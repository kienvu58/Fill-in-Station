Artificial Intelligence Course's Project

----------------------------------------------------------------------
# Fill-in-Station
----------------------------------------------------------------------
1. [Introduction](#introduction)
2. [Problem](#problem) 
3. [Software Requirements](#software-requirements)
4. [Code Detail](#code-detail)
5. [Run Code](#run-code)


----------------------------------------------------------------------
### Introduction
----------------------------------------------------------------------

Bài tập lớn môn trí tuệ nhân tạo đòi hỏi sinh viên vận dụng các kiến thức về chiến thuật tìm kiếm để giải quyết trò chơi có tên là Fill-in Station.

Báo cáo này trình bày code ,cách chạy chiến thuật để giải quyết bài toán Fill-in Station và các đánh giá về chiến thuật được sử dụng 


----------------------------------------------------------------------
### Problem
----------------------------------------------------------------------

Fill-in Station là một trò chơi ô chữ bắt đầu bằng một ma trân 3x3 và 9 chữ cái (chữ cái có thể lặp lại trong danh sách này). Công việc của bạn là viết chương trình giúp bạn điền các chữ cái vào ma trận 3x3 sao cho nếu ta xếp các chữ cái theo hướng của mũi tên thì các chữ cái này tạo thành một từ có nghĩa. 


----------------------------------------------------------------------
### Software Requirements
----------------------------------------------------------------------

-Python 2.7.11

Link Download: https://www.python.org/downloads/release/python-2711/

Hướng dẫn cài đặt: https://docs.python.org/2/using/


----------------------------------------------------------------------
### Code Detail
----------------------------------------------------------------------

Trong python folder

1. 3_letters_dictionary

  Danh sách tất cả các từ có 3 chữ cái trong từ điển ( 972 từ)
  
2.  bigram_frequence_list

  Tần suất xuất hiện của các chữ cái trong tiếng anh
  
3. effective_branching_factor.py

  Hàm đánh giá thuật toán heuristic
  
4. generate_input.py

  Hàm tạo 100 input ngẫu nhiên cho bài toán
  
5. input

  Kết quả sau khi chạy hàm generate_input.py - 100 input ngẫu nhiên cho bài toán
  
6. fill_in_station.py

  Hàm giải thuật chương trình - gồm có 2 hàm heuristic là thông thường và nâng cao
  
7. experiment.py

  Hàm chạy ra thời gian trung bình và kết quả EBF trung bình của hàm heuristic thông thường và nâng cao


----------------------------------------------------------------------
### Run Code
----------------------------------------------------------------------

B1: Vào folder python trong project

B2: Chạy lệnh trên cmd trong folder python đấy
Các lệnh:
1. Khởi tạo input
python generate_input.py

2. Chạy chương trình giải quyết bài toán bằng hàm đánh giá thường 
python fill_in_station.py input 3_letters_dictionary bigram_frequence_list normal_heuristic

3. Chạy chức năng truy vết khi chương trình giải quyết bài toán hàm toán đánh giá thường
python fill_in_station.py input 3_letters_dictionary bigram_frequence_list normal_heuristic -trace

4. Chạy chương trình giải quyết bài toán bằng hàm đánh giá nâng cao
python fill_in_station.py input 3_letters_dictionary bigram_frequence_list advanced_heuristic

5. Chạy chức năng truy vết khi chương trình giải quyết bài toán bằng hàm đánh giá nâng cao
python fill_in_station.py input 3_letters_dictionary bigram_frequence_list advanced_heuristic -trace

6. Chạy hàm đánh giá thời gian trung bình và giá trị EBF trung bình của 2 hàm đánh giá thường và nâng cao
python experiment.py
