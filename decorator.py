promos = []


def promotion(promo_func):
    print(f'Promo: {promo_func.__name__}')
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(value):
    return value * 0.05 if value > 100 else 0


@promotion
def fidelity2(value):
    return value * 0.1 if value > 200 else 0


@promotion
def fidelity3(value):
    return value * 0.2 if value > 200 else 0


promos_name = [promo.__name__ for promo in promos]
promos_value = [promo(200) for promo in promos]
max_promo = max(promo(200) for promo in promos)

zip_promos = zip(promos_name, promos_value)
print(max_promo)
for promo in zip_promos:
    print(promo)

print(fidelity(40))
