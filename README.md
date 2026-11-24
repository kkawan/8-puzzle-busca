# 8-Puzzle — Busca em Espaço de Estados

## Como executar

Com Python 3.10 ou mais recente, rode na raiz do projeto:

```bash
python main.py
```

O programa resolve o mesmo tabuleiro com os três algoritmos e mostra os movimentos, o custo e as métricas da busca. Os movimentos indicam a direção do espaço vazio: `UP`, `DOWN`, `LEFT` e `RIGHT`.

- **BFS:** usa uma fila para explorar os estados por camada e encontra um caminho de custo mínimo.
- **DFS:** usa uma pilha e explora até um limite de profundidade (50 por padrão). A primeira solução pode não ser a mais curta.
- **A\*:** prioriza a soma entre o custo já percorrido e a distância Manhattan das peças até suas posições finais, sem contar o espaço vazio.

## Estrutura

```
├── puzzle/
│   ├── state.py        # movimentos e reconstrução do caminho
│   ├── result.py       # resultado da busca
│   └── base_search.py  # interface dos algoritmos
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   └── a_star.py
└── main.py
```

