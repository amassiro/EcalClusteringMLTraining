import ROOT as root
import numpy as np

np.random.seed(1234)



def getDataFromFile(fileinfo, branchlist) :

  tfil = root.TFile(fileinfo)
  tree = tfil.Get('SimDigiTreeProducer/tree')
  datasize = tree.GetEntriesFast()
  
  print ("Reading NN inputs from " + fileinfo)
  data_sim  = np.zeros([datasize, 61200])
  data_digi = np.zeros([datasize, 61200])
  
  counter = 0
  
  for entry in tree :
    sim_idx = 0
    digi_idx = 0
    
    #print (" entry = ", entry)
    
    for branch in branchlist :
      for xtal in range (0, 61200): 
        if "sim" in branch:
          data_sim[counter][sim_idx] = getattr(entry, branch)[xtal*3+0]
          sim_idx = sim_idx + 1
        if "digi" in branch:
          data_digi[counter][digi_idx] = getattr(entry, branch)[xtal*10+4]
          digi_idx = digi_idx +1
          
    counter = counter + 1
  
  tfil.Close()

  return data_sim, data_digi



#
# ieta and iphi map
#

def getIetaIphiMapFromFile(fileinfo, branchlist) :

  tfil = root.TFile(fileinfo)
  tree = tfil.Get('SimDigiTreeProducer/tree')
  datasize = 1
  
  data_ieta  = np.zeros([61200])
  data_iphi  = np.zeros([61200])
  
  counter = 0
  
  for entry in tree :
    ieta_idx = 0
    iphi_idx = 0

    for branch in branchlist :
      for xtal in range (0, 61200): 
        if "ieta" in branch:
          value = getattr(entry, branch)[xtal]
          if value > -999: 
            data_ieta[ieta_idx] = value
          ieta_idx = ieta_idx + 1
        if "iphi" in branch:
          value = getattr(entry, branch)[xtal]
          if value > -999: 
            data_iphi[iphi_idx] = value
          iphi_idx = iphi_idx + 1
          
    counter = counter + 1
    
  tfil.Close()

  return data_ieta, data_iphi





#######################################
#
# Start here
#

inputfile = 'test.root'

# 
# Float_t         digi_ped_subtracted_EB[612000];
# Float_t         simenergy_EB[61200*3];
#

brlist  = ['simenergy_EB', 'digi_ped_subtracted_EB']
numvars = len(brlist)
ntrain  =  0.50   # 80% for train
ntest   =  1 - ntrain

print (" brlist = ", brlist)
data_sim, data_digi = getDataFromFile (inputfile, brlist)

#
# entries * 61200 = 
#
print (" data_sim.size  = " , data_sim.size )
print (" data_digi.size = " , data_digi.size)


#
# entries
#
print (" data_sim.len  = " , len(data_sim) )
print (" data_digi.len = " , len(data_digi))


#
# entries
#
#print (" data_sim.shape  = " , data_sim,shape )
#print (" data_digi.shape = " , data_digi.shape)


#
# now transform it into a 2D map to feed into the ML training
#
#
# [ nbatch, nDim==2, features per pixel]
#


#
# but first get the mapping
#

ietas, iphis = getIetaIphiMapFromFile(inputfile, ["ieta", "iphi"])

#
# entries * 61200 = 
#
print (" ietas.size  = " , ietas.size )
print (" iphis.size  = " , iphis.size )



print ("total = ",  (int(max(ietas) - min(ietas))* int(max(iphis) - min(iphis)))   )

print ( "iphi = " , int(max(iphis) - min(iphis)), " --> ", max(iphis), "   ", min(iphis) )
print ( "ieta = " , int(max(ietas) - min(ietas)), " --> ", max(ietas), "   ", min(ietas) )


#
# Super slow!!!!
#

#event = 0
#color = np.zeros(( int(max(ietas) - min(ietas))+1, int(max(iphis) - min(iphis))+1 ))

#counter = 0
#for i,j,k in zip(ietas, iphis, data_sim[event]):
  #if not (counter%1000) : print (counter, "   --->   ", i-int(min(ietas)) ,  "   ",  j-int(min(iphis)) )
  #color[int(i)-int(min(ietas))][int(j)-int(min(iphis))] = k
  ##print (counter)
  #counter = counter +1

#import matplotlib.pyplot as plt
#plt.imshow(color)    

#col = plt.colorbar()
#plt.xlabel("ieta")
#plt.ylabel("iphi")
#col.set_label("sim energy")





##inputs_digis = 

##[ nbatch, nDim==2, features per pixel]


#data_digi = np.asarray(data_digi)
#data_sim  = np.asarray(data_sim)



#from keras.models import Sequential
#from keras.layers import Dense, Conv2D, Flatten 
##create model 
#model = Sequential()
##add model layers 
#model.add(Conv2D(64, kernel_size=5, activation='relu', input_shape=(28,28,1))) 
#model.add(Conv2D(32, kernel_size=3, activation='relu')) 
#model.add(Flatten()) model.add(Dense(10, activation='softmax'))    
  
  

#datasize_bkg = data_input.size/numvars

#print "Splitting data between " + str(int(len(data_input)*ntrain)) + " training and " + str(int(len(data_input)*ntest)) + " testing samples bkg ..."

#data_input_train = data_input[ : int(len(data_input)*ntrain) ]
#data_input_test  = data_input[ int(len(data_input)*ntrain) : ]

#data_train = np.vstack( [ data_input_train] )
#data_test  = np.vstack( [ data_input_test ] )

