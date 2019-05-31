## El Gamal ##

1. Run 'Elgamal_Complete'. This will generate primes of the form p, q = 2p + 1, along with our public and private keys.
2. 'public_key.txt' has (q,g,h) in separate lines.
3. 'private_key.txt' has (a).
4. The file 'p_val' consists of the value of p.
5. The plaintext is in the file 'plain_text.txt'. The current text is 'abcdefgh'.
6. Next, run 'ElGamal_Signature.py'. This creates a text file called 'sign.txt', containing the signature and r. 
7. Run 'ElGamal_Dec.py'. This will print True or False on the terminal according to whether the signature matches or not. 

## Existential Forgery ##

8. Run 'ElGamal_Existential_Forgery.py'. This will write the forged signature to 'forged_sign_', and the forged plain text to 'plain_text_forgery'
9. To verify this, run 'ElGamal_Verify_Existential_Forgery.py'. You will get 'True' if the signature matches, and 'False' otherwise

## Hashing ##

10. Run 'ElGamal_Hashing.py'. This will hash the value in 'plain_text.txt'. Repeat steps 6 and 7. 
