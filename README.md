🔴 RedSim v2 — Adversary Simulation Framework (Purple Team)
📌 Visão Geral

RedSim v2 é um projeto educacional de simulação de comportamento adversário, desenvolvido para Purple Team, treinamento de SOC e Threat Modeling, com base no framework MITRE ATT&CK.

O projeto simula técnicas reais utilizadas por atacantes, permitindo que equipes defensivas analisem, detectem e respondam a atividades maliciosas de forma controlada, segura e não exploratória.

⚠️ Aviso Legal
Este projeto foi desenvolvido exclusivamente para fins educacionais e laboratoriais.
Nenhuma funcionalidade foi criada para uso malicioso em ambientes reais ou produtivos.

🎯 Objetivos do Projeto

Simular comportamento de ataque realista

Mapear técnicas ofensivas ao MITRE ATT&CK

Apoiar treinamentos de SOC / Blue Team

Criar um artefato técnico para portfólio profissional

Demonstrar conceitos de Red Team, Blue Team e Purple Team

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

Sistema Operacional: Windows (ambiente de laboratório)

IDE: Visual Studio Code

🧩 Arquitetura do Projeto
RedSim-v2/
│
├── main.py                 # Orquestrador principal
│
├── logs/
│   └── activity.log        # Registro das ações simuladas
│
├── modules/
│   ├── enum_system.py      # Discovery (enumeração do sistema)
│   ├── simulate_c2.py      # Simulação de Command & Control
│   ├── simulate_exfil.py   # Simulação de exfiltração
│   └── persistence.py     # Persistência simulada
│
└── README.md

🔥 Funcionalidades Implementadas
🔍 Discovery

Simula o reconhecimento inicial do sistema, coletando informações básicas:

Sistema operacional

Versão do SO

Arquitetura

Hostname

Usuário logado

🔁 Persistence (Simulada)

Simula mecanismos de persistência sem modificar o sistema real, com foco educacional.

Exemplos:

Criação de artefatos simulados

Registro de eventos em logs

📡 Command & Control (Simulado)

Simula comunicação com um servidor C2 sem tráfego real, apenas registrando eventos para análise defensiva.

📤 Exfiltration (Simulada)

Simula o processo de exfiltração criando arquivos locais que representam dados “coletados”.

📝 Logging

Todas as ações do agente são registradas em:

logs/activity.log


Isso permite:

Auditoria

Análise defensiva

Simulação de alertas de SOC

🧭 MITRE ATT&CK — Mapeamento de Técnicas
Tática	Técnica	MITRE ID
Discovery	System Information Discovery	T1082
Discovery	User Discovery	T1033
Persistence	Boot or Logon Autostart Execution	T1547
Command & Control	Application Layer Protocol	T1071
Exfiltration	Exfiltration Over C2 Channel	T1041

✔️ Técnicas simuladas com foco em comportamento, não em exploração real.

▶️ Execução

Na raiz do projeto, execute:

python main.py


Após a execução, verifique:

logs/activity.log

🧠 Técnicas Demonstradas

Mapeamento de técnicas ofensivas

Pensamento orientado a comportamento adversário

Uso prático do framework MITRE ATT&CK

Criação de simulações seguras

Comunicação técnica entre Red ↔ Blue Team
