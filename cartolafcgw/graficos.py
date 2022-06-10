from json import dumps

from pandas import DataFrame
from plotly.express import bar, line
from plotly.utils import PlotlyJSONEncoder

from cartolafcgw.database import db
from cartolafcgw.models import Usuario, Ponto, GraficoLigaView


class LigaGrafico:

    def __init__(self):
        self.times = [
            (usuario.rodada_id, usuario.posicao, usuario.time_nome)
            for usuario in GraficoLigaView.query.all()
        ]

    def __criar_data_frame(self):
        return DataFrame(self.times, columns=['Rodada', 'Posição', 'Cartoleiro'])

    def criar_figura(self):
        figura = line(
            data_frame=self.__criar_data_frame(),
            x='Rodada',
            y='Posição',
            text='Posição',
            color='Cartoleiro'
        )

        figura.update_layout(
            # title_text='Posição por Rodada - Liga GW Altino FC - Cartola 2022',
            title_x=0.5,
            title_font_size=20,
            width=600,
            height=500
        )

        figura.update_traces(textposition='top center')

        figura.update_yaxes(
            title='Posição',
            title_font_color='green',
            title_font_size=18,
            # visible=False,
            showticklabels=False,
            autorange="reversed"
        )

        figura.update_xaxes(
            title='Rodada',
            title_font_color='green',
            title_font_size=18
        )

        # figura.show()
        return dumps(figura, cls=PlotlyJSONEncoder)


# class DueloGrafico:

#     def __init__(self, jogador, adversario, rodada, times):
#         self.jogador = jogador
#         self.adversario = adversario
#         self.rodada = int(rodada)
#         self.times = times

#     def criar_data_frame(self):
#         """
#         SELECT r.id, pontos,
#                ROUND(pontos / s.total * 100, 2)
#         FROM rodadas AS "r"
#             INNER JOIN cartoleiros AS "c"
#             ON r.time_id = c.id

#             INNER JOIN (SELECT r.id, SUM(pontos) AS "total"
#                             FROM rodadas AS "r"
#                                 INNER JOIN cartoleiros AS "c"
#                                 ON r.time_id = c.id
#                             WHERE c.primeiro_nome in('Weverton', 'Raphael')
#                             GROUP BY r.id) AS "s"
#             ON r.id = s.id
#         WHERE c.primeiro_nome in('Weverton', 'Raphael');
#         """

#         subq = db.session.query(
#             Rodada.id, db.func.sum(Rodada.pontos).label('total')
#         ).join(
#             Cartoleiro, Rodada.time_id == Cartoleiro.id
#         ).filter(
#             Cartoleiro.primeiro_nome.in_([self.jogador, self.adversario])
#         ).group_by(
#             Rodada.id
#         ).subquery()

#         duelos = db.session.query(
#             Rodada.id, Rodada.pontos, Rodada.time_id,
#             db.func.round(Rodada.pontos / subq.c.total * 100, 2)
#         ).join(
#             Cartoleiro, Rodada.time_id == Cartoleiro.id
#         ).join(
#             subq, subq.c.id == Rodada.id
#         ).filter(
#             Cartoleiro.primeiro_nome.in_([self.jogador, self.adversario])
#         ).all()

#         dic = {'Rodada': [], 'Pontos': [], 'Time': [], 'Porcentagem': []}
#         for duelo in duelos:
#             dic['Rodada'].append(duelo[0] + 'ª')
#             dic['Pontos'].append(float(duelo[1]))
#             dic['Time'].append(self.times[duelo[2]])
#             dic['Porcentagem'].append(duelo[3])

#         return DataFrame(dic)

#     def criar_figura(self):
#         figura = bar(
#             data_frame=self.criar_data_frame(),
#             x='Rodada',
#             y='Porcentagem',
#             text='Pontos',
#             color='Time'
#         )
        
#         figura.update_layout(
#             title_text='Pontos por Rodada - Liga GW Altino FC - Cartola 2022',
#             title_x=0.5,
#             title_font_size=20
#         )

#         figura.update_traces(textposition='inside')

#         figura.update_yaxes(
#             title='Pontuação',
#             title_font_color='blue',
#             title_font_size=18,
#             # visible=False,
#             showticklabels=False
#         )

#         figura.update_xaxes(
#             title='Rodada',
#             title_font_color='blue',
#             title_font_size=18
#         )

#         figura.show()
