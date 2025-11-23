# Flood Fill - Preenchimento de Regiões Conectadas

## Descrição

Este projeto implementa o algoritmo **Flood Fill** (Preenchimento por Inundação) usando **BFS** (Busca em Largura) para preencher todas as regiões conectadas de um grid.

**Problema:**
- Dado um grid 2D com células vazias (valor `0`) e obstáculos (valor `> 0`),
- Preencher cada região conectada de células vazias com uma cor única.
- Regiões conectadas são células adjacentes horizontalmente ou verticalmente (4-conectado).

**Solução:**
- O algoritmo itera pelo grid procurando por células vazias.
- Para cada célula vazia encontrada, executa Flood Fill (BFS) para colorir toda a região com uma cor única.
- Cores começam em `2` e incrementam a cada nova região descoberta.

---

## Estrutura do Projeto

```
floodfill-projeto/
├── floodfill.py       # Código principal com implementação completa
├── README.md          # Este arquivo
├── input.txt          # Exemplo de entrada simples
└── input_complex.txt  # Exemplo de entrada complexa
```

---

## Como Usar

### 1. Instalação (Ponto Extra - Opcional)

Para usar a visualização colorida, instale a dependência:

```powershell
pip install colorama
```

Sem `colorama`, o programa funciona normalmente em modo texto plano.

---

### 2. Entrada Interativa (stdin)

Execute o programa sem argumentos para entrar no modo interativo:

```powershell
python floodfill.py
```

O programa solicitará:
- **Número de linhas**: inteiro `n > 0`
- **Número de colunas**: inteiro `m > 0`
- **Grid**: `n` linhas, cada uma com `m` inteiros separados por espaço

**Exemplo de entrada interativa:**
```
Digite o número de linhas: 3
Digite o número de colunas: 3
Digite o grid (cada linha separada por Enter, valores separados por espaço):
1 0 1
0 0 0
1 0 1
```

### 3. Entrada por Arquivo

Crie um arquivo (ex.: `input.txt`) com o seguinte formato:

```
3 3
1 0 1
0 0 0
1 0 1
```

Execute passando o nome do arquivo:

```powershell
python floodfill.py input.txt
```

**Com visualização colorida (Ponto Extra):**

```powershell
python floodfill.py input.txt -c
```

ou

```powershell
python floodfill.py input.txt --color
```

### 4. Entrada por Stdin Redirecionado

```powershell
python floodfill.py < input.txt
```

---

## Formato de Entrada

**Primeira linha:** `n m` (número de linhas e colunas)  
**Próximas n linhas:** `m` inteiros separados por espaço

Onde:
- `0` = célula vazia (será preenchida)
- `>0` = obstáculo (será mantido)

---

## Exemplos

### Exemplo 1: Execução Básica

```powershell
python floodfill.py input.txt
```

**Input:**
```
3 3
1 0 1
0 0 0
1 0 1
```

**Output:**
```
========================================
Grid ANTES do preenchimento:
========================================
1 0 1
0 0 0
1 0 1

========================================
Grid DEPOIS do preenchimento:
========================================
1 2 1
2 2 2
1 2 1

Regiões preenchidas: 1
```

### Exemplo 2: Com Visualização Colorida (Ponto Extra)

```powershell
python floodfill.py input_complex.txt -c
```

**Input:**
```
4 4
1 0 0 1
0 1 0 0
0 0 1 0
1 0 0 1
```

**Output (com cores no terminal):**
```
========================================
Grid ANTES do preenchimento:
========================================
1 0 0 1
0 1 0 0
0 0 1 0
1 0 0 1

========================================
Grid DEPOIS do preenchimento:
========================================
(Visualização Colorida - Ponto Extra)
1 2 2 1
3 1 2 2
3 3 1 2
1 3 3 1

Regiões preenchidas: 2
```

**Legenda de Cores:**
- 🟥 Vermelho: Obstáculos (valor 1)
- 🟦 Azul: Região 1 (valor 2)
- 🟩 Verde: Região 2 (valor 3)
- 🟨 Amarelo: Região 3 (valor 4)
- 🟪 Magenta: Região 4 (valor 5)
- (e assim por diante, ciclando cores)

---

## Ponto Extra - Visualização Colorida

A versão colorida é **opcional** e oferece uma visualização melhorada:

- **Requisitos:** Biblioteca `colorama` (instale com `pip install colorama`)
- **Uso:** Adicione `-c` ou `--color` ao comando
- **Compatibilidade:** Funciona em Windows, macOS e Linux
- **Fallback:** Se `colorama` não estiver instalado, o programa funciona em modo texto normal

**Benefícios:**
- ✅ Melhor visualização de regiões distintas
- ✅ Cores ajudam a identificar padrões
- ✅ Apresentação profissional

---

## Complexidade Algorítmica

- **Tempo:** $O(n \times m)$ - cada célula é visitada no máximo uma vez
- **Espaço:** $O(n \times m)$ - fila BFS pode conter até todas as células

---

## Funções Principais

### `flood_fill(grid, x, y, color)`
Preenche uma região conectada de células vazias usando BFS.

### `find_next_free_cell(grid)`
Encontra a próxima célula vazia não explorada.

### `fill_all_regions(grid)`
Preenche todas as regiões vazias do grid.

### `print_grid(grid, colored=False)`
Exibe o grid em modo texto normal.

### `print_grid_colored(grid)`
Exibe o grid com cores (requer colorama).

### `read_grid_from_file(filename)`
Lê grid de um arquivo de texto.

### `read_grid_from_stdin()`
Lê grid interativamente do terminal.

---

## Tratamento de Erros

O programa valida:
- ✓ Arquivo existe e é legível
- ✓ Dimensões `n, m > 0`
- ✓ Número de colunas consistente em todas as linhas
- ✓ Valores são inteiros válidos
- ✓ Coordenadas dentro dos limites do grid

---

## Requisitos

- Python 3.6+
- `colorama` (opcional, para visualização colorida)

---

## Exemplos de Teste

### Exemplo 1: Grid com uma região

```
2 2
0 0
0 0
```

**Resultado:** Todas as células preenchidas com `2` (uma região)

### Exemplo 2: Grid cheio de obstáculos

```
2 2
1 1
1 1
```

**Resultado:** Nenhuma célula preenchida (0 regiões)

### Exemplo 3: Grid com múltiplas regiões isoladas

```
3 5
0 1 0 1 0
1 1 1 1 1
0 1 0 1 0
```

**Resultado:** 4 regiões isoladas preenchidas com cores 2, 3, 4, 5

---

## Autor

Guilherme da Silveira Cantoni

---

## Licença

Este projeto é fornecido como está para fins educacionais.
