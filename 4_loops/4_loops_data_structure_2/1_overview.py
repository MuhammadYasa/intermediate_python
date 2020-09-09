# for biasa
import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
# for val in brics:
#     print(val)

print('\nitterows')
# itterows
for lab, row in brics.iterrows():
    print(lab)
    print(row)

# selective print
print('\n')
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

# add column
# kalau datanya sedikit tidak masalah, tp kalau datanya banyak itu jd masalah,
# karena harus di loop di setiap iterasi
print('\ndengan cara loc')
for lab, row in brics.iterrows():
    # - Creating Series on every iteration
    brics.loc[lab, "name_lenght"] = len(row["country"])
print(brics)

# apply
# kalau untuk menambah column yg berisi len tanpa iterasi di setiap loop
# dapat dilakukan dngn cara seperti ini, cocok untuk data yg banyak
print('\ndengan cara apply')
brics["panjang_nama"] = brics["capital"].apply(len)
print(brics)