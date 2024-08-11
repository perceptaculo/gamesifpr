# Simulações de Movimento Retilíneo Uniforme (MRU) em Python

Este repositório contém três simulações básicas de Movimento Retilíneo Uniforme (MRU) em Python, utilizando as bibliotecas `matplotlib` e `pygame`. As simulações foram desenvolvidas para ilustrar conceitos de MRU, sendo elas:

1. **Gráfico de MRU**: Uma representação gráfica do movimento.
2. **Simulação MRU**: Uma bola que se move automaticamente em uma direção fixa.
3. **Simulação MRU com Controle**: Uma bola controlável com o teclado, incluindo aceleração ao pressionar a tecla Shift.

## Requisitos

Para rodar os códigos, é necessário ter o Python instalado na sua máquina. Além disso, as seguintes bibliotecas são necessárias:

- `matplotlib`
- `numpy`
- `pygame`

Você pode instalar as dependências executando:

```bash
pip install matplotlib numpy pygame
```

## 1. Gráfico de MRU

### Descrição

Esta simulação desenha um gráfico de posição em função do tempo, representando um Movimento Retilíneo Uniforme (MRU). 

### Código

O código está localizado em `mru_grafico.py`.

### Execução

Para rodar a simulação, execute:

```bash
python mru_grafico.py
```

Um gráfico será gerado mostrando a posição do objeto ao longo do tempo.

### Exemplo de Saída

![Gráfico de MRU](https://via.placeholder.com/800x600)

## 2. Simulação MRU (Movimento Automático)

### Descrição

Este programa abre uma janela onde uma bola se move automaticamente em linha reta com velocidade constante. O movimento é reiniciado quando a bola atinge a borda da janela.

### Código

O código está localizado em `mru_simulacao.py`.

### Execução

Para rodar a simulação, execute:

```bash
python mru_simulacao.py
```

### Controles

- A bola se move automaticamente da esquerda para a direita.
- Quando atinge a borda direita da janela, reaparece na borda esquerda.

### Exemplo de Saída

![Simulação MRU Automática](https://via.placeholder.com/800x600)

## 3. Simulação MRU com Controle e Aceleração

### Descrição

Esta simulação abre uma janela onde uma bola pode ser movida pelo usuário usando as setas do teclado. Quando a tecla Shift é pressionada, a bola acelera em ambas as direções (X e Y).

### Código

O código está localizado em `mru_simulacao_controle.py`.

### Execução

Para rodar a simulação, execute:

```bash
python mru_simulacao_controle.py
```

### Controles

- Setas do teclado: Movimentam a bola nas direções esquerda, direita, cima e baixo.
- Shift: Aumenta a velocidade da bola, aplicando aceleração.

### Exemplo de Saída

![Simulação MRU com Controle](https://via.placeholder.com/800x600)

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
