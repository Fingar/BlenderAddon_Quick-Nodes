# Quick Math Nodes - Blender Addon

Tired of changing the operator-type of math nodes every time you want to multiply?
Ever wondered where the F%$&#$% Lerp node is?

...Me too!

So when I found out that Blender 4.0 added a great new search feature for nodes, I wrote this addon to make my life easier.
Maybe it will make your life easier too.

## What does it do?

It simply enhances the node editor's 'Add" menu by adding new entries with helpful names like 'Add (Math)', 'Multiply (Vector Math)', 'Dot Product (Vector Math)', etc., making them easily searchable!

For example, if you select "Multiply (Vector Math)", it will add Blender's standard "Vector Math" node to your graph and set its operator to "Multiply," saving you valuable time.

## Features
- Adds menu entries for all 'Math' operators (Add, Subtract, Multiply, Clamp, Sine, etc.)
- Adds menu entries for all 'Vector Math' operators (Add, Subtract, Multiply, Dot Product, Normalize, etc.)
- Adds menu entries for 'Mix / Lerp' (Float/Vector/Color)
- Works for both Shader Editor and Geometry Nodes! (yay!)

## Bug list
- Some menu entries are available in all node editors, even those that don't support them.
- Texture Nodes and Compositor are not supported.

Give it a try and simplify your Blender node workflow!

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