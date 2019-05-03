This is the implementation for our graph embedding paper:
JUST - Are Meta-Paths Necessary? Revisiting Heterogeneous Graph Embeddings

How to run example:
python src/main.py --input Datasets/dblp.edgelist --node_types Datasets/dblp_node_types.txt --dimensions 128 --walk_length 100 --num_walks 10 --window-size 10 --alpha 0.5 --output dblp.embeddings

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
Header + node id and d dimensional representation

Citing:
@inproceedings{hussein2018meta,
  title={Are Meta-Paths Necessary?: Revisiting Heterogeneous Graph Embeddings},
  author={Hussein, Rana and Yang, Dingqi and Cudr{\'e}-Mauroux, Philippe},
  booktitle={Proceedings of the 27th ACM International Conference on Information and Knowledge Management},
  pages={437--446},
  year={2018},
  organization={ACM}
}