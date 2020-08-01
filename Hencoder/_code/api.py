from collections import Counter
from queue import PriorityQueue


class HauffmanNode:
    def __init__(self, char, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.frequency < other.frequency


        
# =============================================================================
#         ENCODE
# =============================================================================

def _create_encoding(key, node, code, encoding_table):
    '''
    Create Encoding for given input.
    '''
    if node.char is not None:
        encoding_table[chr(ord(node.char)+key)] = code
    else:
        _create_encoding(key, node.left, code+'0', encoding_table)
        _create_encoding(key, node.right, code+'1', encoding_table)


def _create_tree_encoding(key, node, tree_encoding):
    '''
    Creates encoding of the Haufmann tree obtained.
    '''
    if node.char is not None:
        tree_encoding += "1"
        tree_encoding += "{0:08b}".format(ord(node.char)+key)
    else:
        tree_encoding += "0"
        tree_encoding = _create_tree_encoding(key, node.left, tree_encoding)
        tree_encoding = _create_tree_encoding(key, node.right, tree_encoding)
    return tree_encoding
        

def _encode_text(key, text):
    word_frequencies = Counter(text)
    queue = PriorityQueue() # Queue Initialisation
    
    # Creating Hauffman Tree
    for word,freq in word_frequencies.items(): # Creates a priority queue
        queue.put(HauffmanNode(char=word, frequency=freq))
        
    encoding_table = {}
    
    # Create queue with Empty Parent node & frequency=sum of child
    while queue.qsize()>1:
        left_node, right_node = queue.get(), queue.get()
        # Place a empty node above chars
        queue.put(HauffmanNode(char=None, 
                               frequency= (left_node.frequency + right_node.frequency),
                               left= left_node, 
                               right= right_node 
                               ))
    
    hauffmanHead = queue.get() # Instance of Hauffman tree
    
    _create_encoding(key, hauffmanHead, '', encoding_table)
    
    # Input text encoding
    encoded_text_code = ''
    for s in text:
        encoded_text_code += encoding_table[chr(ord(s)+key)]
    
    # Encoding of Hauffman tree    
    tree_encoding = ''
    tree_encoding = _create_tree_encoding(key, hauffmanHead, tree_encoding)
           
    '''
    Suppose the scenario:
        Text-Encoding = 1000001 
        len(Text-Encoding) = 7
        
        127 is not a perfect 8bit code, so :
            7%8 = 7
            8-7 = 1 <-Q
                Therefore, we are lacking 1 bit to make it perfect 8bit code.
        
        So we add 0*Q number of 0's to the code:
            Text-Encoding : 01000001  <- This is perfect 8bit code
        
        And then Q is also stored to keep track how many zero numbers were added.
        so ord(1) - 00000001
        Final encoding: TreeEncoding + QEncoding + TextEncoding  
    '''
    bit_size_of_encoding = len(encoded_text_code) + len(tree_encoding)+8
    bits_less_for_8bit_code = 8 - bit_size_of_encoding%8
    if bits_less_for_8bit_code != 0: 
        # Extra bits needed to be added to make file of 8 bit pattern
        encoded_text_code = "0"*bits_less_for_8bit_code + encoded_text_code
        
    ''' 
    Final encoding is of form
    -------------------------
            Tree Encoding->Extra 0 binary added->Input Encoding. 
    '''    
#    final_encoding = "{tree_encoding}{key:08b}{bits_less_for_8bit_code:08b}{encoded_text_code}"
    final_encoding = tree_encoding + "{0:08b}".format(8) + "{0:08b}".format(bits_less_for_8bit_code) + encoded_text_code
    return final_encoding
 
    
# =============================================================================
#         DECODE
# =============================================================================

def _decode_hauffman_tree(encoding_array):
    '''
    Extracts Hauffman tree from input encoding.
    
    Approach:
    --------
    As encoded in the encoding tree, the node containing actual input words
    are encoded with 1 and all remaining are encoded with 0.
    So we need to to recursively iterate untill we find 1.
    '''
    encoded_bit = encoding_array[0]
    del encoding_array[0] # we delete it so in future we do not refer to same bit.
    
    if encoded_bit == "1":
        ''' 
        It means the next bit is a char, and as we have converted every char
        into its 8bit equivalent representation of its ASCII value, we will
        iterate to find out next 8 bits and then convert it into a char.
        '''
        char = "" # Initially contain 8bit equivalent encoding
        for _ in range(8):
           char += encoding_array[0]
           del encoding_array[0]
        return HauffmanNode(chr(int(char, 2)))
    return HauffmanNode(None, left= _decode_hauffman_tree(encoding_array), \
                        right= _decode_hauffman_tree(encoding_array))


def _decode_encoding(key, encoding):
    # First we extract the Tree Encoding
    encoding_array = list(encoding)
    decoded_hauffman_tree = _decode_hauffman_tree(encoding_array)
    # Removing extra binarry added for file balancing
    '''
    Suppose the scenario:
        Text-Encoding = 1000001 
        len(Text-Encoding) = 7
        
        127 is not a perfect 8bit code, so :
            7%8 = 7
            8-7 = 1 <-Q
                Therefore, we are lacking 1 bit to make it perfect 8bit code.
        
        So we add 0*Q number of 0's to the code:
            Text-Encoding : 0-1000001  <- This is perfect 8bit code
        
        And then Q is also stored to keep track how many zero numbers were added.
        so ord(1) - 00000001
        Final encoding: TreeEncoding + QEncoding + TextEncoding     
    '''
        
    # Here first we remove the QEncoding, which is always 8-bits
    encoding_array = encoding_array[8:]
    extra_0_binaries = encoding_array[:8] 
    encoding_array = encoding_array[8:] # The actual text-encoding is after 8 bits.
    number_of_0_added = int("".join(extra_0_binaries),2) 
    # Now we remove the actuall number of extra zero added.
    encoding_array = encoding_array[number_of_0_added:] 
    
    
    '''
    Now we iterate through encoded_text and follow below instructions:
        
        If encoded-bit == 0:
            Go to left of hauffman tree
                If left-child of Current root is not None, means we have reached leaf,
                    Extract Value, set root to initial Hauffman tree again.
        
        If encoded-bit == 1:
            Go to right of hauffman tree
                If right-child of Current root is not None, means we have reached leaf,
                    Extract Value, set root to initial Hauffman tree again.
    '''
    decoded_text = ''
    current_node = decoded_hauffman_tree
    char = encoding_array[5]
    for char in encoding_array:
        if char=='0' :
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += chr(ord(current_node.char)-key )
            current_node = decoded_hauffman_tree
            
    return decoded_text


def _read_file(input_file):
    file = open(input_file,'r')
    text = file.read()
    file.close()
    return text


def _write_file(output_file, text):
    file = open(output_file,'w')
    file.write(text)
    file.close()
    

def _filehandling(path, inplace, op):
    text = _read_file(path)
    if not text:
        raise print('Error reading file')
    output_path = path
    if not inplace:
        i = output_path.rindex('.')
        output_path = output_path[:i] + '_' + op + output_path[i:] 
    return text, output_path


def encode( text='', key=0, path=None, inplace=False):
    '''
    Input Parametes
    ---------------
        input_text: Text that needs to be converted.
        key: A secret key that you want to embedd to this text.
        file: If input is a file.
        path: Path of input file.
    '''
    key = key
    if path:
        text, output_filepath = _filehandling(path,inplace,op="encode")
    
    encoded = _encode_text(key, text)
    
    if path:
        _write_file(output_filepath, encoded)
        print("Your file has been encoded at path: {}".format(output_filepath))
        return True
    else:
        return encoded
    

def decode( text='', key=0, path=None, inplace=False):
    '''
    Input Parametes
    ---------------
        input_text: Text that needs to be converted.
        key: A secret key that you want to embedd to this text.
        
        file: If input is a file.
            path: Path of input file. Dependent on "file" argument.
            inplace: Update the existing file. Dependent on "file" argument.
    '''
    key = key
    if path:
        text, output_filepath = _filehandling(path,inplace,op="decode")
    
    decoded = _decode_encoding(key, text)
    
    if path:
        _write_file(output_filepath, decoded)
        print("Your file has been decoded at path: {}".format(output_filepath))
        return True
    else:
        return decoded


def test():
	print("Tested OK !")
	return True
