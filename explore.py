import pandas as pd

pirate_attacks = pd.read_csv('data/pirate_attacks.csv')
country_indicators = pd.read_csv('data/country_indicators.csv')
country_codes = pd.read_csv('data/country_codes.csv')

from collections import Counter
from pprint import pprint
c_vessel_types = Counter(pirate_attacks.vessel_type)
pprint(c_vessel_types)
pass

c_attack_types = Counter(pirate_attacks.vessel_status)
pprint(c_attack_types)