"""
Testes unitários para o Exercício 17.3 (exercicio_003.py).
"""

import unittest

from exercicio_003 import (
    LAN,
    LANEstrela,
    LANBarramento,
    LANAnel,
    LANHub,
    No,
    ComputadorPessoal,
    EstacaoTrabalho,
    Servidor,
    MaquinaFax,
    ImpressoraRede,
    Pacote,
    SimuladorLAN,
)


class TestHierarquiaNos(unittest.TestCase):
    """Valida a hierarquia de nós e dispositivos de rede."""

    def test_no_classe_abstrata(self):
        with self.assertRaises(TypeError):
            No("N1", "Nome", "MAC", "IP")  # type: ignore[abstract]

    def test_instanciacao_dispositivos(self):
        pc = ComputadorPessoal("PC-1", "PC Escritório", "00:11:22:33:44:55", "192.168.1.10")
        ws = EstacaoTrabalho("WS-1", "Workstation CAD", "00:11:22:33:44:56", "192.168.1.20")
        srv = Servidor("SRV-1", "Servidor BD", "00:11:22:33:44:57", "192.168.1.100")
        fax = MaquinaFax("FAX-1", "Fax Recepção", "00:11:22:33:44:58", "192.168.1.50")
        imp = ImpressoraRede("IMP-1", "Laserjet", "00:11:22:33:44:59", "192.168.1.60")

        self.assertEqual(pc.tipo_dispositivo, "Computador Pessoal (PC)")
        self.assertEqual(ws.tipo_dispositivo, "Estação de Trabalho (Workstation)")
        self.assertEqual(srv.tipo_dispositivo, "Servidor Corporativo")
        self.assertEqual(fax.tipo_dispositivo, "Máquina de Fax")
        self.assertEqual(imp.tipo_dispositivo, "Impressora de Rede")

        # Verifica recebimento e buffer
        pkt = Pacote("P1", "PC-1", "IMP-1", 500, "Imprimir")
        imp.receber_pacote(pkt)
        self.assertEqual(len(imp.buffer_recebimento), 1)
        self.assertEqual(imp.buffer_recebimento[0].id_pacote, "P1")


class TestHierarquiaTopologiasLAN(unittest.TestCase):
    """Valida as topologias derivadas de LAN (Estrela, Barramento, Anel, Hub)."""

    def test_lan_classe_abstrata(self):
        with self.assertRaises(TypeError):
            LAN("LAN Genérica", "Cabo", "Acesso", "Quadro", "Padrão", 100.0)  # type: ignore[abstract]

    def test_topologia_estrela_roteamento(self):
        estrela = LANEstrela(velocidade_mbps=1000.0)
        estrela.adicionar_no(ComputadorPessoal("PC-1", "PC 1", "M1", "10.0.0.1"))
        estrela.adicionar_no(Servidor("SRV-1", "Servidor", "M2", "10.0.0.2"))

        pkt = estrela.enviar_pacote("PC-1", "SRV-1", "Ping", tamanho_bytes=64)
        self.assertTrue(pkt.sucesso)
        self.assertEqual(pkt.rota, ["PC-1", "SWITCH-CENTRAL", "SRV-1"])
        self.assertGreater(pkt.tempo_transito_ms, 0.0)

    def test_topologia_barramento_roteamento(self):
        barramento = LANBarramento(velocidade_mbps=10.0, comprimento_cabo_metros=100.0)
        barramento.adicionar_no(ComputadorPessoal("PC-1", "PC 1", "M1", "10.0.0.1"))
        barramento.adicionar_no(ComputadorPessoal("PC-2", "PC 2", "M2", "10.0.0.2"))

        pkt = barramento.enviar_pacote("PC-1", "PC-2", "Dados", tamanho_bytes=1000)
        self.assertTrue(pkt.sucesso)
        self.assertEqual(pkt.rota, ["PC-1", "BARRAMENTO-COMPARTILHADO", "PC-2"])

    def test_topologia_anel_roteamento(self):
        anel = LANAnel(velocidade_mbps=16.0)
        anel.adicionar_no(ComputadorPessoal("N1", "Nó 1", "M1", "10.0.0.1"))
        anel.adicionar_no(ComputadorPessoal("N2", "Nó 2", "M2", "10.0.0.2"))
        anel.adicionar_no(ComputadorPessoal("N3", "Nó 3", "M3", "10.0.0.3"))

        pkt = anel.enviar_pacote("N1", "N3", "Token Message", tamanho_bytes=500)
        self.assertTrue(pkt.sucesso)
        # No anel N1 -> N2 -> N3
        self.assertEqual(pkt.rota, ["N1", "N2", "N3"])

    def test_topologia_hub_roteamento(self):
        hub = LANHub(velocidade_mbps=100.0)
        hub.adicionar_no(ComputadorPessoal("H1", "Nó 1", "M1", "10.0.0.1"))
        hub.adicionar_no(ComputadorPessoal("H2", "Nó 2", "M2", "10.0.0.2"))

        pkt = hub.enviar_pacote("H1", "H2", "Frame Ethernet", tamanho_bytes=1500)
        self.assertTrue(pkt.sucesso)
        self.assertEqual(pkt.rota, ["H1", "HUB-BROADCAST-PHY", "H2"])


