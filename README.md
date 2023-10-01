# Quick Nodes 1.1.1 - Blender Addon

Tired of changing the operator-type of math nodes every time you want to do anything other than 'Add'?
Ever wondered where the F%$&#$% Lerp node is?

...Me too!

So when I found out that Blender 4.0 added a great new search feature for nodes, I wrote this addon to make my life easier.
Maybe it will you out too!


## What does it do?

It simply enhances the node editor's 'Add" menu by adding a bunch of new entries with helpful names like 'Add (Math)', 
'Multiply (Vector Math)', 'Dot Product (Vector Math)', 'Lerp', 'Split', etc., and then just adds the nodes and 
sets the correct mode or setting required for the feature you requested.!

For example, if you select "Multiply (Vector Math)", it will add Blender's standard "Vector Math" node to your graph and set its operator to "Multiply," saving you valuable time.


## Why is it called Quick Nodes?

Because it makes it super quick to work with nodes.

<br>

<b>All the usual suspects are here; Add, Subtract, Multiply, etc.</b><br>
![](https://raw.githubusercontent.com/Fingar/BlenderAddon_Quick-Math-Nodes/main/Examples/QuickMathNodes_Example_1.gif)

<b>... and the rest too.</b><br>
![](https://raw.githubusercontent.com/Fingar/BlenderAddon_Quick-Math-Nodes/main/Examples/QuickMathNodes_Example_2.gif)

<b>And if you have been looking for a "Lerp" node in Blender, well now you can just search for "Lerp", <br>and it will give you the correct mix node.</b><br>
![](https://raw.githubusercontent.com/Fingar/BlenderAddon_Quick-Math-Nodes/main/Examples/QuickMathNodes_Example_3.gif)

<b>And yes, it supports geometry nodes too!.</b><br>
![](https://raw.githubusercontent.com/Fingar/BlenderAddon_Quick-Math-Nodes/main/Examples/QuickMathNodes_Example_4.png)

<b>Oh, and compositor too!.</b><br>
![](https://raw.githubusercontent.com/Fingar/BlenderAddon_Quick-Math-Nodes/main/Examples/QuickMathNodes_Example_5.png)

<br>

Give it a try and simplify your Blender node workflow!

## New features and bug fixes in 1.1.1
- Separated the implementation logic so the node entries are not visible any and every node editor. <br> Implementation is now done on an editor to editor basis. 
- Added explicit implementation for Shader Node Editor
- Added explicit implementation for Geometry Node Editor
- Added explicit implementation for Compositor (limited to math, lerp color, split color)
- Can no longer attempt add quick nodes to empty node trees (would cause error)
- Added menu entries for 'Split / Separate' (Vector/Color)

## Features
- Menu entries for all 'Math' operators (Add, Subtract, Multiply, Clamp, Sine, etc.)
- Menu entries for all 'Vector Math' operators (Add, Subtract, Multiply, Dot Product, Normalize, etc.)
- Menu entries for 'Mix / Lerp' (Float/Vector/Color)

## Requirements

The addon is only supported on Blender 4.0 and newer. 
This is manly because of the new search feature, the addon isn't very useful without it.

You could try it on earlier versions, but you might have to change the blender version number in the "__init__.py"-file (just look for '"blender": (4, 0, 0)').

## Install

1. Download the latest release ZIP file from the [Releases](https://github.com/Fingar/BlenderAddon_Quick-Math-Nodes/releases) page of this repository.

2. Open Blender.

3. Navigate to Edit > Preferences > Add-ons.

4. Click the "Install..." button and browse to the downloaded ZIP file.

5. Enable the "Quick Math Nodes" addon by checking the checkbox next to it.

You're all set!
