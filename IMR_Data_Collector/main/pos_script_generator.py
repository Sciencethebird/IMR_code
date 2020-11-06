#!/usr/bin/env python
import sys
import os
import random

def main(args):
	n = int(args)
	#print("generate ", n, "camera position")
	f = open("camera_script.txt", mode='w')

	for i in range(n):
  		randx = random.uniform(-1.0, 1.0)
  		randy = random.uniform(-1.0, 1.0)
  		randz = random.uniform(1.5, 1.8)
  		out = "{},{},{}\n".format(randx, randy, randz)
  		#print(out)
  		f.write(out)
	f.close()
  	
if __name__ == '__main__':
    main(sys.argv[1])