def get_summ(one, two, delimeter='&'):
    return str.upper(one) + str.upper(delimeter) + str.upper(two)


one1 = 'Learn'
two1 = 'python'

print(get_summ(one1, two1))