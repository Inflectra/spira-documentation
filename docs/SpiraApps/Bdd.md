# BDD

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest or SpiraTeam"

This SpiraApp automatically highlights Gherkin syntax within Requirement Steps, Test Case Steps, and Risk Mitigations <span class="pill">SpiraPlan</span>. It also adds a toolbar button to these details pages to export the artifact steps as an attached .feature file.

!!! info "About this SpiraApp"
    - [ ] system settings
    - [ ] product settings 
    - [ ] product template setup required
    - [x] runs automatically on the requirement details page
    - [x] runs automatically on the test case details page
    - [x] runs automatically on the risk details page
    - [x] toolbar button on requirement details page
    - [x] toolbar button on test case details page
    - [x] toolbar button on risk details page
    - [x] officially supports Gherkin syntax in English, German, French, Portuguese, Spanish, and other languages.

## Using the SpiraApp
### Automatic Highlighting on Details Pages
The BDD highlighting is automatically applied any time any user either opens a relevant details page, or when they save the description of a Requirement Step, Test Step (from the test case details page), or Risk Mitigation. Note that the user must be able to modify the artifact for the syntax highlighting to be applied.

- Syntax highlighting is added to all BDD/Gherkin titles and keywords at the start of lines:

    - **Title keywords**: Feature, Scenario, Background, Scenario Outline, Scenario Template
    - **Statement keywords**: Given, When, Then, And, But

- Syntax highlighting is added to all BDD comments, quotes, and tags:

    - **Comments** are lines starting with a # sign
    - **Quotes** are parts of a line enclosed in " " characters
    - **Tags** start with an @ symbol and contain any characters other than whitespace.

![Shows the following step description with @tags colored in red, "Scenario: ..." line bolded and colored in blue, Given/When/Then keywords bolded and colored green, "quoted strings" colored in bright cyan, and the comment line starting with # colored in gray: `@bdd @highlighting (new line) Scenario: BDD syntax highlighting is applied on saving a requirement step (new line) Given I have written a requirement step using BDD syntax using words like “Scenario:, Given, When, Then” (new line) When I save the requirement step (new line) Then I will see that the BDD highlighting has been applied automatically. (new line) # -describes feature requested by Customer A` ](img/bdd-highlight-example.png)

### Exporting from Details Pages
If you can create documents, you can use the "BDD Actions" > "Export Feature" toolbar button to export the current artifact's steps or mitigations as a `.feature` file. You will be asked to name the feature file, and it will then be saved to Spira's document repository for that product (at the root level). The first line of the feature file will be the name of the artifact itself (e.g. the requirement name). 

Please note that a feature file is a plain text file. Indentation is preserved but all other formatting is removed (including images, tables, links).

### Example Localizations
=== "French"
    - **And**: Et (que/qu/)
    - **Background**: Contexte
    - **But**: Mais (que/qu/)
    - **Feature**: Fonctionnalité
    - **Given**: Soit, Sachant (que/qu/), (Etant/Étant) donné (que/qu/), (Etant/Étant) donné(s/es)
    - **Scenario**: Exemple, Scénario
    - **Scenario Outline**: Plan du scénario
    - **Then**: Alors, Donc
    - **When**: Quand, Lorsque, Lorsqu

=== "German"
    - **And**: Und
    - **Background**: Grundlage, Hintergrund, Voraussetzungen, Vorbedingungen
    - **But**: Aber
    - **Feature**: Funktionalität, Funktion
    - **Given**: Angenommen, Gegeben sei, Gegeben seien
    - **Scenario**: Beispiel, Szenario
    - **Scenario Outline**: Szenariogrundriss, Szenarien
    - **Then**: Dann
    - **When**: Wenn
  
=== "Portuguese"
    - **And**: E
    - **Background**: Contexto, Cenário de Fundo, Cenario de Fundo, Fundo
    - **But**: Mas
    - **Feature**: Funcionalidade, Característica, Caracteristica
    - **Given**: Dad(o/a), Dad(os/as)
    - **Scenario**: Exemplo, Cenário, Cenario
    - **Scenario Outline**: Esquema do Cenário, Esquema do Cenario, Delineação do Cenário, Delineacao do Cenario
    - **Then**: Então, Entao
    - **When**: Quando

=== "Spanish"
    - **And**: Y, E
    - **Background**: Antecedentes
    - **But**: Pero
    - **Feature**: Característica, Necesidad del negocio, Requisito
    - **Given**: Dad(o/a), Dad(os/as)
    - **Scenario**: Ejemplo, Escenario
    - **Scenario Outline**: Esquema del escenario
    - **Then**: Entonces
    - **When**: Cuando