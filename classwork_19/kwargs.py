def inregistreaza_utilizator(email: str, password: str, **informatie_aditionala) -> bool:
    print(f'Am inregitstrat {email}')
    print(f'Pe langa asta am inregistrat {informatie_aditionala}')


inregistreaza_utilizator('mt@mt.com', 'ASD')

inregistreaza_utilizator(email='<EMAIL>', password='asd', varsta=25, rank='ADMIN', gen='MASCULIN')


def conecteazate_la_db(ip: str, port: int, db_name: str, password: str, **info) -> bool:
    print(f'Am conecteazat {ip}:{port}:{db_name}')
    print(f"Pentru conectare am folosit parametri {info}")


conecteazate_la_db('localhost', 5432, 'main', '1231', encryption='RSA', connection_timeout=10)

dictionar_conexiune = {
    'db_name': 'main2',
    'connection_timeout': 20,
    'encryption': 'RSA',
    'ip': 'remote',
    'port': 9877,
    'password': '<PASSWORD>',
}

conecteazate_la_db(**dictionar_conexiune)
