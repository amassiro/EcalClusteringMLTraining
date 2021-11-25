# EcalClusteringMLTraining

Dumper:

    https://github.com/amassiro/EcalClusteringML
    
    in 
    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_11_2_2_patch1/src/ECALValidation/EcalClusteringML
    
Where:

    /home/amassiro/Cern/Code/ECAL/EcalClusteringMLTraining
    
    

    
Plot:

    r99t test.root draw.cxx
    

Run:

    python train.py
    
    
In parallel on swan:

    /user/amassiro/projects/GPUECAL
    
    CNN ECAL.ipynb
    Development CNN.ipynb
    


Setup ssh on cerbero
====

Instructions from here: https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server

In local file:

    .ssh/config
    
write:

    Host cerbero
        Hostname cerbero.mib.infn.it
        User amassiro

On cerbero write in file 

    .ssh/authorized_keys
    
the public key from local



gpu4hep01
====

On gpu4hep01

    cd /gwpool/users/amassiro/

    
    