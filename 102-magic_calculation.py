def calculate_result(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result = result + (a / b) ** i
        except:
            result = result + (a + b)

    return result