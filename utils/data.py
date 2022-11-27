import numpy as np
import pandas as pd

pirate_attacks = pd.read_csv("data/pirate_attacks.csv")
pirate_attacks['date_year'] = pirate_attacks.date.apply(lambda x: int(x.split('-')[0]))


def filter_data(range: list = None,
                 attack_types: list = None,
                 df: pd.DataFrame = pirate_attacks):
    data_mask = np.ones(df.shape[0], dtype=bool)

    if range:
        data_mask = data_mask & (df.date_year >= range[0])
        data_mask = data_mask & (df.date_year <= range[1])

    if attack_types:
        data_mask = data_mask & (df.attack_type.apply(lambda at: at in attack_types))

    return pirate_attacks[data_mask].copy()
