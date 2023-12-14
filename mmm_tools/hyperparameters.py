media_vars_internet = [
    'imprs_ths', 
]
media_vars_tv = [
    'tvr_25_54', 
]

decay_rates_daily = {
    'tvr_25_54': 0.25, 
    'imprs_ths': 0.25,
    'imprs_ths_multipl_tvr_25_54': 0.25,
    
}

# shifts_daiy = {
#     'tv': 3, 
#     'internet': 1,
#     'tvr_25_54': 0.25, 
#     'imprs_ths': 0.25,
#     'imprs_ths_multipl_tvr_25_54': 0.25,
# }

# hill_parameters_daily = {
#     'tv': {
#         'max': 160,
#         'slope': 0.95,
#         'inflection': 150 * 0.6,
#     },
#     'internet': {
#         'max': 3_000,
#         'slope': 1.05,
#         'inflection': 3_000 * 0.6,
#     }
# }

decay_rates_weekly = {
    'tvr_25_54': 0.6, 
    'imprs_ths': 0.4,
    'imprs_ths_multipl_tvr_25_54': 0.45,
    
}

# shifts_weekly = {
#     'tv': 0, 
#     'internet': 0
# }

# hill_parameters_weekly = {
#     'tv': {
#         'max': 650,
#         'slope': 0.95,
#         'inflection': 650 * 0.6,
#     },
#     'internet': {
#         'max': 27_000,
#         'slope': 1.05,
#         'inflection': 27_000 * 0.6,
#     }
# }

