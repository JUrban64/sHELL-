from pony import orm 

db = orm.Database()

db.bind(provider = "sqlite", filename= "/Users/jachymurban/Desktop/PONYORM/Features.db", create_db = True  )


class Izotops(db.Entity): 
    F = orm.Optional(str)
    A = orm.Required(str)
    M = orm.Optional(str)
    Z = orm.Required(str)
    elemnts = orm.Required(str)
    J = orm.Optional(str)
    decay = orm.Optional(str)
    branch  = orm.Optional(str)
    excitation_en= orm.Optional(str)
    Q = orm.Optional(str)
    T = orm.Optional(str)
    abduance = orm.Optional(str)
    atom_mass  = orm.Required(str)
    delta_mass  = orm.Required(str)
    S = orm.Optional(str)
    date = orm.Optional(str)
    half_time = orm.Required(str)

class ELements(db.Entity): 
    Atomic_num = orm.Required(str)
    symbol = orm.Required(str)
    name = orm.Required(str)
    origin_name= orm.Required(str)
    group = orm.Required(str)
    period  = orm.Required(str)
    block = orm.Required(str)
    ar= orm.Required(str)
    density = orm.Required(str)
    melting_p = orm.Required(str)
    boiling_p = orm.Required(str)
    Cp = orm.Required(str)
    X = orm.Required(str)
    abduance = orm.Required(str)
    origin  = orm.Required(str)
    phase  = orm.Required(str)


db.generate_mapping(create_tables=True)


with orm.db_session:
    with open("nuclear-wallet-cards_2011.csv", "tr", encoding="utf-8") as file2: 
        next(file2)
        for line in file2: 
            F,A, M, Z, elemnts, J, decay, branch , excitation_en, Q, T, abduance, atom_mass, delta_mass, S, date, half_time = line.strip().split(";")
            i = Izotops(F=F, A=A, M = M, Z = Z, elemnts = elemnts, J = J, decay = decay, branch = branch, excitation_en= excitation_en, Q = Q, T= T, abduance = abduance, atom_mass = atom_mass, delta_mass = delta_mass, S = S, date = date, half_time = half_time )



with orm.db_session: 
    with open("elements-from-wiki.csv", "tr", encoding="utf-8") as file1: 
        next(file1)
        for line in file1: 
            Atomic_num,symbol, name, origin_name,group, period, block, ar ,density, melting_p, boiling_p, Cp, X, abduance,origin, phase = line.strip().split("\t")
            e = ELements(Atomic_num = Atomic_num, symbol = symbol, name = name, origin_name = origin_name, group = group, period = period, block = block, ar = ar, density = density, melting_p = melting_p, boiling_p = boiling_p, Cp = Cp, X = X, abduance = abduance, origin= origin, phase = phase )