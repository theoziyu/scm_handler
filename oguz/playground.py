import pandas as pd

from dataframe_checker import DataframeChecker
csv_path = "dataframe.csv"

checker_object = DataframeChecker(csv_path)

checker_object.check_continuously()
"""
old_csv_file = pd.read_csv("dataframe.csv")
new_csv_file = pd.read_csv("new_dataframe.csv")

df2 = pd.DataFrame([["bayat", "666.666.6.6:1111", "False", "False", "False"]],
            columns=["camera_name", "camera_ip", "model_a", "model_b", "model_c"])

# new_csv_file = new_csv_file.append(df2, ignore_index=True)

wanted_row = old_csv_file[old_csv_file["camera_name"] == "ozlem"]

print(wanted_row["camera_ip"])
# def is_dataframe_changed(orig_df, new_df) -> bool:
#     orig_row_count = len(orig_df)
#     new_row_count = len(new_df)

#     if orig_row_count != new_row_count:
#         return True
#     else:
#         bool_df = (orig_df == new_df)
#         bool_df = bool_df[bool_df == False]
#         bool_df = bool_df.dropna(axis = 0, how = 'all')
#         if bool_df.empty:
#             return False
#         else:
#             return True

# print(is_dataframe_changed(old_csv_file, new_csv_file))
    

# new_csv_file = "new_dataframe.csv"

# csv_file.to_csv(new_csv_file, index=False)


"""