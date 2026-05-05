from domain.entities import NetworkNode, TrafficMetric

class PollDeviceMetricsUseCase:
    def __init__(self, snmp_service, metric_repository):
        self.snmp_service = snmp_service
        self.metric_repository = metric_repository

    def execute(self, node: NetworkNode):
        \"\"\"
        Realiza as requisições SNMP (Get/Walk) para o dispositivo.
        Hackathon Challenge: Implementar o polling em paralelo para dezenas de switches.
        \"\"\"
        # data = self.snmp_service.get_interface_metrics(node.ip, node.snmp_community)
        # self.metric_repository.save(data)
        raise NotImplementedError("Implementar a coleta SNMP ativa.")

class AnalyzeTrafficBottleneckUseCase:
    def __init__(self, metric_repository):
        self.metric_repository = metric_repository

    def execute(self, node_id: str):
        \"\"\"
        Analisa a diferença (delta) de bytes_in/out para detectar saturação.
        \"\"\"
        raise NotImplementedError("Implementar análise de gargalos.")
