
from ij.plugin.frame import RoiManager

rm = RoiManager.getInstance()


from ij import IJ 

import random

imp = IJ.getImage()

IJ.run("ROI Manager...", "");

x = random.randint(1,2048)
y = random.randint(400,1200)

roi = imp.setRoi(x,y,400,400);

rm.addRoi(roi);

print imp

imp = imp.resize(400, 400, "bilinear");

IJ.run("Duplicate...", "new");

imp = IJ.getImage()

IJ.run(imp, "Find Edges", "");
IJ.setAutoThreshold(imp, "Default dark");
IJ.run(imp, "Convert to Mask", "");
IJ.run(imp, "Outline", "");

IJ.run("Hough Circle Transform","minRadius=5, maxRadius=30, inc=1, minCircles=1, maxCircles=65535, threshold=0.65, resolution=233, ratio=1.0, bandwidth=10, local_radius=10,  reduce show_mask show_centroids results_table");
