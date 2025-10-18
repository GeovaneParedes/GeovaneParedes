# 🐍 Guia Pythonic Avançado — Estilo Sênior  
**Autor:** DevGege  
**Versão:** 1.0  
**Linguagem:** Python 3.12+  
**Licença:** MIT  

---

## 📘 Sumário
1. [Palavras Reservadas](#-1-palavras-reservadas)
2. [Coringas Pythonic](#-2-coringas-pythonic)
3. [Macetes de Sênior](#-3-macetes-de-sênior)
4. [Desafios Pythonic](#-4-desafios-pythonic)
5. [Referências e Leituras Avançadas](#-5-referências-e-leituras-avançadas)

---

## 🧩 1. Palavras Reservadas

Palavras que **não podem ser usadas como identificadores**, pois são parte da sintaxe do Python.

| Categoria | Palavras |
|------------|-----------|
| **Controle de fluxo** | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `return`, `yield`, `try`, `except`, `finally`, `raise`, `assert`, `pass` |
| **Definições** | `def`, `class`, `lambda`, `async`, `await` |
| **Lógica e valores** | `True`, `False`, `None`, `and`, `or`, `not`, `is`, `in` |
| **Escopo** | `global`, `nonlocal`, `del` |
| **Módulos e imports** | `import`, `from`, `as` |
| **Pattern Matching** | `match`, `case` |
| **Gerenciamento de contexto** | `with` |

🔍 Verifique todas em tempo real:
```python
import keyword
print(keyword.kwlist)
```

---

## 🃏 2. Coringas Pythonic

### ⚡ Desempacotamento poderoso
```python
a, *b, c = [1, 2, 3, 4, 5]
# a=1, b=[2,3,4], c=5
```

### 🐋 Walrus Operator (`:=`)
```python
if (n := len(data)) > 10:
    print(f"Tamanho: {n}")
```

### 💡 Comprehensions elegantes
```python
pares = [x for x in range(20) if x % 2 == 0]
quadrados = {x: x**2 for x in range(5)}
```

### ⚙️ Geradores (economia de memória)
```python
def gerador():
    for n in range(1_000_000):
        yield n ** 2
```

### 📂 Context Managers
```python
with open("dados.txt") as f:
    conteudo = f.read()
```

### 🧠 Fatiamento
```python
texto = "Python"
print(texto[::-1])  # 'nohtyP'
```

### 🧩 Lambda + Sort
```python
alunos = [("Ana", 8), ("João", 10), ("Bia", 7)]
ordenado = sorted(alunos, key=lambda x: x[1], reverse=True)
```

### 🌈 *args e **kwargs
```python
def soma(*args):
    return sum(args)
print(soma(1, 2, 3, 4))
```

### 🎭 Decoradores
```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*a, **kw):
        print(f"Executando: {func.__name__}")
        return func(*a, **kw)
    return wrapper

@log
def teste():
    print("Rodando...")

teste()
```

### 🧱 Dataclasses
```python
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int

print(Usuario("DevGege", 30))
```

### 🔀 Pattern Matching
```python
match comando:
    case ["add", x, y]:
        print(int(x) + int(y))
    case ["exit"]:
        print("Saindo...")
```

### 🔤 F-strings avançadas
```python
valor = 12.3456
print(f"{valor:.2f}")  # 12.35
print(f"{valor=}")     # valor=12.3456
```

### ⚖️ Zip e unzip
```python
nomes = ["Ana", "Bia", "Caio"]
notas = [8, 9, 10]
for nome, nota in zip(nomes, notas):
    print(nome, nota)
```

---

## ⚙️ 3. Macetes de Sênior

| Tema | Dica |
|------|------|
| 🧠 **Legibilidade** | “**Readable > Clever.**” O código precisa ser fácil de manter, não apenas esperto. |
| ⚡ **Performance** | Prefira geradores (`yield`) para streams grandes. |
| 🧰 **Erros** | Sempre capture exceções específicas. `except ValueError:` é melhor que `except:` |
| 🧾 **Tipagem** | Use **type hints** e docstrings: `def soma(a: int, b: int) -> int:` |
| 🪶 **Arquivos** | Trabalhe com `pathlib` + `with open()` |
| 🧱 **CLI Profissional** | Use `argparse`, `click` ou `typer` para scripts reutilizáveis. |
| 🔄 **Resiliência** | Trate `KeyboardInterrupt`, salve progresso e retome depois. |
| 🧮 **Functools e Itertools** | Explore `lru_cache`, `partial`, `chain`, `combinations`. |
| 🧩 **Zen do Python** | Rode `import this` no terminal. Filosofia em 19 linhas. |
| 🔍 **Logs** | Substitua `print()` por `logging` com níveis e timestamps. |
| 🧪 **Testes** | Escreva funções puras e modulares. Prefira `pytest`. |
| 🌐 **Assíncrono** | Use `asyncio` e `aiofiles` para I/O massivo. |
| 🔬 **CPU-bound** | Use `concurrent.futures.ProcessPoolExecutor`. |
| 🧠 **Design Patterns** | Prefira dataclasses, context managers e mixins a herança complexa. |

---

## 🎯 4. Desafios Pythonic

### 🥇 Nível 1 – Júnior
✅ Reescreva um loop tradicional em *list comprehension*.

### 🥈 Nível 2 – Pleno
✅ Crie um decorador que exiba o tempo de execução de qualquer função.

### 🥇 Nível 3 – Sênior
✅ Implemente um sistema de *retry automático* com `asyncio`, `tqdm` e `logging`.

### 🧩 Bônus
✅ Crie um script CLI (`typer`) que baixe vídeos, mostre progresso e registre logs estruturados.

---

## 📚 5. Referências e Leituras Avançadas

- [The Zen of Python](https://peps.python.org/pep-0020/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Real Python – Advanced Tips](https://realpython.com/)
- [Effective Python, 2nd Edition (Brett Slatkin)](https://effectivepython.com/)
- [Python Tricks (Dan Bader)](https://dbader.org/python-tricks)
- [Asyncio – Official Docs](https://docs.python.org/3/library/asyncio.html)

---

💬 **"Ser Pythonic é transformar complexidade em elegância."**  
— *DevGege*
