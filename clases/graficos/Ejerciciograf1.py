import matplotlib.pyplot as mm

RegionWorld = ['Africa', 'America', 'Europe', 'United States', 'Asia-Pacific' ]
BillionariesPercentage = ['0-150','150-300','300-400','400-500', '500-600']

mm.bar(RegionWorld, BillionariesPercentage)
mm.title ('Number of billionaires per region of the world')
mm.xlabel('regions of the world')
mm.ylabel('Number of billionaires per region ')

mm.savefig('GraphicExample.png')
mm.show()