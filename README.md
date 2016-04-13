Artificial Intelligence Course's Project

----------------------------------------------------------------------
# Fill-in-Station
----------------------------------------------------------------------
1. [Introduction](#introduction)
2. [Problem](#problem) 
3. [Software Requirements](#software-requirements)
4. [Input Output](#input-output)
5. [Code Details](#code-details)
6. [Run Code](#run-code)
7. [Special Attention](#special-attention)


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

-Python 2.6.9

Link Download: https://www.python.org/download/releases/2.6.9/

Hướng dẫn cài đặt: https://docs.python.org/2/using/

----------------------------------------------------------------------
### Input Output
----------------------------------------------------------------------

1. Input

Là tập tin đầu vào của chương trình. File input gồm 100 dòng, mỗi dòng là 1 tập gồm 9 chữ cái. File input được tạo bởi hàm generate_input.py

2. Output

Output được in ra trên cmd.( Cách chạy sẽ được nói chi tiết ở phần sau) Output gồm có kết quả của trò chơi là 1 ma trận 3x3 với các ô chữ thỏa mãn yêu cầu của trò chơi hoặc là sẽ in ra "Cannot find any solution" nếu không tìm được kết quả của bài toán

Ngoài ra, nếu trò chơi có lời giải, màn hình sẽ in ra thời gian để tìm câu trả lời và số node đi qua để tìm đáp án.

----------------------------------------------------------------------
### Code Details
----------------------------------------------------------------------

Trong python folder

1. 3_letters_dictionary

  Danh sách tất cả các từ có 3 chữ cái trong từ điển ( 972 từ)
  
2.  bigram_frequence_list

  Tần suất xuất hiện của các chữ cái trong từ điển
  
3. effective_branching_factor.py

  Chứa hàm đánh giá effective branching factor thuật toán heuristic
  
4. generate_input.py

  Hàm tạo 100 input ngẫu nhiên cho bài toán. 
  
  Do thực nghiệm chỉ ra việc tạo 100 input ngẫu nhiên sẽ có nhiều trường hợp không tìm được kết quả. Vì để tăng khả năng kiểm tra thuật toán, mỗi dòng sẽ được tạo bằng cách chọn 3 dòng trong từ điển và kiểm tra 5 ràng buộc còn lại. Nếu thỏa mãn thì sẽ điền ra file input 
  
5. input - tập tin đầu vào

  Kết quả sau khi chạy hàm generate_input.py - 100 input ngẫu nhiên cho bài toán
  Gồm có 100 dòng - mỗi dòng là tập 9 chữ cái được trộn ngẫu nhiên từ lời giải
  
6. fill_in_station.py

  Chứa lớp mô tả bài toán và giải thuật chương trình - gồm có 2 hàm heuristic là thông thường và nâng cao
  
7. experiment.py

  Hàm chạy ra thời gian trung bình và kết quả EBF trung bình của 2 hàm heuristic thông thường và nâng cao với đầu vào là file input


----------------------------------------------------------------------
### Run Code
----------------------------------------------------------------------

B1: Vào folder python trong project

B2: Chạy lệnh trên command line hoặc terminal trong folder python đấy

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

6. Chạy hàm đánh giá thời gian trung bình và giá trị EBF trung bình của 2 hàm đánh giá thường và nâng cao với input được khởi tạo như trên

python experiment.py

7. Để xuất kết quả từ màn hình dòng lệnh ra file thêm "> filename" và sau mỗi lệnh, ví dụ

python fill_in_station.py input 3_letters_dictionary bigram_frequence_list advanced_heuristic > log.txt

----------------------------------------------------------------------
### Special Attention
----------------------------------------------------------------------

1. Code được viết trên python 2.6 nên nếu chạy python 3.0 trở lên, rất có thể sẽ gặp lỗi

2. Khi chạy chương trình giải quyết trò chơi, phải nhập đủ các tham số như trong hướng dẫn

3. Nếu chưa có input, phải khởi tạo input trước khi chạy chương trình 
