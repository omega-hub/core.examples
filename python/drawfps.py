fpsStat = Stat.find('fps')
# Add an initial fps sample or onDraw will fail when querying for fps on the
# first frame
fpsStat.addSample(0)

def onDraw(displaySize, tileSize, camera, painter):
    font = painter.getDefaultFont()
    painter.drawText("fps: " + str(fpsStat.getCur()), font, Vector2(5, 5), TextAlign.HALeft | TextAlign.VATop, Color(1, 1, 0, 1))

setDrawFunction(onDraw)

