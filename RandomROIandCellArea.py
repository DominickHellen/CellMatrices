# Import necessary modules
from ij import IJ 
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog
import random

# Get the active image
imp = IJ.getImage()

# Convert the image to 8-bit to work with ROI manager
IJ.run(imp, "8-bit", "");

# Get the ROI manager instance and display it
rm = RoiManager.getInstance()
IJ.run("ROI Manager...", "");

# Get the dimensions of the image
width = imp.getWidth()
height = imp.getHeight()

# Generate random coordinates for the ROI
x = random.randint(1,width)
y = random.randint(1,height)

# Define a function to create and add a new ROI to the ROI manager
def ROI():
	# Set the ROI to a 300x300 square around the randomly generated coordinates
	roi = imp.setRoi(x,y,300,300);
	
	# Add the ROI to the ROI manager
	rm.addRoi(roi);
	
	# Create a duplicate of the image with the ROI
	IJ.run("Duplicate...", "new");

# Call the function to create a new ROI and add it to the ROI manager
ROI()
imp = IJ.getImage()

# Define a function to analyze cell geometries
def Cell_Geometrics():
	# Find edges in the image to help with segmentation
	IJ.run(imp, "Find Edges", "");
	
	# Automatically threshold the image to separate foreground from background
	IJ.setAutoThreshold(imp, "Default dark");
	
	# Convert the image to a binary mask
	IJ.run(imp, "Convert to Mask", "");
	
	# Outline the binary mask
	IJ.run(imp, "Outline", "");
	
	# Perform Hough circle transform to detect circular objects in the image
	IJ.run("Hough Circle Transform","minRadius=5, maxRadius=30, inc=1, minCircles=1, maxCircles=65535, threshold=0.6, resolution=233, ratio=1.0, bandwidth=10, local_radius=10,  reduce show_mask show_centroids results_table");

# Call the function to analyze cell geometries
Cell_Geometrics()
