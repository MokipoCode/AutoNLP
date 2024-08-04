
#LOAD DATA

#APPLY MOD TO DATA

# #df = df.drop(columns=['county']) (county is 100% NaN)

# **IGNORE:** ❌
# - `url`: the URL of the listing on Craigslist (not used + URL from 2021...)
# - `image_url`: the URL of an image of the vehicle (not used + URL from 2021...)
# - `VIN`: the vehicle identification number (VIN) of the vehicle (UUID already provided by `id`)
# - `county`: the county where the listing was posted (all NaN)

# #NaN ignored by default
# df['year'] = pd.to_numeric(df['year'], errors="coerce").astype('Int64')

# df['odometer'] = pd.to_numeric(df['odometer'], errors="coerce").astype('Int64')

# #ISO 8601 format
# df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')

# #I need to run this line twice??


# df['post_day'] = df['posting_date'].dt.day.astype('Int64')
# df['post_month'] = df['posting_date'].dt.month.astype('Int64')
# df['post_year'] = df['posting_date'].dt.year.astype('Int64')

#SAVE DATA