import torch
from torch_geometric.nn.models.gcn import GCN, GCNWithJK


def test_gcn():
    model = GCN(in_channels=8, hidden_channels=16, num_layers=3)
    out = 'GCN(16, 8, num_layers=3)'
    assert model.__repr__() == out

    x = torch.randn(3, 8)
    edge_index = torch.tensor([[0, 1, 1, 2], [1, 0, 2, 1]])

    out = model(x, edge_index)
    assert out.size() == (3, 16)

def test_graph_sagewithjk():
    model = GCNWithJK(in_channels=8, hidden_channels=16, num_layers=3)
    out = 'GCNWithJK(16, 8, num_layers=3)'
    assert model.__repr__() == out

    x = torch.randn(3, 8)
    edge_index = torch.tensor([[0, 1, 1, 2], [1, 0, 2, 1]])

    out = model(x, edge_index)
    assert out.size() == (3, 16)