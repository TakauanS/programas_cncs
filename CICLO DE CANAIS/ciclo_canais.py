import textwrap

class CicloCanal:
    
    def __init__(self, diametro_inicial: float, diametro_final: float, n_canais: int, pos_canais: list):

        if not isinstance(diametro_inicial, (int, float)):
            raise ValueError('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, (int, float)):
            raise ValueError('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(n_canais, int):
            raise ValueError('O valor do número de canais deve ser um número inteiro (int). Por favor, insira um valor válido.')
        
        if n_canais < 0:
            raise Exception('O valor do número de canais não pode ser negativo. Por favor, insira um valor válido.')

        self._diametro_inicial = diametro_inicial
        self._diametro_final = diametro_final
        self._n_canais = n_canais
        self._pos_canais = pos_canais

    @property
    def diametro_inicial(self):
        return self._diametro_inicial

    @property
    def diametro_final(self):
        return self._diametro_final

    @property
    def n_canais(self):
        return self._n_canais

    @property
    def pos_canais(self):
        return self._pos_canais

    @diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if novo_diametro_inicial < self._diametro_final:
            raise Exception('O diâmetro inicial não pode ser menor que o diâmetro final. Por favor, insira valores válidos.')
    
        else:
            self._diametro_inicial = novo_diametro_inicial

    @diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if novo_diametro_final > self._diametro_inicial:
            raise Exception('O diâmetro final não pode ser maior que o diâmetro inicial. Por favor, insira valores válidos.')
        
        else:
            self._diametro_final = novo_diametro_final

    @n_canais.setter
    def set_n_canais(self, novo_n_canais: int):

        if novo_n_canais < 0:
            raise Exception('O valor do número de canais não pode ser negativo. Por favor, insira um valor válido.')

        else:
            self._n_canais = novo_n_canais

    @pos_canais.setter
    def set_pos_canais(self, novo_pos_canais):
        self._pos_canais = novo_pos_canais

    def avanco(self, advance: float):

        if advance < 0:
            raise Exception('O valor do avanço de usinagem deve ser maior que zero. Por favor, insira um valor válido.')
        
        else:
            self._avanco = advance

    def referencia_trabalho(self, ref):
        list_referencia = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

        if ref not in list_referencia:
            raise Exception('O sistema de referência de trabalho informado é inválido. Por favor, verifique e insira um valor correto.')
        
        else:
            self._referencia = ref

    def ferramenta(self, tool: str):
        self._ferramenta = tool

    def rotacao(self, rpm: float):
        self._rotacao = rpm

    def gcode(self, nome_arquivo='Ciclo de Canais'):

        gcode_text = textwrap.dedent(f'''
        DEF INT CANAIS[{self._n_canais}] = SET ({self._pos_canais})
        
        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self._referencia} X400 Z100

        N40 {self._ferramenta} M3;
        N50 G97 S{self._rotacao} M8

        R1 = {self._diametro_inicial};
        R2 = {self._diametro_final};

        R3 = 0.5;
        R4 = -0.5;
        R5 = R1 - R2;

        R7 = {self._n_canais}

        N60 G0 X=(R1 + 1) Z0

        FOR R6 = 0 TO (R7 - 1)
            G1 Z=CANAIS[R6] F{self._avanco}
            FOR R9 = 0 TO R5
                G91
                G1 X=R4 F{self._avanco}
                X=R3
                X=R4
            ENDFOR
            G90
            G0 X=(R1 + 1)
        ENDFOR

        N70 G90
        N80 G0 X=(R1 + 1)
        N90 Z0

        N100 G0 {self._referencia} X400 Z100

        N110 M9
        N120 M5
        N130 M30''')

        with open(f'{nome_arquivo}.txt', "w") as arquivo:
            arquivo.write(gcode_text)