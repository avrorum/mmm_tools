import numpy as np


def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    non_zero_mask = y_true != 0
    y_true_filtered = y_true[non_zero_mask]
    y_pred_filtered = y_pred[non_zero_mask]
    if len(y_true_filtered) == 0:
        return np.nan
    return np.mean(np.abs((y_true_filtered - y_pred_filtered) / y_true_filtered)) * 100




# тест Рамсея

# тест VIF

# тест JArque-Bera

# графический анализ остатков

# тест Голдфельда-Кванта

# тест Уайта

# тест BG Бройша-Годфри

# exo / endo genitiy check

