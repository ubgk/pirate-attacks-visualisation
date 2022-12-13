import string

import numpy as np
import pandas as pd
from global_land_mask import globe

from utils.colors import map_colors, COLOR_LIST

pirate_attacks = pd.read_csv("data/pirate_attacks.csv")

# Filter points on land
pirate_attacks["is_ocean"] = pirate_attacks.apply(lambda row: globe.is_ocean(row.latitude, row.longitude), axis=1)
pirate_attacks = pirate_attacks[pirate_attacks["is_ocean"]]

# Year
pirate_attacks['date_year'] = pirate_attacks.date.apply(lambda x: int(x.split('-')[0]))

# Map attack types to colors
c_map = map_colors(pirate_attacks.attack_type.unique(), COLOR_LIST)
pirate_attacks['color'] = pirate_attacks.attack_type.apply(str).map(c_map)

# Attack Type "Boarded" == "Boarding"
pirate_attacks['attack_type'] = pirate_attacks['attack_type'].apply(lambda at: 'Boarded' if at == 'Boarding' else str(at))


def format_colname(plot_type):
    plot_type = plot_type.replace("_", " ")
    plot_type = string.capwords(plot_type)
    return plot_type.replace('Eez', 'EEZ')


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
