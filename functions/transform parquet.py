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



