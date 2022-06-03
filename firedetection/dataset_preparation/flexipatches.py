""" A very simple first take on composite fire/nofire detection dataset generation """



import sys
import gdal
import numpy as np
import os 
from imageio import imwrite
import json
#from matplotlib import pyplot as plt 

raster = gdal.Open(sys.argv[1])
band = raster.GetRasterBand(1)
# https://gisgeography.com/sentinel-2-bands-combinations/

composites ={
    "wf_natural_4_3_2": ["B04","B03","B02"],
    "wf_colorinfrared_8_4_3": ["B08","B04","B03"],
    "wf_12-11-04": ["B12","B11", "B04"],
    "wf_swinfrared12-8a-4": ["B12", "B8A", "B04"],
    "wf_agriculture11-8-2": ["B11","B08","B02"]
    }

ranges  = {
    "B12": [0,0.5],
    "B11": [0,0.7],
    "B08": [0,0.5],
    "B8A": [0,0.5],
    "B04": [0,0.5],
    "B03": [0,0.5],
    "B02": [0,0.5]
}
bands = dict()

def scale(x, sc):
    x = x - sc[0]
    x = x / (sc[1] - sc[0])
    # truncate to 0,1
    x [ x < 0 ] = 0
    x[ x > 1] = 1
    return x
  


print("DEBUG: %s (%d x %d x %d)" % (os.path.basename(sys.argv[1]),raster.RasterXSize, raster.RasterYSize, raster.RasterCount))

for i in range(raster.RasterCount):
    description = raster.GetRasterBand(i+1).GetDescription()
    print("Band: %d (%s)" % (i+1, description))
    for key in ranges:
        if key in description:
            bands[key] = raster.GetRasterBand(i+1)

print(bands)
            

# Let us create some RGB patch first.
#for bandname in composite:
#    bands[bandname].ComputeStatistics(True)
#    print(bandname, "min",bands[bandname].GetMinimum())
#    print(bandname, "max",bands[bandname].GetMaximum())

cw,nodata,fire = [raster.GetRasterBand(i) for i in [9,10,11]]
print("Cloud (CW): %s" % (cw.GetDescription()))
print("NoData (nodata): %s" % (nodata.GetDescription()))
print("Fire (fire): %s" % (fire.GetDescription()))
# whole layers seems to be okay as we still have small products.
assert "Fire" in fire.GetDescription(),"Description of Fire band not correct. Expecting \"Fire\", got \"%s\"" %(fire.GetDescription())


# Data Loading (here we are time and memory consuming)
print("Data Stage...")
f = fire.ReadAsArray().astype(np.uint8) # Read Fire
nodata = (nodata.ReadAsArray()*4).astype(np.uint8)
cloud = (cw.ReadAsArray()*5).astype(np.uint8)
f = f + nodata + cloud; # this will effectively mask out clouds for fire and nofire.


b = {x:bands[x].ReadAsArray() for x in ranges}

print("Data Read Complete")
print(np.unique(f))

patch_size=[64,64]
assert patch_size[0] % 2 == 0, "Patchsize[0] must be divisble by 2"
assert patch_size[1] % 2 == 0, "Patchsize[1] must be divisble by 2"

    

np.random.seed(42)
x,y = np.where(f == 1) # fire
positions = np.vstack([x,y]).transpose()
np.random.shuffle(positions)

def write_patch(composite_name, classname, xslice, yslice):
    channels = [b[y][xslice, yslice] for y in composites[composite_name]]
    channels = [scale(x,ranges[s]) for x,s in zip(channels,composites[composite_name])]
    rgb = np.stack(channels, axis=-1)
    rgb *= 256
    rgb = rgb.astype(np.uint8)
    if not os.path.exists(composite_name):
        os.mkdir(composite_name)
    if not os.path.exists("%s/%s"%(composite_name,classname)):
        os.mkdir("%s/%s"%(composite_name,classname))
    imwrite ("%s/%s/%s-%s-%d-%d.png" %(composite_name,classname,classname,os.path.basename(sys.argv[1]).split(".")[0],p[0],p[1]), rgb)
    

# Find fires and write fire patches. ISSUE: all fires are central, maybe we should change this
numFires = 0
for p in positions:
    xslice = slice(p[0] - (patch_size[0] // 2),p[0] + (patch_size[0] // 2))
    yslice = slice(p[1] - (patch_size[1] // 2),p[1] + (patch_size[1] // 2))
    fire_extract = f[xslice,yslice]
    if 2 in fire_extract:
        continue
    # Create a suitable patch and de-patch it
    for c in composites:
        write_patch(c,"fire", xslice, yslice)
    #imwrite ("masks/mask-%s-%d-%d.png" %(sys.argv[1],p[0],p[1]), rgb)
    numFires = numFires + 1
#    plt.imshow(rgb)
#    plt.show()
#    plt.imshow(fire_extract)
#    plt.show()
    # Delete all patch information
    f[xslice,yslice] = 2

print("I found %d fires, trying to find %d negative samples as well" % (numFires, numFires))

# choose a random patch location for max 100*numFires times. Stop as soon as done
for i in range(200*numFires):
    p = [np.random.randint(patch_size[0] // 2 + 2, f.shape[0] - (patch_size[0] // 2 + 2)),
         np.random.randint(patch_size[1] // 2 + 2, f.shape[1] - (patch_size[1] // 2 + 2))]
    print(p)
    xslice = slice(p[0] - (patch_size[0] // 2),p[0] + (patch_size[0] // 2))
    yslice = slice(p[1] - (patch_size[1] // 2),p[1] + (patch_size[1] // 2))
    fire_extract = f[xslice,yslice]
    if (np.all((fire_extract == 0))):
        print("Negative sample at %s" %(str(p)))
        for c in composites:
            write_patch(c,"nofire", xslice, yslice)
        #write_patch("nofire", xslice, yslice)
        numFires = numFires - 1
        if numFires < 1:
            print("For each fire a no-fire was generated")
            break 
        f[xslice,yslice] = 2
        
