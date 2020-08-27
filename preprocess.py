# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Laboratorio #4 - Análisis de sentimientos
# * Oscar Juárez - 17315
# * José Pablo Cifuentes - 17509
# * Paul Belches - 17088

# %%
import pandas as pd
import re


# %%
df = pd.read_csv('./files/GrammarandProductReviews.csv')
print([var for var in df])


# %%
clean_df = df[['brand', 'manufacturer', 'name', 'reviews.username',
               'reviews.didPurchase', 'reviews.doRecommend', 'reviews.rating', 'reviews.text']].copy()

# %%
clean_reviews = []

for line in clean_df['reviews.text']:
    line = str(line)
    # Quitar saltos de linea y convertirlo a minusculas
    line = line.rstrip('\n').lower()
    # Quitar URLS
    line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
    # Quitar el resto de expresiones regulares, excepto . ? ! y '
    line = re.sub(r"[^\w.?!\d'\s]", '', line)
    # Quitar números
    line = re.sub(' \d+', ' ', line)
    # Quitar espacios extra
    line = line.strip(' \t\n\r')
    # Reemplazar ! y ? por puntos.
    line = line.replace('!', '.').replace('?', '.')
    # Quitar multiples puntos por solo uno
    line = re.sub(r'\.+', ".", line)
    # Finalmente, quitamos apostrofes
    line = line.replace("'", '')

    clean_reviews.append(line)


# %%
clean_df['reviews.text'] = clean_reviews


# %%
df = pd.DataFrame(clean_df)
df.to_csv('./files/CleanData.csv', index=False)
