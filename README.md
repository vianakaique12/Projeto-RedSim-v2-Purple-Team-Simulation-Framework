🔴 RedSim v2 — Adversary Simulation Framework (Purple Team)
📌 Visão Geral

O RedSim v2 é um projeto educacional de simulação de comportamento adversário, desenvolvido para fins de Purple Team, SOC Training e Threat Modeling, com base no framework MITRE ATT&CK.

O objetivo do projeto é simular técnicas reais utilizadas por atacantes, permitindo que equipes defensivas compreendam, detectem e respondam a atividades maliciosas de forma controlada.

⚠️ Aviso Legal
Este projeto foi desenvolvido exclusivamente para fins educacionais e laboratoriais.
Nenhuma funcionalidade foi criada para uso malicioso em ambientes reais.

🎯 Objetivos do Projeto

Simular comportamento de ataque realista

Mapear técnicas ofensivas no MITRE ATT&CK

Apoiar treinamentos de SOC / Blue Team

Criar um artefato técnico para portfólio profissional

Demonstrar conceitos de Red Team e Purple Team

🧠 Conceitos Abordados

Adversary Simulation

MITRE ATT&CK

Red Team / Blue Team / Purple Team

Detecção baseada em comportamento

Logging e Telemetria

Persistence (simulada)

Command & Control (simulado)

🛠️ Ambiente de Execução

Linguagem: Python 3

Sistema Operacional: Windows (laboratório)

IDE: VS Code

🧩 Arquitetura do Projeto
RedSim-v2/
│
├── main.py                     # Orquestrador principal
├── logs/
│   └── activity.log            # Registro das ações simuladas
│
├── modules/
│   ├── enum_system.py          # Discovery (enumeração do sistema)
│   ├── simulate_c2.py          # Simulação de C2
│   ├── simulate_exfil.py       # Simulação de exfiltração
│   └── persistence.py          # Persistência simulada
│
└── README.md

🔥 Funcionalidades Implementadas
🔍 Discovery

Coleta informações básicas do sistema para simular reconhecimento inicial.

Sistema operacional

Versão do SO

Arquitetura

Hostname

Usuário logado

🔁 Persistence (Simulada)

Simula mecanismos de persistência com fins educacionais, sem alterar o sistema real.

Exemplo:

Criação de artefatos de persistência simulados

Registro em arquivos de log

📡 Command & Control (Simulado)

Simula comunicação com um servidor C2 de forma não maliciosa, apenas registrando eventos.

📤 Exfiltration (Simulada)

Simula o processo de exfiltração de dados, criando arquivos locais que representam dados “coletados”.

📝 Logging

Todas as ações do agente são registradas em:

logs/activity.log


Isso permite:

Auditoria

Análise defensiva

Simulação de alertas SOC

🧭 MITRE ATT&CK – Attack Matrix
Tática	Técnica	MITRE ID
Discovery	System Information Discovery	T1082
Discovery	User Discovery	T1033
Persistence	Boot or Logon Autostart Execution	T1547
Command & Control	Application Layer Protocol	T1071
Exfiltration	Exfiltration Over C2 Channel	T1041

✔️ Técnicas simuladas com foco em comportamento, não exploração real.

▶️ Execução

Na raiz do projeto:

python main.py


Ao final da execução, verifique:

logs/activity.log

🧠 Técnicas Demonstradas

Mapeamento de técnicas ofensivas

Pensamento orientado a comportamento adversário

Uso prático do MITRE ATT&CK

Criação de simulações seguras

Comunicação Red ↔ Blue Team
