from ij import IJ 
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog
import random

imp = IJ.getImage()

def Cell_counter():
#These two steps below can be skipped and done by hand, depending on the focal plane & brightness of the image
	IJ.run(imp, "Find Edges", "");
	IJ.run(imp, "Convert to Mask", "");
#These steps below need to be run for everything
	IJ.run(imp, "Dilate", "");
	IJ.run(imp, "Fill Holes", "");
	IJ.run(imp, "Watershed", "");
	IJ.run(imp, "Analyze Particles...", "size=300-Infinity circularity=0.30-1.00 show=Outlines summarize");

Cell_counter()
