import pandas as pd
import os


def combine_salary_files(output_file='nba_salaries_combined.csv'):
    """
    Combines individual year CSV files into one consolidated file
    Expected file pattern: 'nba_salaries_YYYY.csv' (2000-2025)
    """
    # Get all matching files in current directory
    files = [f for f in os.listdir() if f.startswith('nba_salaries_') and f.endswith('.csv') and f != output_file]

    if not files:
        print("No individual year files found!")
        return

    print(f"Found {len(files)} year files to combine")

    # Read and combine all files
    dfs = []
    for file in files:
        try:
            df = pd.read_csv(file)
            dfs.append(df)
            print(f"Added {file} ({len(df)} records)")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not dfs:
        print("No valid data found in any files")
        return

    # Combine all DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)

    # Clean the combined data
    combined_df.drop_duplicates(inplace=True)
    combined_df = combined_df[combined_df['Salary'] > 0]  # Remove invalid entries

    # Save to new CSV
    combined_df.to_csv(output_file, index=False)
    print(f"\nSuccessfully created {output_file} with {len(combined_df)} total records")

    # Verify the output
    print("\nSample of combined data:")
    print(combined_df.head())


if __name__ == "__main__":
    combine_salary_files()