import pandas as pd
import functions_machine_learning as fml
from PIL import Image

# 1. Google drive directory of each team member
#directory_aurelien =
#directory_alexandre =
#directory_marion =
#directory_mohammed =

# 2. Declare csv clean directories
link_title_akas_clean = f"{directory_aurelien}title_akas_clean.csv"
link_title_basics_clean = f"{directory_aurelien}title_basics_clean.csv"
link_title_genre_clean = f"{directory_aurelien}title_genre_clean.csv"
link_name_basics_clean = f"{directory_aurelien}title_nameBasics_clean.csv"
link_name_basics_keys = f"{directory_aurelien}title_nameBasics_clean.csv"
link_title_principals_clean = f"{directory_aurelien}title_principals_clean.csv"
link_title_rating_clean = f"{directory_aurelien}title_ratings_clean.csv"

# 3. Generate dataframe from custom function
df_title_akas_clean = fml.read_database(link_title_akas_clean, ",")
df_title_basics_clean = fml.read_database(link_title_basics_clean, ",")
df_title_genre_clean = fml.read_database(link_title_genre_clean, ",")
df_name_basics_clean = fml.read_database(link_name_basics_clean, ",")
df_name_basics_keys = fml.read_database(link_name_basics_keys, ",")
df_title_principals_clean = fml.read_database(link_title_principals_clean, ",")
df_title_rating_clean = fml.read_database(link_title_rating_clean, ",")

# 4. import dashboard image
link_dashboard_picture = f"G:\\.shortcut-targets-by-id\\1ISrfbm7zzuVqO7_ibsR8dnoL6hna0X6B\\PROJET 2\\Dashboard\\cinema.jpg"
dashboard_img = Image.open(link_dashboard_picture)

