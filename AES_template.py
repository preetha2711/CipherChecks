SBOX = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)


def byte2array(bytes):
    """Converts bytes to 4 x 4 array
    :param bytes: bytes
    :return: 4 x 4 array
    """
    array = []
    for i, byte in enumerate(bytes):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i // 4].append(byte)
    return array


def array2hex(array):
    """Converts 4 x 4 array to hex string
    :param array: array
    :return: hex string
    """
    hexstr = ""
    for i in range(4):
        hexstr += ''.join('{:02x}'.format(x) for x in array[i])
    return hexstr


def getKeySchedule(key):
    """Returns key schedule of 44 words
    :param key: 128 bit master key
    :return: key schedule
    """
    temp_keys = 44 * [None]
    key_schedule = byte2array(key)
    for i in range(len(key_schedule)):
        if i%4==0:
            temp = key_schedule[i]
            for j in range(0,len(temp_keys),4):
                temp_keys[j] = temp
                
                temp = [temp[-1]] + temp[:3] 
        
        if i%4==1:
            temp = key_schedule[i]
            for j in range(1,len(temp_keys),4):
                temp_keys[j] = temp
                
                temp = [temp[-1]] + temp[:3] 

        
        if i%4==2:
            temp = key_schedule[i]
            for j in range(2,len(temp_keys),4):
                temp_keys[j] = temp
                
                temp = [temp[-1]] + temp[:3] 

        
        if i%4==3:
            temp = key_schedule[i]
            for j in range(3,len(temp_keys),4):
                temp_keys[j] = temp
                
                temp = [temp[-1]] + temp[:3] 


    key_schedule = temp_keys

    return key_schedule

global glob_state_ar 
def encrypt(plaintext, key_schedule):
    """Encrypts plaintext using key schedule
    :param plaintext: plaintext in hex
    :param key_schedule: key schedule
    :return: ciphertext in hex
    """
    state_array = byte2array(plaintext)
    round_0 = []
    round_0.extend([key_schedule[0],key_schedule[1],key_schedule[2],key_schedule[3]])
    ADD_ROUND_KEY(state_array,round_0)
    count = 0
    temp = []
    temp_key_sched = []

    for i in range(4,44):    
        temp.append(key_schedule[i])
        count += 1 

        if count % 4 == 0 :
            temp_key_sched.append(temp)
            count = 0
            temp = []
    words = temp_key_sched



    for i in words:
        a = SUBSTITUTE_BYTES(state_array)
        b = SHIFT_ROWS(a)
        state_array = ADD_ROUND_KEY(b,i)

    # Code here

    return array2hex(state_array)


def ADD_ROUND_KEY(state_array, key_array):
    """Performs ADD ROUND KEY
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    for i in range(4):
        for j in range(4):
            state_array[i][j] = state_array[i][j] ^ key_array[i][j]
    return state_array


def SUBSTITUTE_BYTES(state_array):
    """Performs SUBSTITUTE_BYTES
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    temp_state_arr = []
    for i in range(len(state_array)):
        temp = []
        for j in (state_array[i]):
            
            temp.append(SBOX[j])
        temp_state_arr.append(temp)
    
    state_array = temp_state_arr
    return state_array


def SHIFT_ROWS(state_array):
    """Performs SHIFT_ROWS
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    temp_arr_single = [None] * 4
    temp_arr = [[None,None,None,None] for i in range(4)]


    for i in range(4):
        for j in range(4):
            temp_arr[j][i] = state_array[i][j]
          
    
    state_array = temp_arr
    temp_state_arr = []
    for i in range(len(state_array)):
        if i%4==0:
            temp = state_array[i]   
            temp_state_arr.append(temp)
        if i%4==1:
            temp = state_array[i]
            temp = temp[1:] + [temp[0]]
            temp_state_arr.append(temp)
        if i%4==2:
            temp = state_array[i]
            temp = temp[2:] + temp[:-2]
            temp_state_arr.append(temp)
        if i%4==3:
            temp = state_array[i]
            temp = [temp[-1]] + temp[:3]
            temp_state_arr.append(temp)

    for i in range(4):
        for j in range(4):
            state_array[j][i] = temp_state_arr[i][j]

    return state_array
   

# print(SHIFT_ROWS([[i,i+1,i+2,i+3] for i in range(0,16,4)]))

key = "7750f228896eb4561b9cd67497aad0b1"
key_schedule = getKeySchedule(bytes.fromhex(key))

plaintext = ["27153a16906ef425d078796f71569cbe",
             "b6f2d9b55d607b9a3e23cb4b9e133a18",
             "1a9d31f65a985ae9dfb6344cc90ec75b",
             "4e90a7cd0d8bce7285161377f0fd6fca"]


ciphertext = []

for msg in plaintext:
    ciphertext.append(encrypt(bytes.fromhex(msg), key_schedule))

print(ciphertext)
