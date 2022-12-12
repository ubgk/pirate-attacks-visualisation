def map_colors(seq, c_map, key_f=(lambda x: x)):
    seq = map(lambda s: str(s), seq)
    seq = list(sorted(seq, key=key_f))

    c_map_dict = dict()
    for i, s in enumerate(seq):
        c_map_dict[s] = c_map[i % len(c_map)]

    return c_map_dict
