## Cálculo de Número de Passes

O cálculo do número de passes é amplamente utilizado em ciclos de desbaste, furação e canais.

Esse cálculo pode ser aplicado de diversas maneiras, mas as formas mais comuns adotadas por operadores e programadores são as seguintes:

> **Primeira forma**: Ø diâmetro_inicial - Ø diâmetro_final

É recomendável usar a primeira forma quando o passe de profundidade for igual a **1mm**.

> **Segunda forma**: Ø diâmetro_inicial - Ø diâmetro_final / pf 

Essa forma é mais comum para os ciclos de desbaste, pois, com o PF (passe de profundidade), torna-se mais versátil e de fácil utilização.

**Exemplo:**

    Ø diâmetro_inicial = 100mm.
	Ø diâmetro_final = 80mm.
	pf = 2mm. 
    n° de passes = ?

	n° de passes = 100 - 80 / 2
	n° de passes = 20 / 2
	n° de passes = 10

	n° total de passes = 10 passes.

Como mencionado acima, existem outras formas de utilização, mas estas são as mais utilizadas.