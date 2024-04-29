QUAL A FUNÇÃO DE CADA ARQUIVO?

random_data:
Ele é um armazenamento de dados. Onde fica todas as informações (de pessoas/produtos/compras...), que será usado quando precisar "Puxar" a informação durante a progrmação

funcoes:
É onde fica todas as funções feitas no projeto

app:
o app, deixa armazenado todas as rotas feitas de cada função



CONFIGURANDO O GIT REMOTE PARA A SINCRONIZAÇÃO COM O GITHUB OU OUTRO REPOSITORIO REMOTO 
1. Acesse o repositório que deseja sincronizar.
Copie a URL do repositório. A URL geralmente pode ser encontrada na barra de endereço do navegador ou nas configurações do repositório.

2. Inicializar o Repositório Local: abra um prompt de comando ou terminal.
Execute o comando git init para inicializar o repositório Git local.

3. Adicionar o Repositório Remoto:

Utilize o comando git remote add para adicionar o repositório remoto que você copiou anteriormente. A sintaxe do comando é:
git remote add <nome-do-remoto> <url-do-repositório>
Substitua <nome-do-remoto> por um nome descritivo para o repositório remoto (por exemplo, origin).
Substitua <url-do-repositório> pela URL do repositório remoto que você copiou.

4. Verificar o Repositório Remoto: Utilize o comando git remote -v para verificar os repositórios remotos configurados para o seu repositório local.

5. Sincronizar com o Repositório Remoto: Utilize o comando git fetch para buscar as últimas alterações do repositório remoto. Isso não atualizará seus arquivos locais, mas permitirá que você visualize as alterações e as incorpore em seu trabalho.

6. Visualizar as alterações: Utilize o comando git status para verificar as alterações que foram buscadas do repositório remoto e que ainda não foram incorporadas ao seu trabalho local.

7. Incorporar as alterações: Utilize o comando git merge para incorporar as alterações buscadas do repositório remoto em seu trabalho local. Este comando pode gerar conflitos de mesclagem se você e outros colaboradores tiverem feito alterações nos mesmos arquivos.

8. Enviar suas alterações para o repositório remoto: Utilize o comando git push para enviar suas alterações locais para o repositório remoto. A sintaxe do comando é:
git push <nome-do-remoto> <branch>
Substitua <nome-do-remoto> pelo nome do repositório remoto que você configurou anteriormente (por exemplo, origin).
Substitua <branch> pelo nome do branch que você deseja enviar (geralmente master).