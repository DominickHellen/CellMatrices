# Import necessary modules
from ij import IJ 
import random

# Get the active image
imp = IJ.getImage()

# Define a function to calculate confluency
def Confluency():
    
    # Find edges in the image to help with segmentation
    IJ.run(imp, "Find Edges", "");
    
    # Manually threshold the image to separate foreground from background
    IJ.run(imp, "Manual Threshold...", "min=5141 max=65535");
    
    # Convert the image to a binary mask
    IJ.run(imp, "Convert to Mask", "");
    
    # Dilate the mask to fill in gaps between cells
    IJ.run(imp, "Dilate", "");
    
    # Fill any holes in the mask
    IJ.run(imp, "Fill Holes", "");
    
    # Analyze particles to calculate confluency
    IJ.run(imp, "Analyze Particles...", "size=200-Infinity pixel circularity=0-1.00 show=Outlines summarize composite");

# Call the function to calculate confluency
Confluency()
