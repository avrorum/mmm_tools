import numpy as np

# mape
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    non_zero_mask = y_true != 0
    y_true_filtered = y_true[non_zero_mask]
    y_pred_filtered = y_pred[non_zero_mask]
    if len(y_true_filtered) == 0:
        return np.nan
    return np.mean(np.abs((y_true_filtered - y_pred_filtered) / y_true_filtered)) * 100


# todo: 

# тест Рамсея
def ramsey():
    '''
    Оценка включения всех необходимых переменных в модель 
    Оценка правильности функциональной формы зависимости
    '''
    pass

# тест VIF
def vif():
    '''
    Проверка мультиколлинеарности (линейной зависимости между регрессорами)
    '''
    pass 


# тест JArque-Bera
def j_bera():
    '''
    Проверка нормальности распределения ошибок
    '''
    pass


# графический анализ остатков

# тест Голдфельда-Кванта
def gold_quant():
    '''
    Проверка гомоскедастичности ошибок 
    '''
    pass

# тест Уайта
def white():
    '''
    Проверка гомоскедастичности ошибок 
    '''
    pass

# тест BG Бройша-Годфри
def b_godfri():
    '''
    Анализ автокорреляции (нарушение предпосылки о некоррелированности ошибок)
    '''
    pass

# exo / endo genitiy check

# other quality metrics of model mse, mae etc