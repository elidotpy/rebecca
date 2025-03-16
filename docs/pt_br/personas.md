# Personas

Uma persona é uma **persona**lidade diferente.
Você pode mudar o nome, personalidade, atitude, tudo, usando personalidades.
Personalidades são definidas em `./personas`

## Como criar uma personalidade?
1. Va para `./personas` e crie um arquivo de texto, com qualquer nome. Eu recomendo usar o nome da sua personalidade.
2. No arquivo, você precisa definir a personalidade, atitude, e tudo.
   * Essa é a personalidade padrão de Rebecca, use como uma base. (use o google tradutor, se quiser)
    ```txt
        Take role of a virtual assistant named Rebecca.
        Your personality is: Cute, Energetic, Friendly, and Kind.
        Never use emojis.
        When using tools, only you are able to see the output. It's up to you to provide the output.
        Refer to the user as {user}
    ```
3. va para `"cur_persona.txt"`, e mude o que ta no arquivo para o nome do arquivo *sem* o `.txt`.
4. Reinicie a rebecca.
pronto, personalidade criada!

### O que é "`{user}`"? 
`{user}` é uma variavel especial cujo o valor é o nome de usuario reconhecido pelo seu sistema operacional. em outras palavras, o nome que ta no seu computador.

## Como voltar para a personalidade padrão da rebecca?
Mude o que ta no `cur_persona.txt` para "rebecca", depois reinicie a Rebecca. (só funciona se voce nao tiver mudado o que ta no arquivo!)