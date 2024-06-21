# BDD Syntax Highlighter

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest or SpiraTeam"
This SpiraApp automatically highlights Gherkin syntax within Requirement Steps, Test Case Steps, and Risk Mitigations. It also adds a toolbar button to these details pages to export the artifact steps as an attached .feature file.

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
    - [x] officially supports Gherkin syntax in English, German, French, Portuguese, and Spanish.

## Using the SpiraApp
### Artifact Details Pages
When any user saves the description of a **Requirement *step***, **Test Case Test Step**, or **Risk Mitigation**:

- All Gherkin titles and keywords will be highlighted and bolded.
    - Title keywords: Feature, Scenario, Background, Scenario Outline, Scenario Template
    - Statement keywords: Given, When, Then, And, But
- All comments, quoted strings, and tags will be highlighted with unique colors.
    - Comments are lines starting with a # sign
    - Tags start with an @ symbol and contain any characters other than whitespace.

!!! info "When a user with modification permissions views an artifact with unformatted steps for the first time, this SpiraApp will apply BDD syntax highlighting to all steps/mitigations."

See screenshot below for an example of the syntax highlighting

![Shows the following step description with @tags colored in red, "Scenario: ..." line bolded and colored in blue, Given/When/Then keywords bolded and colored green, "quoted strings" colored in bright cyan, and the comment line starting with # colored in gray: `@bdd @highlighting (new line) Scenario: BDD syntax highlighting is applied on saving a requirement step (new line) Given I have written a requirement step using BDD syntax using words like “Scenario:, Given, When, Then” (new line) When I save the requirement step (new line) Then I will see that the BDD highlighting has been applied automatically. (new line) # -describes feature requested by Customer A` ](img/bdd-highlight-example.png)

A user with permissions to create Documents can use the **BDD Actions** > **Export Feature** toolbar button to export the viewed artifact's steps as a `.feature` file. This is available on the details pages for Requirements, Test Cases, and Risks, and adds the created document as an attachment to the current artifact. The app asks the user for a filename, and appends the name of the artifact to the *Feature:* line within the file itself. Any indentation within a step, including from ordered and unordered lists, is kept when each step is converted to a scenario, and all lines are indented two additional spaces from the left to create a proper Feature > Scenario hierarchy. Any text formatting will be removed automatically, and exporting other HTML elements like images, tables, and links are not supported and may lead to unexpected behavior.

### Gherkin words in officially supported Languages
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