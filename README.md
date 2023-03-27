# Automated-in-vitro-Cell-Matrices-in-Fiji #

## AutomaticROIandCellArea.py

Automated quantification of cell number, radius, and area in culture using randomized ROI selection and hugh circles. 
<br />
Must have Hough Circle Transform Installed <br />
link: https://imagej.net/plugins/hough-circle-transform
<br />

![Cell Matrices](https://user-images.githubusercontent.com/88243822/212144545-cd672258-93de-40a4-9759-9a825b085531.png)
<br />
### Outline
Manual: <br />
> Open brightfield image in Fiji
  
Code: <br />
> Insert code into File --> New --> Script... <br />
> Change Language --> Python <br />
> Random ROI selection --> Find Edges --> Auto Threshold --> Mask Conversion --> Binary Outline --> Hugh Circle Transform --> Data in Results Table <br />

### Must click run twice
<br />

##  AutomaticConfluency.py
Automated quantification of confluency (%area) in culture using binary masking, and particle analysis.
<br />

![Confluency schematic](https://user-images.githubusercontent.com/88243822/227949364-5429a69c-b34e-49be-bb66-069a4d45134d.png)
<br />
###  Outline
Manual: <br />
> Open brightfield image in Fiji <br />
Code: <br />
> Insert code into File --> New --> Script... <br />
> Change Language --> Python <br />
> Find Edges --> Custom (set) Threshold --> Mask Conversion --> Dilate --> Fill Holes --> Analyze particles (custom)--> Data in Results Table <br />

### better for cells that form dense patches or tight junctions
<br />

## AutomaticCellCount.py
Automated quantification of cell number in culture using binary masking, and particle analysis.
<br />

![Cell Count schematic](https://user-images.githubusercontent.com/88243822/227957937-d8402c27-e8b4-455a-a5dd-464b4513df68.png)
<br />
###  Outline
Manual: <br />
> Open brightfield image in Fiji <br />
Code: <br />
> Insert code into File --> New --> Script... <br />
> Change Language --> Python <br />
> Find Edges --> Mask Conversion --> Dilate --> Fill Holes --> Watershed --> Analyze particles (custom) --> Data in Results Table <br />

### better for sparse patches of cells
