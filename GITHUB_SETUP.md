# 📋 Instruções para Criar e Conectar ao Repositório GitHub

## Passo 1: Criar o Repositório no GitHub

1. Acesse https://github.com/new
2. Preencha os campos:
   - **Repository name:** `FloodFill-FPAA`
   - **Description:** `Implementação do algoritmo Flood Fill com BFS para preenchimento de regiões conectadas em grid 2D. Inclui visualização colorida como ponto extra.`
   - **Public** (deixe como público para que qualquer um possa ver)
   - **Desmarque** "Initialize this repository with:" (já temos commits locais)
3. Clique em **Create repository**

---

## Passo 2: Conectar o Repositório Local ao GitHub

Após criar o repositório, você verá instruções na tela do GitHub. Execute os comandos abaixo no PowerShell (dentro da pasta `c:\Users\gscan\floodfill-projeto`):

### Opção A: Via HTTPS (mais simples)

```powershell
cd c:\Users\gscan\floodfill-projeto
git branch -M main
git remote add origin https://github.com/gscantoni/FloodFill-FPAA.git
git push -u origin main
```

**Quando solicitado, use seu GitHub Personal Access Token (PAT) como senha:**
1. Vá para https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome como "FloodFill-Upload"
4. Selecione escopo `repo` (full control of private repositories)
5. Gere o token e copie-o
6. Cole-o quando o Git pedir a senha

### Opção B: Via SSH (mais seguro, se tiver SSH key configurada)

```powershell
cd c:\Users\gscan\floodfill-projeto
git branch -M main
git remote add origin git@github.com:gscantoni/FloodFill-FPAA.git
git push -u origin main
```

---

## Passo 3: Verificar o Resultado

Após fazer push, acesse:
```
https://github.com/gscantoni/FloodFill-FPAA
```

Você deve ver todos os arquivos:
- ✅ `floodfill.py` - Código principal
- ✅ `README.md` - Documentação
- ✅ `requirements.txt` - Dependências
- ✅ `.gitignore` - Arquivos a ignorar
- ✅ `input.txt`, `input_complex.txt`, `input_many_regions.txt` - Exemplos

---

## 🎯 Próximos Passos (Opcional)

### Adicionar Topics (tags) ao Repositório:
1. Vá para Settings do repositório
2. Procure por "Topics"
3. Adicione: `flood-fill`, `bfs`, `graph-algorithms`, `python`, `fpaa`

### Adicionar uma GitHub Action (CI/CD - Opcional):
Crie `.github/workflows/python-test.yml` para rodar testes automaticamente em cada push.

### Adicionar Badges ao README:
```markdown
[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
```

---

## ⚠️ Dicas Importantes

1. **Nunca commit credentials/tokens** - Já adicionamos `.gitignore` para evitar isso
2. **Use branches** para trabalhar em features: `git checkout -b feature/nova-feature`
3. **Faça commits atômicos** - Um commit por feature/correção
4. **Escreva mensagens descritivas** em inglês ou português consistentemente

---

## 📞 Suporte

Se encontrar erro ao fazer push:
- Verifique sua conexão de internet
- Certifique-se de que o token/senha está correto
- Verifique se o repositório foi criado corretamente no GitHub
- Tente: `git remote -v` para verificar a URL remota
