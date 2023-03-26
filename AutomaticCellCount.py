# Import necessary modules
from ij import IJ 
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog
import random

# Get the active image
imp = IJ.getImage()

# Define a function to count cells
def Cell_counter():
    
    # Find edges in the image to help with segmentation
	#These two steps below can be skipped and done by hand, depending on the focal plane & brightness of the image
    IJ.run(imp, "Find Edges", "");
    
    # Convert the image to a binary mask
    IJ.run(imp, "Convert to Mask", "");
    
    # Dilate the mask to fill in gaps between cells
	#These next steps below need to be run for everything
    IJ.run(imp, "Dilate", "");
    
    # Fill any holes in the mask
    IJ.run(imp, "Fill Holes", "");
    
    # Segment cells using watershed algorithm
    IJ.run(imp, "Watershed", "");
    
    # Analyze particles to count cells
    IJ.run(imp, "Analyze Particles...", "size=300-Infinity circularity=0.30-1.00 show=Outlines summarize");

# Call the function to count cells
Cell_counter()
