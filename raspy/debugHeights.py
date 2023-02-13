import pickle

file = open("/home/pi/Documents/data/motorheights.txt","wb")
file.truncate(0)
pickle.dump([0]*5,file)
file.close()