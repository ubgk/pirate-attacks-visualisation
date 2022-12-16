import plotly

COLOR_LIST = plotly.colors.qualitative.Light24

COLOR_LIST = ['#0062FF', '#F2FF00', '#FF00D4', '#22FF00', '#FF0051', '#9000FF', '#72E0FF'][::-1]


# COLOR_LIST = ['#7af8ff'] + [COLOR_LIST[i] for i in [1, 4, 5, 6, 11, 15, 17, 18]]
# COLOR_LIST = ["#4deeea", "#74ee15", "#ffe700", "#f000ff", "#001eff", "#ff005c", "#ffbf00", "#ffffff"]
# COLOR_LIST = ['#7AF8FF', '#D875FF', '#567CFF', '#CCFF00', '#1F51FF', '#7FFF00', '#07F985', '#ffffff']

def map_colors(seq, c_map, key_f=(lambda x: x)):
    seq = map(lambda s: str(s), seq)
    seq = list(sorted(seq, key=key_f))

    c_map_dict = dict()
    for i, s in enumerate(seq):
        c_map_dict[s] = c_map[i % len(c_map)]

    return c_map_dict
