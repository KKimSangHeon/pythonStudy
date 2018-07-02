import os

def makeSamplePage(directory):
 samplesFile=open(directory+"/samples.html","wt")
 samplesFile.write(doctype())
 samplesFile.write(title("Samples from "+directory))
 # Now, let's make up the string that will be the body.
 samples="<h1>Samples from "+directory+" </h1>"
 for file in os.listdir(directory):
  if file.endswith(".png"):
   samples=samples+"<p>Filename: "+file+"</p>"
   samples=samples+'<image src="'+file+'"height="100">'
 samplesFile.write(body(samples))
 samplesFile.close()


def doctype():
  return '<!DOCTYPE html>'


def title(titlestring):
  return "<html><head><title>"+titlestring+"</title></head>"


def body(bodystring):
  return "<body>"+bodystring+"</body></html>"


makeSamplePage(os.getcwd())
