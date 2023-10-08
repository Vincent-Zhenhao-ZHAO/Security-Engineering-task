from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256, SHA384, SHA512, SHA1, MD5

# read the public key and signature
public_key_path = "./public.key"
signature_path = "./signature.pem"

file1_path = "./message.txt"
file2_path = "./messageTwo.txt"

# read the public key and signature
public_key = RSA.import_key(open(public_key_path, "rb").read())
signature = open(signature_path, "rb").read()

# use different hash algorithm to verify the signature
hash_algorithm = [SHA384, SHA512, SHA256, SHA1, MD5]

file_names = [file1_path, file2_path]

# store the verified files and the hash algorithm used
verfied_file = {}
    
for each_file in file_names:
    
    with open(each_file, "rb") as f:
        # read the file
        message = f.read()
        # brute force the hash algorithms
        for hash_algo in hash_algorithm:
            try:
                # use the public key to verify the signature
                verfied_signature = PKCS1_v1_5.new(public_key)
                
                # get the hash object and update the message -> compouted hash value
                file_hash = hash_algo.new()
                file_hash.update(message)
                
                # verify the signature
                if verfied_signature.verify(file_hash, signature):
                    # store the verified file and the hash algorithm used
                    verfied_file[each_file] = hash_algo.__name__
            except:
                continue

print("The following files are verified:" + str(verfied_file))
print("The following files are not verified:" + str(list(set(file_names) - set(verfied_file.keys()))))
print("The following hash algorithms are used:" + str(list(set(verfied_file.values()))))
