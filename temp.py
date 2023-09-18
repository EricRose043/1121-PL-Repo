import pandas as pd

# 設定 CSV 檔案的路徑
csv_file_path_PL = 'plane.csv'
csv_file_path_WEB = 'chisel.csv'


# 使用 pandas 的 read_csv 函式讀取 CSV 檔案並將其轉換為 DataFrame
df_PL = pd.read_csv(csv_file_path_PL)
df_WEB = pd.read_csv(csv_file_path_WEB)
# 從 DataFrame 中取出學生名稱欄位，假設欄位名稱為 '學生名稱'，你可以根據實際情況調整
student_names_PL = df_PL['love']
student_names_WEB = df_WEB['love']


# 將學生名稱轉換為 set 資料型態
student_names_PL_set = set(student_names_PL)
student_names_WEB_set = set(student_names_WEB)

#同時選了PECU的程式語言和網際網路概論的學生是哪幾位
print( student_names_PL_set & student_names_WEB_set )
print( student_names_PL_set | student_names_WEB_set )
print( student_names_PL_set - student_names_WEB_set )