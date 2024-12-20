## Ciclo de Desbaste - Padrão

O ciclo de desbaste padrão é o mais utilizado, pois o tipo de ferramenta empregada permite realizar a usinagem apenas em um sentido.

Exemplo de insertos que podem ser utilizado o estilo de ciclo de desbaste padrão:

![TNMG](../imgs/tnmg.png)ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ![VNMG](../imgs/vnmg.png)

> A outros diversos tipos de insertos que podem ser utilizados para esse estilo de usinagem.

O programa **.nc** só pode ser executado em controladores **Siemens**, pois o programa contém **parâmetros R**.

O programa que será disponibilizado abaixo contém campos com "{ }" e os parâmetros R que também dentro das chaves é o nome que deve ser passado o valor do parâmetro.

**Confira o programa:**

    N10 G290
    N20 G18 G54 G95 G90

    N30 G0 G54 X{POSICIONAMENTO EM X} Z{POSICIONAMENTO EM Z}

    N40 {FERRAMENTA}
    N50 G97 {ROTAÇÃO} M3;

    N60 R1 = Ø DIÂMETRO INICIAL
    N70 R2 = Ø DIÂMETRO FINAL
    N80 R3 = ESPESSURA

    N90  R4 = PASSE
    N100 R5 = RETORNO (RECUO)  

    N110 G0 X=R1 Z0 M8

    FOR R6 = 1 TO {NÚMERO DE PASSES}
        G91
        G1 X=R4 F{AVANÇO}
        Z=R3
        X=R5
        Z=ABS(R3)
        X=R4
    ENDFOR

    N120 G90

    N130 G0 Z2
    N140 G0 X=R2

    N150 G1 Z=R3 F{AVANÇO}

    N160 G0 G54 X{POSICIONAMENTO EM X} Z{POSICIONAMENTO EM Z}

    N170 M5
    N180 M30

Para encontrar o número de passes use o cálculo de [número de passes](https://github.com/TakauanS/programas_cncs/blob/staging/CICLO%20DE%20DESBASTE/calculo_passes.md) que se encontra no repositório.

Faça um bom proveito do programa, lembrando que o código pode passar por algumas atualizações.  