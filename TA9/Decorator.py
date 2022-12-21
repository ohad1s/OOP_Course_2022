"""
The decorator design pattern is a structural design pattern that allows you
 to add new behavior to existing objects dynamically by wrapping them in an object of a decorator class.
 This is an alternative to subclassing, which can be inflexible because it requires modifying the original
 class or creating a new subclass for each variation of behavior.
"""

class File:   # interface or abstract class
    def write(self, data):
        pass

class TextFile(File):
    def write(self, data):
        with open("text.txt", "w") as f:
            f.write(data)

class BinaryFile(File):
    def write(self, data):
        with open("binary.bin", "wb") as f:
            f.write(data)

class CompressedFile(File):   # decorator class
    def __init__(self, file):
        self._file = file

    def write(self, data):
        # Compress the data
        compressed_data = self._compress(data)
        # Write the compressed data to the underlying file
        self._file.write(compressed_data)

    def _compress(self, data):
        import zlib
        data2=bytes(data,"latin-1")
        compressed_data = zlib.compress(data2)
        return compressed_data

class EncryptedFile(File):    # decorator class
    def __init__(self, file):
        self._file = file

    def write(self, data):
        # Encrypt the data
        encrypted_data = self._encrypt(data)
        # Write the encrypted data to the underlying file
        self._file.write(encrypted_data)

    def _encrypt(self, data):
        # Implement data encryption here
        ciphertext = ""
        for ch in data:
            ch=str(ch)
            if ch.isalpha():
                shift_ch = chr((ord(ch) + 10 - 65) % 26 + 65)
                ciphertext += shift_ch
            else:
                ciphertext += ch
        return ciphertext

# Client code
text_file = TextFile()
encrypted_text_file = EncryptedFile(text_file)
compressed_encrypted_text_file = CompressedFile(encrypted_text_file)
compressed_encrypted_text_file.write("Hello, world!")

""" 
 In this example, we have a File class that represents a file and defines the interface for writing data to a file.
  We have two concrete file classes: TextFile and BinaryFile, which represent text files and binary files, respectively.
   Both of these classes implement the write method of the File class to write data to a file.

We also have two decorator classes: CompressedFile and EncryptedFile, 
which add additional functionality to the write method of the File class. The CompressedFile class compresses 
the data before writing it to the underlying file, and the EncryptedFile class encrypts the 
data before writing it to the underlying file.

To use the decorator pattern, we create a File object and wrap it in one or more decorator objects.
 When we call the write method on the outermost decorator object, the request is forwarded through the chain of decorators, 
 with each decorator adding its own behavior before or after forwarding the request to the next decorator or the wrapped File object.

In this example, we create a TextFile object and wrap it in an EncryptedFile 
decorator and a CompressedFile decorator. When we call the write method on the CompressedFile object, 
the data is first compressed and then encrypted before being written to the underlying TextFile object.
 """