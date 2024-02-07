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
