def product(a, b):
    if a < 0:
        a *= -1
    else:
        if b < 0:
            b *= -1
    result = a * b
    print("Product of", a, "and", b, "equals", result)
    return result

def pre_product(a, b):
    if type(a) is int and type(b) is int:
        product_result = product(a, b)
    else:
        product_result = "Введены неверные параметры"
        print(product_result)
    return product_result


