import os
import pandas as pd
import time


def convert_csv_to_parquet(source_folder, target_folder):
    """
    Converts all CSV files in the source folder to Parquet files and stores them in the target folder.
    Only converts files that haven't already been converted.
    After conversion, the original CSV file is deleted to save space.
    """
    csv_files = [f for f in os.listdir(source_folder) if f.endswith('.csv')]

    for csv_file in csv_files:
        source_file_path = os.path.join(source_folder, csv_file)
        # parquet_filename = os.path.splitext(csv_file)[0] + '.parquet'
        parquet_filename = csv_file.replace('.csv', '.parquet')
        target_file_path = os.path.join(target_folder, parquet_filename)

        # Check if the Parquet file already exists
        if not os.path.exists(target_file_path):
            print(f"Converting {csv_file} to Parquet format.")
            df = pd.read_csv(source_file_path
                             # ,sep=';'
                             )
            df.to_parquet(target_file_path)

            # Delete original CSV file
            os.remove(source_file_path)
            print(f"Deleted original CSV file: {csv_file}")
        # else:
        #     print(f"Parquet file for {csv_file} already exists. Skipping conversion.")

def get_source(target_folder, cols_to_merge):
    """
    Reads all Parquet files in the target folder, extracts specific columns, and merges them into a single DataFrame.
    """
    parquet_files = [f for f in os.listdir(target_folder) if f.endswith('.parquet')]
    dfs = []

    for parquet_file in parquet_files:
        file_path = os.path.join(target_folder, parquet_file)
        df = pd.read_parquet(file_path, columns=cols_to_merge)
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)

    return merged_df

source_folder = r'/Users/jessie/Desktop/test/source'
target_folder = r'/Users/jessie/Desktop/test/parquet'


import os
import glob
import pandas as pd

# 设置你的基础路径
base_path = '你的基础路径'  # 例如 '/path/to/folders'
output_base_path = '你的输出基础路径'  # 例如 '/path/to/output/folders'

# 确保输出目录存在
if not os.path.exists(output_base_path):
    os.makedirs(output_base_path)

# 找到所有以2023开头的文件夹
folders = glob.glob(os.path.join(base_path, '2023*'))

# 文件名中需要包含的字符串
includes = ['012tko', '216col']

# 遍历所有文件夹
for folder in folders:
    # 对于每个文件夹，找到所有符合条件的.bz2文件
    # 使用glob模式匹配所需文件
    pattern = os.path.join(folder, "*-Orders.csv.bz2")
    for file_path in glob.glob(pattern):
        # 检查文件名是否包含任一所需字符串
        if any(include in os.path.basename(file_path) for include in includes):
            # 读取.csv.bz2文件为pandas DataFrame
            df = pd.read_csv(file_path, compression='bz2')
            
            # 获得原始文件名，用于创建新的文件路径
            filename = os.path.basename(file_path)
            # 替换扩展名以构建新文件名
            new_filename = filename.replace('.csv.bz2', '.parquet')
            # 构建新的文件路径
            parquet_path = os.path.join(output_base_path, new_filename)
            
            # 将DataFrame写入.parquet文件
            df.to_parquet(parquet_path, engine='pyarrow', index=False)
            
            print(f'Converted {file_path} to {parquet_path}')



if __name__ == '__main__':

    start_time = time.time()
    convert_csv_to_parquet(source_folder, target_folder)
    end_time = time.time()
    run_time = end_time - start_time
    print(run_time)

    cols = ['date_received', 'product', 'sub_product']
    start_time = time.time()
    a = get_source(target_folder, cols)
    end_time = time.time()
    run_time = end_time - start_time
    print(run_time)



