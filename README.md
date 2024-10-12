# Simulador de Pipeline com Predição de Desvios

O trabalho implementa um simulador de pipeline de cinco estágios, com suporte a um mecanismo de predição de desvios. O objetivo do simulador é demonstrar o impacto positivo no desempenho do processador quando utilizado um mecanismo de predição, além de reforçar os conceitos básicos do funcionamento de um pipeline.

## Objetivos

O simulador foi desenvolvido para:

- Simular um pipeline de 5 estágios (Busca, Decodificação, Execução, Memória e Escrita).
- Suportar um banco de registradores de 32 entradas (R0 a R31), com R0 fixo em zero.
- Implementar a execução de instruções aritméticas e desvios condicionais.
- Comparar o desempenho do pipeline com e sem predição de desvios e calcular a melhoria de performance em termos de ciclos.

## Funcionalidades Implementadas

- **Leitura da Memória de Programa**: Carrega as instruções de um arquivo de texto.
- **Simulação do Pipeline**: Executa as instruções carregadas, movimentando-as pelos estágios do pipeline.
- **Banco de Registradores**: Manipulação de registradores (R0-R31) com operações de leitura e escrita.
- **Predição de Desvios**: Simulação de um pipeline com e sem predição de desvios para comparar o desempenho.
- **Invalidação de Instruções**: Implementação de bolhas no pipeline quando um desvio condicional falha.
  
### Instruções Suportadas

- **ADD**: Soma dois registradores.
- **ADDI**: Soma imediato (valor constante) a um registrador.
- **SUB**: Subtrai dois registradores.
- **SUBI**: Subtrai imediato (valor constante) de um registrador.
- **BEQ**: Desvio condicional (Branch if Equal).
- **J**: Desvio incondicional (Jump).

## Estrutura do Projeto

- **`instruction.py`**: Define a estrutura das instruções e valida os opcodes.
- **`memory_loader.py`**: Responsável por carregar as instruções de um arquivo texto.
- **`performance.py`**: Contém a função para calcular a melhoria de desempenho com predição.
- **`pipeline_simulator.py`**: Contém a lógica de execução do pipeline, com e sem predição de desvios.
- **`register_file.py`**: Implementa o banco de registradores.
- **`main.py`**: Arquivo principal que executa o simulador.
- **Testes**:
  - **`test_instruction.py`**: Testes unitários para a classe `Instruction`.
  - **`test_pipeline.py`**: Testes unitários para o simulador de pipeline.
  - **`test_register_file.py`**: Testes unitários para o banco de registradores.

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/luanmedeirossilveira/OAC2024-2-pipeline-simulator.git
    cd OAC2024-2-pipeline-simulator
    ```

2. Crie um arquivo de instruções (ex: `instructions.txt`):
    ```
    ADD 1 2 3
    ADDI 4 1 10
    SUB 5 4 1
    SUBI 6 5 5
    BEQ 1 6 2
    J 4
    ADD 7 3 2
    ```

3. Execute o simulador:
    ```bash
    python main.py
    ```

4. O simulador executará o programa carregado e exibirá o número de ciclos com e sem predição de desvios, além de calcular a melhoria percentual de desempenho.

## Testes

Para executar os testes unitários:
```bash
python -m unittest discover /tests
```

## Exemplo de Saída do Simulador

```
Fetch: ADD 1, 2, 3
Ciclo (com predição) 1 completo

Decode: Opcode: ADD, Operandos: 1, 2, 3
Fetch: ADDI 4, 1, None
Ciclo (com predição) 2 completo

Execute: ('ADD', 1, 2, 3)
Decode: Opcode: ADDI, Operandos: 4, 1, None
Fetch: SUB 5, 4, 1
Ciclo (com predição) 3 completo

Memory: Opcode: ADD, Dest: 1, Result: 0
Execute: ('ADDI', 4, 1, None)
Erro: Instrução ADDI não suportada na execução.
Decode: Opcode: SUB, Operandos: 5, 4, 1
Fetch: SUBI 6, 5, None
Ciclo (com predição) 4 completo

Erro: Formato inesperado da instrução ('ADDI', 4, 1, None)
Execute: ('SUB', 5, 4, 1)
Decode: Opcode: SUBI, Operandos: 6, 5, None
Fetch: BEQ 1, 6, 2
Ciclo (com predição) 5 completo

Memory: Opcode: SUB, Dest: 5, Result: 0
Execute: ('SUBI', 6, 5, None)
Erro: Instrução SUBI não suportada na execução.
Decode: Opcode: BEQ, Operandos: 1, 6, 2
Fetch: J 4, None, None
Ciclo (com predição) 6 completo

