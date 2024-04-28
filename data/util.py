import subprocess
import os
import polars as pl


def create_df(file: str, project_name: str) -> pl.DataFrame:
    uuid = file.split('.')[0]
    df = pl.read_csv(file, separator='\t', truncate_ragged_lines=True)
    return df.with_columns(project=pl.lit(project_name), uuid=pl.lit(uuid))


if __name__ == '__main__':
    # take all files out
    curdir = os.getcwd()
    project_name = curdir.split('/')[-1]
    print(f'on {os.environ["SHELL"]}')
    print(f"[+] at: {curdir}")
    print(f"project name: {project_name}")

    if input("proceed? [y/n]") == 'y':
        subprocess.run(r'find . -type f -exec mv {} . \;', shell=True)
        subprocess.run('rm *parcel anno*', shell=True)
        # remove all dirs
        subprocess.run('find . -type d | xargs rm -rf', shell=True)

    files = os.listdir()
    dfs = [
        create_df(x, project_name) for x in files
    ]
    df = pl.concat(dfs)
    df = df.with_columns()
    print(df.head())

    if input("proceed? [y/n]") == 'y':
        df.write_parquet(f'../dfs/{project_name.lower()}.parquet')
