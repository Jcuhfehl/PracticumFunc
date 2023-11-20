import math


def first_significant_figure(x: float) -> int:
    x = abs(x)
    print(x)
    while str(x)[0] == '0':
        x *= 10
    return int(str(x)[0])


def ceil_to_significant_figures(x: float, sigfigs: int):
    exponent = -exponent_scientific_notation(x)
    rounded_to_sigfigs = math.ceil(x*10**(exponent+sigfigs-1))
    return rounded_to_sigfigs/(10**(exponent+sigfigs-1))


def round_to_decimals(x: float, decimals: int) -> int:
    """
    Returns the integer representation of x rounded to the number of decimal
        places specified by decimals.
    :param x: a floating point number to round to decimal places
    :param decimals: an integer specifying the number of decimal places
    :return: an integer representing the rounded value of x
    """
    return round(x*10**decimals)/(10**decimals)


def exponent_scientific_notation(x: float) -> int:
    """
    Returns the exponent that would be used for the exponent in
        scientific notation
    :param x: a floating point number that the exponent will be extracted from
    :return: an integer representing exponent that would be used in
        scientific notation
    """
    return int(math.floor(math.log10(abs(x))))


def round_with_error(value: float, error: float) -> (float, float):
    """
    Returns a tuple containing the rounded value and rounded error of a
        floating point number with a given error term.
    :param value: a floating point number with an associated error term
    :param error: the error term of the value (as a float)
    :return: tuple containing the rounded value and rounded error of the value
    """
    if first_significant_figure(error) in [1, 2]:
        number_of_decimals = -exponent_scientific_notation(error) + 1
        error = ceil_to_significant_figures(error, 2)
    else:
        number_of_decimals = -exponent_scientific_notation(error)
        error = ceil_to_significant_figures(error, 1)
    value = round_to_decimals(value, number_of_decimals)
    return value, error


def format_value_with_error(value: float, error: float, unit: str = None) -> str:
    """
    Returns a string representing the formatted value and associated error term of a floating point number.
    :param value: a floating point number with an associated error term
    :param error: the error term of the value (as a float)
    :param unit: the unit in which to express the rounded value (optional)
    :return: a string representing the formatted value and associated error term of the value
    """
    value, error = round_with_error(value, error)
    value_exponent = exponent_scientific_notation(value)
    m_value, m_error = value/(10**value_exponent), error/(10**value_exponent)
    if unit is None:
        return f"${m_value} \\pm {m_error} \\cdot 10^{value_exponent}$"
    else:
        return f"${m_value} \\pm {m_error} \\cdot 10^{value_exponent} {unit}$"
