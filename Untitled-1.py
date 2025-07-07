
from graphviz import Digraph

# Criando o diagrama BPMN simplificado com símbolos
dot = Digraph(format='png')
dot.attr(rankdir='LR', size='10')

# Raia: Procurador(a) Consulente
dot.attr('node', shape='rectangle', style='filled', fillcolor='#d0e1f9')
dot.node('D1', 'Receber Diligência')
dot.node('A1', 'Analisar necessidade de colaboração')
dot.node('F1', 'Preencher Solicitação')
dot.node('S1', 'Escolher colaborador\n(Equipe/Colega/Chefia)')
dot.node('E1', 'Enviar Solicitação')

# Raia: Colaboradores (Equipe / Colega / Chefia)
dot.attr('node', fillcolor='#f9e79f')
dot.node('R1', 'Receber Solicitação')
dot.node('C1', 'Elaborar contribuição')
dot.node('F2', 'Finalizar colaboração')
dot.node('R2', 'Retornar peça')

# Raia: Procurador(a) Consulente (continuação)
dot.attr('node', fillcolor='#d0e1f9')
dot.node('V1', 'Revisar peça final')
dot.node('D2', 'Decidir se há necessidade de\nassinatura coletiva')

# Decisão
dot.attr('node', shape='diamond', fillcolor='#ffffff', style='filled')
dot.node('DEC1', 'Assinatura coletiva?')

# Caminho Sim
dot.attr('node', shape='rectangle', fillcolor='#d0e1f9', style='filled')
dot.node('I1', 'Indicar assinantes')
dot.node('S2', 'Encaminhar para assinatura')

# Raia: Assinantes
dot.attr('node', fillcolor='#aed6f1')
dot.node('A2', 'Assinar peça')

# Final
dot.attr('node', fillcolor='#d0e1f9')
dot.node('F3', 'Finalizar tramitação')

# Fluxo de Conexões
dot.edges(['D1', 'A1', 'F1', 'S1', 'E1'])
dot.edge('E1', 'R1')
dot.edge('R1', 'C1')
dot.edge('C1', 'F2')
dot.edge('F2', 'R2')
dot.edge('R2', 'V1')
dot.edge('V1', 'D2')
dot.edge('D2', 'DEC1')

dot.edge('DEC1', 'I1', label='Sim')
dot.edge('I1', 'S2')
dot.edge('S2', 'A2')
dot.edge('A2', 'F3')

dot.edge('DEC1', 'F3', label='Não')

# Gerar arquivo
dot.render('bpmn_fluxo_colaborativo', cleanup=True)
