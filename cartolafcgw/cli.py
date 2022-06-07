from cartolafcgw.database import db
from cartolafcgw.models import Ponto, Rodada, Usuario
from cartolafcgw.api import CartolaFC


def config(app):

    def create_db():
        """Creates database"""
        db.create_all()

    def drop_db():
        """Cleans database"""
        db.drop_all()

    def insert_values_in_usuarios():
        """Insere 48 registros na tabela usuários"""
        usuarios = [
            Usuario(14836153, 'Juninhofera09', 'Alberto', 'Júnior', None),
            Usuario(527126, 'Alexandre SNTS', 'Alexandre', 'Dias', 'de Lima'),
            Usuario(846171, 'Bahia em Foco FC', 'Antônio', 'de Andrade', 'Costa'),
            Usuario(3459625, 'BW.Barber FC', 'Brendon Willian', 'Cruz', None),
            Usuario(149839, 'Cassiano S.C.C.P', 'Cassiano', 'de Sales', 'Terzi'),
            Usuario(25505954, 'CAÇUAR FC', 'Claudivan', 'Santos', 'de Jesus'),
            Usuario(13991216, 'Cristiano Lima F.C', 'Cristiano', 'Pereira', 'de Lima'),
            Usuario(448887, 'Pode Piorar FC', 'Daniel', 'Gomes', 'da Silva'),
            Usuario(7955099, 'Pântano do Além SNTS', 'Diego', 'da Silva', 'Maciel'),
            Usuario(3428463, 'Cartolytics', 'Diego', 'Pupato', 'Meireles'),
            Usuario(3088830, 'realmadrinha', 'Elias', 'Martins', 'de Souza'),
            Usuario(11419966, 'Autocar Multimarcas', 'Fabiano', 'Siqueira', None),
            Usuario(13934493, 'Fäbynhö F7', 'Fabio', 'Mota', 'Paixão'),
            Usuario(3873535, 'Soccer City E.C.', 'Fagner', 'Santos', 'Borges'),
            Usuario(7781830, 'É o trikas não tem jeito', 'Felipe', 'Morgado', 'Piovan'),
            Usuario(255523, 'Iludidos FGS', 'Fábio', 'Gomes', 'da Silva'),
            Usuario(14748896, 'Viottense United F.C', 'Gustavo', 'Viotto', None),
            Usuario(856073, 'MáKinaFC', 'Gustavo Henrique', 'Tavares', 'de Souza'),
            Usuario(14124471, 'K_tado Fut club', 'Helton', 'Gael', None),
            Usuario(13979324, 'Trikolino', 'Henrique', 'Mota', None),
            Usuario(1036408, 'Facção19 FC SNTS', 'Higor', 'Teles', None),
            Usuario(1000836, 'Silver Hawk\'s FC', 'Hudson', 'Bachesque', None),
            Usuario(3699002, 'SPJUNIORS FC', 'Hélio', 'Barros', 'de Lima Júnior'),
            Usuario(1004239, 'Sport C. R', 'José Geraldo', 'Cândido', 'do Nascimento'),
            Usuario(168447, 'sportclube bamor', 'João Pedro', 'Santana', 'Curcino'),
            Usuario(1172500, 'RANGEL_ANDRADAS', 'Leonardo', 'Rangel', None),
            Usuario(8358587, 'Real Maru SNTS', 'Lucas', 'Rodrigues', None),
            Usuario(23799206, 'porphirio 28', 'Lucas', 'Alves', 'Porphirio'),
            Usuario(15793, 'O TEU PADRASTO FC', 'Luís Alberto', 'Santos', 'da Silva'),
            Usuario(15067048, 'X Vídeos F.C.P.', 'Luís Fernando', 'Cordeiro', 'Santos'),
            Usuario(3043804, 'Pirâmide-futebol-clube', 'Marcos', 'Dias', 'Lima'),
            Usuario(1031180, 'NADA MAL F.C', 'Matheus', 'Oliveira', 'de Souza'),
            Usuario(8243052, 'MiB Football Club', 'Micael', 'Bastos', 'do Nascimento'),
            Usuario(771302, 'TEAM CLEMENTE\'S', 'Nonato', 'Clementino', 'Santos'),
            Usuario(13939246, 'RLC Resenha', 'Rafael', 'Silveira', 'de Oliveira'),
            Usuario(3489970, 'BENIC Football Club', 'Rafael', 'Costa', None),
            Usuario(65495, 'Batutinhas F.C', 'Ramon', 'Santos', 'Fabiano Carvalho'),
            Usuario(211214, 'RPONCE F.C', 'Raphael', 'Ponce', 'de Leon Peres'),
            Usuario(136012, 'LIFE STYLE F.C', 'Renato', 'Pereira', 'Perissatto'),
            Usuario(4531940, 'RNTricolor', 'Renato', 'Silveira', 'de Oliveira'),
            Usuario(26075555, 'Dino 2021 SC', 'Rodrigo', 'da Silva', 'Gomes'),
            Usuario(28863195, 'XIPALOBEDA FC', 'Rubens', 'Conegero', 'Neto'),
            Usuario(13989240, 'Sessé The Avenger F.C', 'Sérgio', 'dos Santos', 'Cruz'),
            Usuario(357697, 'Craques do Morumba', 'Tarcizius', 'Michels', 'Júnior'),
            Usuario(576186, 'Porphirio FC', 'Thiago', 'Alves', 'Porphirio'),
            Usuario(9208855, 'WLTSC.FC', 'Wellington', 'Souza', 'Cavalcante'),
            Usuario(44510761, 'brian29wel', 'Wellington', 'Farias', 'da Silva'),
            Usuario(25395518, 'Weverton Teixeira FC', 'Weverton', 'Teixeira', 'de Sousa')
        ]
        db.session.add_all(usuarios)
        db.session.commit()

    def insert_values_in_rodadas():
        """Insere os rodadas da api da Globo na tabela rodadas"""
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])
        for rodada in cfc.rodadas():
            if rodada['rodada_id'] == 16:
                break
            rodada = Rodada(rodada['rodada_id'], rodada['inicio'], rodada['fim'])
            db.session.add(rodada)
        db.session.commit()


    def insert_values_in_pontos():
        """Insere os pontos da api da Globo na tabela pontos"""
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])
        times = Usuario.query.all()
        for rodada in range(9, 10):
            for time in times:
                try:
                    pontos = sum([
                        atleta['pontos_num']
                        for atleta in cfc.time(time.id, rodada)['atletas']
                    ])
                except KeyError:
                    pontos = 0.0

                try:
                    db.session.add(Ponto(time.id, rodada, pontos))
                    db.session.commit()
                except Exception as e:
                    print(e)

    for command in [
        create_db,
        drop_db,
        insert_values_in_usuarios,
        insert_values_in_rodadas,
        insert_values_in_pontos
    ]:
        app.cli.add_command(app.cli.command()(command))
