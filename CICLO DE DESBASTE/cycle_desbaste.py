import textwrap

class CicloDesbaste:

    def __init__(self, diametro_inicial: float, diametro_final: float, espessura:float, passe: float):
        
        if not isinstance(diametro_inicial, (float, int)):
            raise ValueError ('O valor do diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if not isinstance(diametro_final, (float, int)):
            raise ValueError ('O valor do diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if not isinstance(espessura, (float, int)):
            raise ValueError ('O valor da espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')

        if not isinstance(passe, (float, int)):
            raise ValueError ('O valor do passe deve ser um número decimal (float). Por favor, insira um valor válido.')

        self._diametro_inicial = diametro_inicial
        self._diametro_final = diametro_final
        self._espessura = espessura
        self._passe = passe

    @property
    def diametro_inicial(self):
        return self._diametro_inicial

    @property
    def diametro_final(self):
        return self._diametro_final
    
    @property
    def espessura(self):
        return self._espessura

    @property
    def passe(self):
        return self._passe
    
    @diametro_inicial.setter
    def set_diametro_inicial(self, novo_diametro_inicial: float):

        if not isinstance(novo_diametro_inicial, (float, int)):
            raise ValueError ('O valor do novo diâmetro inicial deve ser informado como um número decimal (float). Por favor, insira um valor válido.')

        if novo_diametro_inicial < self._diametro_final:
            raise Exception ('O novo diâmetro não pode ser menor que o diâmetro final. Por favor, insira um valor válido.')
        
        self._diametro_inicial = novo_diametro_inicial
        return self._diametro_inicial
    
    @diametro_final.setter
    def set_diametro_final(self, novo_diametro_final: float):

        if not isinstance(novo_diametro_final, (float, int)):
            raise ValueError ('O valor do novo diâmetro final deve ser informado como um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_diametro_final > self._diametro_final:
            raise Exception ('O novo diâmetro final não pode ser maior que o diâmetro inicial. Por favor, insira um valor válido.')
        
        self._diametro_final = novo_diametro_final
        return self._diametro_final
    
    @espessura.setter
    def set_espessura(self, nova_espessura: float):

        if not isinstance(nova_espessura, (float, int)):
            raise ValueError ('O valor da nova espessura deve ser do tipo decimal (float). Por favor, insira um valor válido.')
        
        if nova_espessura < 0:
            raise Exception ('O valor da espessura deve ser maior que zero. Por favor, insira um valor válido.')

        self._espessura = nova_espessura
        return self._espessura 

    @passe.setter
    def set_passe(self, novo_passe: float):

        if not isinstance(novo_passe, (float, int)):
            raise ValueError ('O valor do passe deve ser um número decimal (float). Por favor, insira um valor válido.')
        
        if novo_passe < 1:
            raise Exception ('O valor do novo passe deve ser igual ou maior que 1. Por favor, insira um valor válido.')
        
        self._passe = novo_passe
        return self._passe
    
    def ferramenta(self, tool: str):
        
        if not isinstance(tool, str):
            raise Exception ('A ferramenta informada deve ser do tipo texto (string). Por favor, insira um valor válido.')
        
        else:
            self._ferramenta = tool
            return self._ferramenta 
        
    def avanco(self, advance: float):

        if not isinstance(advance, (float, int)):
            raise ValueError ('O valor do avanço deve ser um número decimal (float). Por favor, insira um valor válido.')

        if advance <= 0:
            raise Exception ('O valor deve ser maior que zero. Por favor, insira um valor válido.')

        self._avanco = advance
        return self._avanco
    
    def rotacao(self, rpm: float):

        if not isinstance(rpm, (float, int)):
            raise ValueError ('O valor do RPM deve ser um número decimal (float). Por favor, insira um valor válido.')

        if rpm <= 0:
            raise Exception ('O valor do RPM não pode ser menor ou igual a zero. Por favor, insira um valor válido.')

        self._rotacao = rpm
        return self._rotacao
    
    def referencia_trabalho(self, ref: list):

        lista_referencias = ['G54', 'G55', 'G56', 'G57', 'G58', 'G59']

        if ref not in lista_referencias:
            raise Exception ('O valor da referência de trabalho deve ser um dos valores disponíveis na lista de referências. Por favor, selecione uma opção válida.')

        else:
            self._referencia = ref
            return self._referencia
        
    def gcode(self, nome_arquivo='Ciclo de Desbaste'):

        gcode_text = textwrap.dedent(f'''
        DEF INT N_PASSES
        DEF INT C_PASSES

        N10 G290
        N20 G18 G40 G90 G95

        N30 G0 {self._referencia} X400 Z100

        N40 {self._ferramenta} M3
        N50 G97 S{self._rotacao}

        R1 = {self._diametro_inicial}
        R2 = {self._diametro_final}
        R3 = -{self._espessura}

        R4 = -{self._passe}
        R5 = 0.5
        R6 = (R1 - R2) / 1
        R7 = 0

        N_PASSES = R6
        C_PASSES = 1

        IF R7 == 0
            MSG("INICIAR CICLO DE DESBASTE? - CYCLE START")
            M0
            MSG("")
            GOTO N60
        ENDIF

        IF R7 == 1
            MSG("INICIAR CICLO DE ACABAMENTO? - CYCLE START")
            M0
            MSG("")
            GOTO N90
        ENDIF

        IF R7 == 0 OR 1
            MSG("")
        ELSE
            MSG("ESCOLHA O CICLO QUE DESEJA REALIZAR, ATRIBUINDO UM VALOR A VARIÁVEL DE CONTROLE.")
            M0
            M30    
        ENDIF
        
        N60 G0 X=(R1 + 10)
        N70 G0 Z2

        N80 G0 X=R1

        FOR R8 = 0 TO (R6 - 1)
            MSG("PASSE DE DESBASTE: "<<C_PASSES<<" DE "<<N_PASSES)
            G91
            G1 X=R4 F{self._avanco}
            Z=R3
            X=ABS(R4)
            G0 Z=ABS(R3)
            C_PASSES = C_PASSES + 1
            G1 X=R4 F{self._avanco}
        ENDFOR

        MSG("INICIAR CICLO DE ACABAMENTO? - CYCLE START")
        M0
        MSG("PASSE DE ACABAMENTO 1 DE 1")

        N90 G90
        N100 G0 X=R1

        N110 G0 X=R2
        N120 G1 Z=R3 F{self._avanco}
        N130 G0 X=R1

        MSG("")
        N140 G0 {self._referencia} X400 Z100 

        N150 M5
        N160 M30''')

        with open(f'{nome_arquivo}.txt', 'w') as file:
            file.write(gcode_text)