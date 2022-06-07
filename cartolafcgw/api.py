from requests.api import get


class CartolaFC:
    def __init__(self, x_glb_token=None):
        self.cartolafc_url = 'https://api.cartolafc.globo.com'
        self._x_glb_token = x_glb_token

    def rodadas(self):
        rodadas_json = get(f'{self.cartolafc_url}/rodadas')
        return rodadas_json.json()

    def mercado(self):
        mercado_json = get(f'{self.cartolafc_url}/mercado/status')
        return mercado_json.json()

    def time(self, time_id, rodada_id):
        time_json = get(f'{self.cartolafc_url}/time/id/{time_id}/{rodada_id}')
        return time_json.json()

    def liga(self, slug):
        liga_json = get(url=f'{self.cartolafc_url}/auth/liga/{slug}', headers={'x-glb-token': self._x_glb_token})
        return liga_json.json()

    def atleta(self, id):
        atleta_json = get(f'{self.cartolafc_url}/auth/mercado/atleta/{id}/pontuacao', headers={'x-glb-token': self._x_glb_token})
        return atleta_json.json()

    def atletas(self, rodada_id):
        atletas_json = get(f'{self.cartolafc_url}/atletas/pontuados/{rodada_id}')
        return atletas_json.json()
