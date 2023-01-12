from ij import IJ 
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog
import random

imp = IJ.getImage()

rm = RoiManager.getInstance()
IJ.run("ROI Manager...", "");
width = imp.getWidth()
height = imp.getHeight()
x = random.randint(1,width)
y = random.randint(1,height)

def ROI():
	roi = imp.setRoi(x,y,300,300);
	rm.addRoi(roi);
	IJ.run("Duplicate...", "new");
		
ROI()
imp = IJ.getImage()

def Cell_Geometrics():
	IJ.run(imp, "Find Edges", "");
	IJ.setAutoThreshold(imp, "Default dark");
	IJ.run(imp, "Convert to Mask", "");
	IJ.run(imp, "Outline", "");
	IJ.run("Hough Circle Transform","minRadius=5, maxRadius=30, inc=1, minCircles=1, maxCircles=65535, threshold=0.6, resolution=233, ratio=1.0, bandwidth=10, local_radius=10,  reduce show_mask show_centroids results_table");

Cell_Geometrics()
