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

# Attack Type "Boarding" -> "Boarded"
pirate_attacks['attack_type'] = pirate_attacks['attack_type'].apply(
    lambda at: 'Boarded' if at == 'Boarding' else str(at))

# Vessel Status "steaming" -> "Steaming"
pirate_attacks['vessel_status'] = pirate_attacks['vessel_status'].apply(
    lambda vs: 'Steaming' if vs == 'steaming' else str(vs))


def break_lines(s: str, max_len: int = 30) -> str:
    # Split the string into words.
    try:
        words = s.split()

    except Exception as e:
        print('Words are:', s, type(s))

    # Initialize the result string and the current line.
    result = ""
    line = ""

    # Loop over the words.
    for word in words:
        # If the current line plus the current word is longer than the maximum line length,
        # add the current line to the result and reset the current line.
        if len(line) + len(word) > max_len:
            result += line + "<br>"
            line = ""

        # Add the current word to the current line, followed by a space.
        line += word + " "

    # Add the remaining line to the result.
    result += line

    return result


def get_custom_data(data: pd.DataFrame):
    def remove_nans(col):
        return col.apply(lambda s: s if (s is not None and str(s) != 'nan') else 'N/A')

    vessel_names = remove_nans(data['vessel_name'])
    loc_desc = remove_nans(data['location_description'])
    loc_desc = loc_desc.apply(break_lines)

    attack_desc = remove_nans(data['attack_description'])
    attack_desc = attack_desc.apply(break_lines)

    custom_data = np.stack([vessel_names, loc_desc, attack_desc], axis=-1)
    return custom_data


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

    filtered_data = pirate_attacks[data_mask].copy()

    return filtered_data
