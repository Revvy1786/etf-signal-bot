ticker = "VWCE"
prezzi = [110.2, 111.0, 109.8, 112.5, 113.1, 112.7, 114.0, 115.2, 114.6, 116.3]

print(f"Ticker: {ticker}")

giorni = len(prezzi)
print(f"Giorni: {giorni}")

primo = prezzi[0]
print(f"Primo: {primo}")

ultimo = prezzi[-1]
print(f"Ultimo: {ultimo}")

massimo = max(prezzi)
print(f"Massimo: {massimo}")

minimo = min(prezzi)
print(f"Minimo: {minimo}")

media = sum(prezzi) / giorni
print(f"Media: {round(media, 2)}")

variazione = (ultimo - primo) / primo * 100
print(f"Variazione: {round(variazione, 2)}%")