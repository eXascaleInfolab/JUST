This is the implementation for our graph embedding paper published in CIKM18:
JUST - Are Meta-Paths Necessary? Revisiting Heterogeneous Graph Embeddings

This code was developed using Python 2.7

Install requirements:
pip install -r requirements.txt 

How to run example:
python src/main.py --input Datasets/DBLP/dblp.edgelist --node_types Datasets/DBLP/dblp_node_types.txt --dimensions 128 --walk_length 100 --num_walks 10 --window-size 10 --alpha 0.5 --output dblp.embeddings

Input:
1) Edgelist format, the prefix of each node should indicate the node type.
typeID1 typeID2
2) Node_types: Structure of heterogeneous graph. Indicating heterogeneous connections. Eg:
author : paper
topic : paper
venue : paper
paper : author
paper : topic
paper : venue

Output:
Embedding file containing: Header + node id and d dimensional representation

Citing:
@inproceedings{hussein2018meta,
  title={Are Meta-Paths Necessary?: Revisiting Heterogeneous Graph Embeddings},
  author={Hussein, Rana and Yang, Dingqi and Cudr{\'e}-Mauroux, Philippe},
  booktitle={Proceedings of the 27th ACM International Conference on Information and Knowledge Management},
  pages={437--446},
  year={2018},
  organization={ACM}
}