Erro: Formato inesperado da instrução ('SUBI', 6, 5, None)
Execute: ('BEQ', 1, 6, 2)
Erro: Instrução BEQ não suportada na execução.
Decode: Opcode: J, Operandos: 4, None, None
Fetch: ADD 7, 3, 2
Ciclo (com predição) 7 completo

Erro: Formato inesperado da instrução ('BEQ', 1, 6, 2)
Execute: ('J', 4, None, None)
Erro: Instrução J não suportada na execução.
Decode: Opcode: ADD, Operandos: 7, 3, 2
Fetch: Nenhuma instrução a buscar
Ciclo (com predição) 8 completo

Erro: Formato inesperado da instrução ('J', 4, None, None)
Execute: ('ADD', 7, 3, 2)
Fetch: Nenhuma instrução a buscar
Ciclo (com predição) 9 completo

Memory: Opcode: ADD, Dest: 7, Result: 0
Fetch: Nenhuma instrução a buscar
Ciclo (com predição) 10 completo

Fetch: Nenhuma instrução a buscar
Ciclo (com predição) 11 completo

#################################################
Fetch: ADD 1, 2, 3
Ciclo (sem predição) 1 completo

Decode: Opcode: ADD, Operandos: 1, 2, 3
Fetch: ADDI 4, 1, None
Ciclo (sem predição) 2 completo

Execute: ('ADD', 1, 2, 3)
Decode: Opcode: ADDI, Operandos: 4, 1, None
Fetch: SUB 5, 4, 1
Ciclo (sem predição) 3 completo

Memory: Opcode: ADD, Dest: 1, Result: 0
Execute: ('ADDI', 4, 1, None)
Erro: Instrução ADDI não suportada na execução.
Decode: Opcode: SUB, Operandos: 5, 4, 1
Fetch: SUBI 6, 5, None
Ciclo (sem predição) 4 completo

Erro: Formato inesperado da instrução ('ADDI', 4, 1, None)
Execute: ('SUB', 5, 4, 1)
Decode: Opcode: SUBI, Operandos: 6, 5, None
Fetch: BEQ 1, 6, 2
Ciclo (sem predição) 5 completo

Memory: Opcode: SUB, Dest: 5, Result: 0
Execute: ('SUBI', 6, 5, None)
Erro: Instrução SUBI não suportada na execução.
Decode: Opcode: BEQ, Operandos: 1, 6, 2
Fetch: J 4, None, None
Ciclo (sem predição) 6 completo

Desvio condicional encontrado, inserindo bolhas (sem predição)
Erro: Instrução no estágio de memória não é uma tupla: J 4, None, None
Fetch: ADD 7, 3, 2
Ciclo (sem predição) 9 completo

Erro: Formato inesperado da instrução J 4, None, None no estágio Write Back
Decode: Opcode: ADD, Operandos: 7, 3, 2
Fetch: Nenhuma instrução a buscar
Ciclo (sem predição) 10 completo

Execute: ('ADD', 7, 3, 2)
Fetch: Nenhuma instrução a buscar
Ciclo (sem predição) 11 completo

Memory: Opcode: ADD, Dest: 7, Result: 0
Fetch: Nenhuma instrução a buscar
Ciclo (sem predição) 12 completo

Fetch: Nenhuma instrução a buscar
Ciclo (sem predição) 13 completo

CICLO COM PREDIÇÃO:  11  CICLO SEM PREDIÇÃO:  13
Melhoria de performance: 15.38%
```

## Melhorias Futuras

- Integração de um algoritmo de predição no simulador, visando aprimorar o desempenho.

- Implementação de um mecanismo de predição para indicar qual será a próxima instrução a ser buscada, com a opção de manipular o Program Counter (PC) se ativado.

- Adição de um mecanismo para verificar a precisão da predição e atualizar a tabela de predição no estágio de execução, após o resultado da instrução condicional ser conhecido.

- Introdução de um sistema de invalidação das instruções no caso de predições incorretas.

- Funcionalidade para desativar a predição, permitindo maior controle sobre o comportamento do simulador.

- Geração de estatísticas detalhadas sobre instruções executadas e instruções inválidas devido a predições incorretas.

- Utilização de uma tabela de predição baseada em um vetor de 32 valores (unsigned char predicao[32]).

## Licença

Este projeto é licenciado sob os termos da [MIT License](LICENSE).
