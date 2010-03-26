"""
  for displaying a wire or other test shapes
"""
import os
import sys
import os.path
import wx
import logging
import time
import traceback
from OCC import STEPControl,TopoDS, TopExp, TopAbs,BRep,gp,GeomAbs,GeomAPI
from OCC import BRepBuilderAPI,BRepTools,BRepAlgo,BRepBndLib,Bnd,StlAPI,BRepAlgoAPI,BRepAdaptor
from OCC import BRepLProp,BRepGProp,BRepBuilderAPI,BRepPrimAPI,GeomAdaptor,GeomAbs,BRepExtrema
from OCC import BRepClass,GCPnts,BRepBuilderAPI,BRepOffsetAPI,BRepAdaptor,IntCurvesFace,Approx,BRepLib
from OCC.Display.wxDisplay import wxViewer3d


class AppFrame(wx.Frame):
  def __init__(self, parent,title,x,y,app):
      wx.Frame.__init__(self, parent=parent, id=-1, title=title, pos=(x,y),style=wx.DEFAULT_FRAME_STYLE,size = (400,300))
      self.canva = wxViewer3d(self);
      self.app = app;
  def showShape(self,shape):
		self.canva._display.DisplayShape(shape)
  def showShapes(self,listOfShape):
		for s in listOfShape:
			self.canva._display.DisplayShape(s);
			
  def eraseAll(self):
  		self.canva._display.EraseAll();
  def run(self):
	self.app.MainLoop();


app = wx.PySimpleApp()
wx.InitAllImageHandlers()
display = AppFrame(None,"Test Debug Display",1220,20,app)
display.canva.InitDriver()
display.canva._display.SetModeWireFrame()
display.Show(True)	
app.SetTopWindow(display);