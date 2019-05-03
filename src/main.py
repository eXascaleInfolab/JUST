
import argparse
import numpy as np
import networkx as nx
import random
import math
from gensim.models import Word2Vec

def parse_args():
	parser = argparse.ArgumentParser(description="Just")

	parser.add_argument('--input')

	parser.add_argument('--node_types')

	parser.add_argument('--output')

	parser.add_argument('--dimensions' , type=int)

	parser.add_argument('--walk_length' , type=int)

	parser.add_argument('--num_walks' , type=int)

	parser.add_argument('--window-size' , type=int)
	
	parser.add_argument('--alpha' , type=float)

	parser.add_argument('--workers' , default=1)

	return parser.parse_args()

# number of memorized domains = 1
def dblp_generation(G, path_length, heterg_dictionary, start=None):
    
    path = []
    
    path.append(start)
    
    cnt = 1
    homog_length = 1
    no_next_types = 0
    
    heterg_probability = 0
    
    while len(path) < path_length:
		if no_next_types == 1:
			break
		
		cur = path[-1]
		homog_type = []
		heterg_type = []
		for node_type in heterg_dictionary:
			if cur[0] == node_type:
				homog_type = node_type
				heterg_type = heterg_dictionary[node_type]

		heterg_probability = 1 - math.pow(args.alpha, homog_length)
		r = random.uniform(0, 1)
		next_type_options=[]
		if r <= heterg_probability:
			for heterg_type_iterator in heterg_type:
				next_type_options.extend([e for e in G[cur] if (e[0] == heterg_type_iterator)])
			if not next_type_options:
				next_type_options = [e for e in G[cur] if (e[0] == homog_type)]
		else:
			next_type_options = [e for e in G[cur] if (e[0] == homog_type)]
			if not next_type_options:
				for heterg_type_iterator in heterg_type:
					next_type_options.extend([e for e in G[cur] if (e[0] == heterg_type_iterator)])	
		if not next_type_options:
			no_next_types = 1
			break
			
		next_node = random.choice(next_type_options)
		path.append(next_node)
		if next_node[0] == cur[0]:
			homog_length = homog_length + 1
		else:
			 homog_length = 1		

    return path

def generate_walks(G, num_walks, walk_length, heterg_dictionary):
  walks = []
  nodes = list(G.nodes())

  for cnt in range(num_walks):
    random.shuffle(nodes)
    for node in nodes:
		just_walks = dblp_generation(G, walk_length, heterg_dictionary, start=node)
		walks.append(just_walks)

  return walks

def generate_node_types():
	
  heterg_dictionary = {}
  heterogeneous_node_types = open (args.node_types)
  
  for line in heterogeneous_node_types:
	  node_type = (line.split(":")[0]).strip()
	  hete_value = (line.split(":")[1]).strip()
	  if node_type in heterg_dictionary.keys():
		  heterg_dictionary[node_type].append(hete_value)
	  else:
		  heterg_dictionary[node_type] = [hete_value]

  return heterg_dictionary

def main(args):
	G = nx.read_edgelist(args.input)
	heterg_dictionary = generate_node_types()
	walks = generate_walks(G, args.num_walks, args.walk_length, heterg_dictionary)
	model = Word2Vec(walks, size=args.dimensions, window=args.window_size, min_count=0, workers=args.workers)
	model.save_word2vec_format(args.output)


if __name__ == "__main__":
	args = parse_args()
	main(args)
