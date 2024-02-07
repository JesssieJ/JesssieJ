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
