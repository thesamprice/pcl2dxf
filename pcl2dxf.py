import re,os,mmap
from dxfwrite import DXFEngine as dxf
class pcl_parser():
    def __init__(self,filename):
        self.constants = {}
        self.load_file(filename)
        #Move to the first target...
        
    def load_file(self,filename):
        self.filename = filename
        file = os.open(filename,os.O_RDONLY)
        self.map = mmap.mmap(file,0,prot=mmap.PROT_READ)
        
    def get_next_point(self):
        return self.map.readline().split()
if __name__ == "__main__":
    import sys
    #filename = sys.argv[1]
    filename = "joe.txt"
    pcl_file = pcl_parser(filename)

    a = pcl_file.get_next_point()
    point = (float(a[0]), float(a[1]),  float(a[2]))

    drawing = dxf.drawing('test.dxf')
    drawing.add_layer('TEXTLAYER', color=2)

    while a != []:
        point = (float(a[0]), float(a[1]),  float(a[2]))
        drawing.add(dxf.point(point))
        a = pcl_file.get_next_point()
        
    drawing.save()    
