- 👋 Hi, I’m @JesssieJ
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
JesssieJ/JesssieJ is a ✨ special ✨ repository because its `README.md` (this file) 


import pandas as pd
from pathlib import Path

# 设置CSV文件所在的文件夹路径
folder_path = Path('/path/to/your/csv/folder')

# 列出文件夹中所有的CSV文件
csv_files = folder_path.glob('*.csv')

# 初始化一个空的DataFrame列表，用于存储每个CSV文件的数据
dfs = []

# 遍历CSV文件列表，读取每个文件，然后添加到DataFrame列表中
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# 合并所有DataFrame到一个单一DataFrame中
combined_df = pd.concat(dfs, ignore_index=True)

# 现在combined_df包含所有CSV文件的数据，可以进行进一步的处理或分析


import pandas as pd
from pathlib import Path

# 设置父文件夹路径
parent_folder_path = Path('/path/to/your/parent/folder')

# 使用rglob方法递归地搜索所有CSV文件
csv_files = parent_folder_path.rglob('*.csv')

# 初始化一个空的DataFrame列表，用于存储每个CSV文件的数据
dfs = []

# 遍历CSV文件列表，读取每个文件，然后添加到DataFrame列表中
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# 合并所有DataFrame到一个单一DataFrame中
combined_df = pd.concat(dfs, ignore_index=True)

# combined_df现在包含所有子文件夹中CSV文件的数据



import pandas as pd
import os

# 设置父文件夹路径
parent_folder_path = '/path/to/your/parent/folder'

# 初始化一个空的DataFrame列表，用于存储每个CSV文件的数据
dfs = []

# 使用os.walk遍历父文件夹下的所有子文件夹
for subdir, dirs, files in os.walk(parent_folder_path):
    for file in files:
        if file.endswith('.csv'):
            # 构建完整的文件路径
            file_path = os.path.join(subdir, file)
            # 读取CSV文件并添加到列表中
            df = pd.read_csv(file_path)
            dfs.append(df)

# 合并所有DataFrame到一个单一DataFrame中
combined_df = pd.concat(dfs, ignore_index=True)

# combined_df现在包含所有子文件夹中CSV文件的数据


import os

# 设置你的文件夹路径
folder_path = '你的文件夹路径'

# 遍历文件夹
for root, dirs, files in os.walk(folder_path):
    # 检查当前root是否是以"2023"开头的子文件夹
    if os.path.basename(root).startswith("2023"):
        for filename in files:
            print(os.path.join(root, filename))

import re

# 假设我们有以下的文件名列表
file_names = [
    'report20230207.docx',
    'summary2023-02-07.txt',
    'data_20230208.csv',
    # 其他文件名...
]

# 定义一个正则表达式来匹配日期格式 YYYYMMDD 或 YYYY-MM-DD
date_pattern = re.compile(r'\d{4}-?\d{2}-?\d{2}')

# 提取日期并收集到一个列表中
dates = []
for file_name in file_names:
    match = date_pattern.search(file_name)
    if match:
        dates.append(match.group())

# 打印所有提取到的日期
print(dates)

