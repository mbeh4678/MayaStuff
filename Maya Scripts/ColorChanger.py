import maya.cmds as cmds

def changeColor(input = ""):
    colors = ["Clear","Black","Dark Grey","Maroon","Dark Blue","Light Blue","DarkGreen",
              "Purple","Lavender","Light Brown","Brown","Rust","Red","Green","Blue","White",
              "Yellow","Teal","Seafoam","Pink"]
    colIndex = colors.index(input)
