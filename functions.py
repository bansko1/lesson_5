def hello_who(name):
    """
    :param name: кого приветствовать
    :return: приветствие
    """
    return f'Hello, {name}!'


def sallary(hours, salary_by_hours):
    '''
    :param hours: отработано часов
    :param salary_by_hours: ставка за час
    :return: зарплата
    '''
    k = 2
    return hours * salary_by_hours * k
