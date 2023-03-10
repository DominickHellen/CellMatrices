from ij import IJ 
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog
import random

imp = IJ.getImage()



def Confluency():
	IJ.run(imp, "Find Edges", "");
	IJ.run(imp, "Manual Threshold...", "min=5141 max=65535");
	IJ.run(imp, "Convert to Mask", "");
	IJ.run(imp, "Convert to Mask", "");
	IJ.run(imp, "Dilate", "");
	IJ.run(imp, "Fill Holes", "");
	IJ.run(imp, "Analyze Particles...", "size=200-Infinity pixel circularity=0-1.00 show=Outlines summarize composite");
	
Confluency()
