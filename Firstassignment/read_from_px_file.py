import px_reader

px_obj = px_reader.Px("akay_001_200900.px")

df = px_obj.pd_dataframe()
print(df)