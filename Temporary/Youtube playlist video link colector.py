# =============================================================================
# Son promodbaghla te login kore "add to Download library" te click koris jegulo
# download hoe ni
# =============================================================================

import pafy
plurl = input("Enter The Link : ")
playlist = pafy.get_playlist(plurl)
l = len(playlist['items'])
print(l)
file = open("VideoInformation1.csv","w+")

def extract_name_from_title(s):
    name=""
    start = s.find("by")
    start = start+3
# =============================================================================
#     start = s.find("-")
#     start = start+2
# =============================================================================
    start = int(start)
    
    end = s.find("|")
    end = end-1
    end = int(end)
    name = s[start:end]
            
    return name

for i in range(0,5) :
    id = playlist['items'][i]['pafy'].videoid
    v=pafy.new(id)
    #video = pafy.new('https://www.youtube.com/watch?v='+id)
    name = extract_name_from_title(v.title)
    link = "https://www.youtube.com/watch?v={}".format(id)
    
# =============================================================================
#     ami actually akta code likhechi jeta te akta txt file a jader face
#     collect hoe ache tader name thakbe setar name hoche "Names.txt" tai
#     if part ta diechi repetative names jate na hoe
#     
# =============================================================================
    
# =============================================================================
#     with open('E:\\refined datasets\\Names.txt') as f:
#         if name in f.read():
#             f.close()
#             continue
#         else:
# =============================================================================
    print("Video Number : {}".format(i+1))
    file.write("{},{}\n".format(name,link))
    print("Done")
file.close()
# =============================================================================
#     print("Video title :{}".format(name))
#     print("Video Link : {}".format(link))
# =============================================================================
    

    
