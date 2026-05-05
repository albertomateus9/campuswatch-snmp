# CampusWatch SNMP

**CampusWatch SNMP** é um sistema leve para monitoramento ativo do tráfego e saúde dos switches que compõem a infraestrutura de rede escolar.

Com foco em estabilidade, o sistema atua como o cérebro central para garantir que gargalos na rede sejam detectados antes de afetarem as aulas.

## Arquitetura: Manager vs Agents

O protocolo SNMP (Simple Network Management Protocol) baseia-se na dinâmica de Gerente e Agentes:
- **SNMP Agents**: São os switches e roteadores espalhados pela escola. Eles coletam dados de si mesmos (ex: tráfego nas portas, uso de CPU) e guardam na sua MIB (Management Information Base).
- **SNMP Manager (Esta API)**: É o nosso backend em Python. Ele ativamente "pergunta" (polling via SNMP GET/WALK) aos agentes como está o tráfego naquele momento.

## O Desafio (Hackathon)

Este repositório contém o esqueleto do Manager (Backend) e a base do Frontend (React). O desafio para os alunos no Hackathon é:

1. **Frontend (Dashboard)**: Os alunos deverão estruturar o React (pasta `dashboard/`) para consumir a API. O foco é exibir gráficos de linha mostrando o tráfego por porta.
2. **Polling Assíncrono**: Como o tráfego é contínuo, a interface gráfica precisará ser programada para fazer requisições assíncronas (ex: `setInterval` com `fetch`/`axios` ou WebSockets) para atualizar o dashboard automaticamente de tempos em tempos, simulando uma sala de controle real (NOC).

## Estrutura do Monorepo

*   `api/`: Backend em Python (FastAPI + PySNMP + SQLAlchemy) em Clean Architecture.
*   `dashboard/`: Frontend gerado em React/Vite.

## Instalação (Backend)

```bash
cd api
python -m venv venv
# Ative o venv
pip install -r requirements.txt
```

Boa caçada aos gargalos!
