from flask import redirect, render_template, url_for

from cartolafcgw.api import CartolaFC
from cartolafcgw.models import RankingTurnoView, RankingLigaView, RankingMesView, RankingMitoView


def config(app):

    @app.route('/api.gw-cartola')
    def api():
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])

        rodadas = cfc.rodadas()
        mercado = cfc.mercado()
        time = cfc.time(25395518, mercado['rodada_atual'])
        atletas = cfc.atletas(mercado['rodada_atual'])
        liga = cfc.liga('gw-altino-fc')
        atleta = cfc.atleta(25395518)

        return {
            'Rodadas': rodadas,
            'Mercado': mercado,
            'Time': time,
            'Atletas': atletas,
            'Liga': liga,
            'Atleta': atleta
        }

    @app.route('/dashboard')
    def dashboard():
        context = {
            'title': 'Dashboard',
            'rankin_liga': [
                {
                    'total': usuario.total,
                    'posicao': f'{n}º',
                    'time_nome': usuario.time_nome,
                    'primeiro_nome': usuario.primeiro_nome,
                    'segundo_nome': usuario.segundo_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for n, usuario in enumerate(RankingLigaView.query.all(), 1)
            ]
        }
        return render_template('dashboard.html', **context)
