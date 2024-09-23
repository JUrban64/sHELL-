from pony import orm 

from Models import ELements, Izotops

db = orm.Database()
db.bind(provider = "sqlite", filename= "/Users/jachymurban/Desktop/PONYORM/Features.db")

db.generate_mapping()

orm.set_sql_debug(True)

with orm.db_session():
    
    #for record in orm.select(e for e in ELements): ## TODLE NEJĚKA NEFUNGJE 
        #print(record)
    #for reco in db.select(e for e in ELements): ## TODLE HÁZÍ EROR S GENERÁTOREM 
        #print(reco)
    #query = orm.select(e for e in ELements)  
    #query.show() # toto funguje 

    for record in orm.select(e for e in ELements): 
        print(record.symbol , record.Atomic_num)