class TestRequisitosSimuladorLAN(unittest.TestCase):
    """Valida especificamente os 8 requisitos listados no enunciado."""

    def setUp(self):
        self.sim = SimuladorLAN("estrela")
        self.pc = ComputadorPessoal("PC-A", "PC Alpha", "MAC-A", "192.168.0.1")
        self.ws = EstacaoTrabalho("WS-B", "WS Beta", "MAC-B", "192.168.0.2")
        self.srv = Servidor("SRV-C", "SRV Gamma", "MAC-C", "192.168.0.3")

        self.sim.somar_no(self.pc)
        self.sim.somar_no(self.ws)
        self.sim.somar_no(self.srv)

    def test_requisito_1_enumerar_nos(self):
        nos = self.sim.enumerar_nos()
        self.assertEqual(len(nos), 3)
        ids = [n.id_no for n in nos]
        self.assertIn("PC-A", ids)
        self.assertIn("WS-B", ids)
        self.assertIn("SRV-C", ids)

    def test_requisito_2_somar_novo_no(self):
        fax = MaquinaFax("FAX-D", "Fax Delta", "MAC-D", "192.168.0.4")
        self.sim.somar_no(fax)
        self.assertEqual(len(self.sim.enumerar_nos()), 4)

        # Nó duplicado deve gerar ValueError
        with self.assertRaises(ValueError):
            self.sim.somar_no(fax)

    def test_requisito_3_retirar_no(self):
        removido = self.sim.retirar_no("WS-B")
        self.assertEqual(removido.id_no, "WS-B")
        self.assertEqual(len(self.sim.enumerar_nos()), 2)

        # Remover nó inexistente deve gerar KeyError
        with self.assertRaises(KeyError):
            self.sim.retirar_no("INEXISTENTE")

    def test_requisito_4_configurar_topologia(self):
        self.assertEqual(self.sim.lan_ativa.topologia, "Estrela (Switch Central)")
        # Muda para barramento preservando os nós
        self.sim.configurar_topologia("barramento")
        self.assertEqual(self.sim.lan_ativa.topologia, "Barramento (Bus)")
        self.assertEqual(len(self.sim.enumerar_nos()), 3)

        # Muda para anel
        self.sim.configurar_topologia("anel")
        self.assertEqual(self.sim.lan_ativa.topologia, "Anel (Token Ring)")
        self.assertEqual(len(self.sim.enumerar_nos()), 3)

    def test_requisito_5_especificar_tamanho_pacote(self):
        self.sim.especificar_tamanho_pacote(512)
        self.assertEqual(self.sim.lan_ativa.tamanho_pacote_padrao, 512)

        # Tamanho inválido
        with self.assertRaises(ValueError):
            self.sim.especificar_tamanho_pacote(0)

    def test_requisito_6_enviar_pacote_unicast(self):
        pkt = self.sim.enviar_pacote("PC-A", "SRV-C", "Mensagem de Teste")
        self.assertTrue(pkt.sucesso)
        self.assertEqual(pkt.origem_id, "PC-A")
        self.assertEqual(pkt.destino_id, "SRV-C")
        self.assertEqual(len(self.srv.buffer_recebimento), 1)

        # Erro ao enviar para si mesmo
        with self.assertRaises(ValueError):
            self.sim.enviar_pacote("PC-A", "PC-A")

    def test_requisito_7_difundir_pacote_broadcast(self):
        pkts = self.sim.difundir_pacote("PC-A", "Broadcast Geral")
        # Deve entregar para WS-B e SRV-C (total de 2 destinatários)
        self.assertEqual(len(pkts), 2)
        destinos = [p.destino_id for p in pkts]
        self.assertIn("WS-B", destinos)
        self.assertIn("SRV-C", destinos)

    def test_requisito_8_estatisticas_lan(self):
        self.sim.enviar_pacote("PC-A", "WS-B")
        self.sim.enviar_pacote("WS-B", "SRV-C")
        self.sim.difundir_pacote("SRV-C")

        stats = self.sim.obter_estatisticas()
        self.assertEqual(stats["total_pacotes"], 4)  # 2 unicast + 2 broadcast
        self.assertEqual(stats["pacotes_sucesso"], 4)
        self.assertEqual(stats["taxa_sucesso_pct"], 100.0)
        self.assertGreater(stats["tempo_medio_ms"], 0.0)
        self.assertGreater(stats["total_bytes"], 0)


if __name__ == "__main__":
    unittest.main()
