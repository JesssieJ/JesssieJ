import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def convert_csv_to_parquet(source_folder, target_folder):
    """
    Converts all CSV files in the source folder to Parquet files and stores them in the target folder.
    Only converts files that haven't already been converted.
    After conversion, the original CSV file is deleted to save space.
    """
    # Get a list of all CSV files in the source folder
    csv_files = [f for f in os.listdir(source_folder) if f.endswith('.csv')]

    # Convert each CSV file to Parquet
    for csv_file in csv_files:
        # Define the source and target file paths
        source_file_path = os.path.join(source_folder, csv_file)
        # parquet_filename = os.path.splitext(csv_file)[0] + '.parquet'
        parquet_filename = csv_file.replace('.csv', '.parquet')
        target_file_path = os.path.join(target_folder, parquet_filename)

        # Check if the Parquet file already exists
        if not os.path.exists(target_file_path):
            print(f"Converting {csv_file} to Parquet format.")
            # Read the CSV file into a DataFrame
            df = pd.read_csv(source_file_path,sep=';')
            # Convert the DataFrame to a Parquet file
            df.to_parquet(target_file_path)

            # Delete the original CSV file to save space
            os.remove(source_file_path)
            print(f"Deleted original CSV file: {csv_file}")
        # else:
        #     print(f"Parquet file for {csv_file} already exists. Skipping conversion.")

def get_source(target_folder, columns_to_merge):
    """
    Reads all Parquet files in the target folder, extracts specific columns, and merges them into a single DataFrame.
    """
    # Get a list of all Parquet files in the target folder
    parquet_files = [f for f in os.listdir(target_folder) if f.endswith('.parquet')]

    # Initialize an empty DataFrame for the final merged data
    dfs = []

    # Read each Parquet file and concatenate the specific columns
    for parquet_file in parquet_files:
        file_path = os.path.join(target_folder, parquet_file)
        df = pd.read_parquet(file_path, columns=columns_to_merge)
        dfs.append(df)

    # Concatenate all DataFrames from the list
    merged_df = pd.concat(dfs, ignore_index=True)

    return merged_df

source_folder = r'/Users/jessie/Desktop/test/source'
target_folder = r'/Users/jessie/Desktop/test/parquet'

convert_csv_to_parquet(source_folder, target_folder)