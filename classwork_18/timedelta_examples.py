from datetime import datetime, timedelta

timpul_acum = datetime.now()
diferenta_de_o_zi = timedelta(1)

timpul_maine = timpul_acum + diferenta_de_o_zi
print(timpul_maine)