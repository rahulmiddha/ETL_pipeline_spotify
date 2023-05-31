import return_df
import pandas as pd


def check_null(load_df):
    if load_df.empty:
        print("No songs extracted")
        return False
    else:
        print("Songs returned")


if __name__ == "__main__":
    # argument can be either tracks or artists
    load_df = return_df.return_data("tracks")
    # print(load_df)
    check_null(load_df)
