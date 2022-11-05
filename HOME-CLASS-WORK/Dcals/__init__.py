import Dcalc
def create_list(*args, **kwargs):
    disc = []

    for idx, value in enumerate(args):
        disc.append(f"Point_{idx} = {Dcalc.deg_to_gms(value)}")

    for k, v in kwargs.items():
        disc.append(f"{k} = {Dcalc.deg_to_gms(v)}")

    return disc
print(
    create_list(
        172.23242341,
        321.345345123,
        12.23423425,
        pole=21.234856,
        put_1=140.823423440,
    )
)