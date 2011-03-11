import math
try:
   import pylab
   HAVE_MATPLOTLIB = True
except ImportError:
   HAVE_MATPLOTLIB = False

def pearson(x,y):
   nx = len(x)
   ny = len(y)
   if nx != ny: return 0
   if nx == 0: return 0
   n = float(nx)
   meanx = sum(x)/n
   meany = sum(y)/n
   sdx = math.sqrt(sum([(a-meanx)*(a-meanx) for a in x])/(n-1) )
   sdy = math.sqrt(sum([(a-meany)*(a-meany) for a in y])/(n-1) )
   normx = [(a-meanx)/sdx for a in x]
   normy = [(a-meany)/sdy for a in y]
   return sum([normx[i]*normy[i] for i in range(nx)])/(n-1)

def benford_law():
   return [math.log10(1+1/float(i))*100.0 for i in xrange(1,10)]

def calc_firstdigit(dataset):
   fdigit = [str(value)[:1] for value in dataset]
   distr = [fdigit.count(str(i))/float(len(dataset))*100 for i in xrange(1, 10)]
   return distr

def plot_comparative(aset, bset, dataset_label):
   if not HAVE_MATPLOTLIB:
      print "No Matplotlib installed !"
      return False

   xaxis = pylab.arange(1, 10)
   pylab.plot(xaxis, aset, linewidth=1.0)
   pylab.plot(xaxis, bset, linewidth=1.0)
   pylab.xlabel("First Digit")
   pylab.ylabel("Perc. %%")
   pylab.title("Benfords's law for %s (Pearson's Corr. %.2f)" % (dataset_label, pearson(aset, bset)))
   pylab.legend((dataset_label, "Benford's Law"))
   pylab.grid(True)
   return pylab.show()
