sboxes = [ [ [],[],[],[] ] for i in range(8)]

sboxes[0][0] = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7] 
sboxes[0][1] = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8] 
sboxes[0][2] = [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0] 
sboxes[0][3] = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13] 

sboxes[1][0] = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10] 
sboxes[1][1] = [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5] 
sboxes[1][2] = [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15] 
sboxes[1][3] = [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9] 

sboxes[2][0] = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8] 
sboxes[2][1] = [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1] 
sboxes[2][2] = [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7] 
sboxes[2][3] = [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12] 

sboxes[3][0] = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15] 
sboxes[3][1] = [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9] 
sboxes[3][2] = [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4] 
sboxes[3][3] = [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] 

sboxes[4][0] = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9] 
sboxes[4][1] = [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6] 
sboxes[4][2] = [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14] 
sboxes[4][3] = [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3] 

sboxes[5][0] = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11] 
sboxes[5][1] = [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8] 
sboxes[5][2] = [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6] 
sboxes[5][3] = [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] 

sboxes[6][0] = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1] 
sboxes[6][1] = [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6] 
sboxes[6][2] = [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2] 
sboxes[6][3] = [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] 

sboxes[7][0] = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7] 
sboxes[7][1] = [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2] 
sboxes[7][2] = [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8] 
sboxes[7][3] = [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 



def get_keys(bit_string_56):
    temp_arr = []
    temp_str = bit_string_56[16:] + bit_string_56[:16]
    for i in range(16):
        c = temp_str[0:24]+temp_str[-24:]
        temp_arr.append(c)
        temp_str = temp_str[16:] + temp_str[:16]
    
    key_array = temp_arr

    return key_array
# key = "01100011011001000110010101101010011000010110001000011100"
# print (get_keys(key))



def conv_pad(str):
    padded_array = ""
    for i in str:
        order = ord(i)
        bin_no = bin(order)
        bin_no = bin_no[2:]
        bin_no = ((8-len(bin_no))*'0') +  bin_no

        padded_array = padded_array + bin_no

    if len(padded_array)%64 != 0:   
        extra_padding = int(((int(len(padded_array)/64) + 1) * 64 - len(padded_array))/8)
        padded_array = padded_array + extra_padding*"00000011"

    return(padded_array)


def divide_conv_pad(str):
    temp_arr = []
    length = len(str)//64
    temp_str = ""
    for i in range(length):
        temp_str = str[(i*64):(i+1)*64]
        temp_arr.append(temp_str)
    divided_padded_array = temp_arr

    return divided_padded_array


# string = "romeoandjulietweregreatlovers"
# a = (conv_pad(string))
# print (a)
# print (divide_conv_pad(a))


def xor(initial_vec, block):
    xor = ""
    for i in range(len(initial_vec)):
        xor = xor + str(int(initial_vec[i]) ^ int(block[i]))

    return (xor) #this is 64 bits


def expand(str):
    expanded_str = str[31] + str[0:5] + str[3:9] + str[7:13] + str[11:17] + str[15:21] + str[19:25] + str[23:29] + str[27:32] + str[0]     
    return(expanded_str)



def sBox(string):#48 bit input

    div_str = []
    #write terrible code to divide into subblocks bcoz out of fx
    div_str.append(string[0:6])
    div_str.append(string[6:12])
    div_str.append(string[12:18])
    div_str.append(string[18:24])
    div_str.append(string[24:30])
    div_str.append(string[30:36])
    div_str.append(string[36:42])
    div_str.append(string[42:48])

    sBox_string = ""
    # print (div_str)

    for i in range(len(div_str)):
        temp = div_str[i]
        #fuckall logic for this because out of fucks
        a = temp[0]
        b = a + temp[5] 
        c =  temp[1:5]

        n = sboxes[i][int((b),2)][int(c,2)]
        n_bin = bin(n)

        if 'b' in n_bin:
            n_bin = n_bin[2:]
        if len(n_bin)<4:
            n_bin = (4-len(n_bin))*'0' + n_bin
        sBox_string = sBox_string + n_bin

    return sBox_string    

# # x = (sBox("011000110110010001100101011010100110000101101010"))

def pBox(string):

    pbox =  [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]
    b = string
    output = [None] * 32
    for i in range(len(b)):
        output[i] = b[pbox[i]]
    final_output = ""
    for i in output:
        final_output = final_output + i

    return final_output


def cbc(initial_vec,block, key, decr = False): #block = div_pad_arr 

    

    temp = conv_pad(block)  
    block = divide_conv_pad(temp)
    initial_vec = conv_pad(initial_vec)
    key = get_keys(key)

    if decr == True:
        key = key[::-1]
    encryption = []
    for i in range(len(block)):
        # print (i)
        if (i>0):
            if block[i-1] == block[i]:
                print("RAISE FLAG")
            # else:
                # print("loop mein hain")

        if decr == False:
            input_4_feistal_nw = (xor(block[i], initial_vec))
            initial_vec = feistal_nw(input_4_feistal_nw,key)
        else :
            input_4_feistal_nw = block[0]
            initial_vec = feistal_nw(input_4_feistal_nw,key)
            input_4_feistal_nw = (xor(block[i], initial_vec))

        encryption.append(initial_vec)

        

        
    return (encryption)

 

def feistal_nw(input_4_feistal_nw, keys):

    #input_4_feistal_nw is 64 bit block 
    #split into 32 and 32
    left = input_4_feistal_nw[:32]
    right = input_4_feistal_nw[32:]

    for i in range(0,16):

        expanded_right = expand(right)
        # print ("RIGHT",right, expanded_right)
        # print (len(expanded_right), "len of expanded right")
        temp_key_1 = keys[i]
        intermediate_step = xor(expanded_right, temp_key_1)
        # print (len(temp_key_1), len(intermediate_step), i)
        intermediate_step = sBox(intermediate_step)
        # print ("SbOx", intermediate_step)
        output_step = pBox(intermediate_step)
        # print ("pBox", output_step)
        temp = right
        right = xor(left, output_step)
        left = temp
        

    return (right + left)
        
def binary_key(key):
    padded_array = ""
    for i in key:
        order = ord(i)
        bin_no = bin(order)
        bin_no = bin_no[2:]
        bin_no = ((8-len(bin_no))*'0') +  bin_no
        padded_array = padded_array + bin_no

    return(padded_array)
 




string = "romeoandjulietweregreatlovers"
vector = "abcdefgh"
key = binary_key("Z8tb;a=")
encry = ("final",cbc(vector,string, key ), "\\")
print (encry)
decryption = cbc(vector,string, key, decr = True)
print (decryption)

