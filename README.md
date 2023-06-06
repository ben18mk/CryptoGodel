# CryptoGodel
Cryptography algorithm based on Gödel numbering

## Encryption
Each byte is encoded by Gödel numbering.
Then, chunk of the encoded byte's number is stored in a way that
<ul>
  <li>a chunk in an even index is stored in big endian</li>
  <li>a chunk in an even index is stored in little endian</li>
</ul>

## Decryption
Each chunk of each byte is retrieved in big endian or in little endian according to it's position.
Then, the chunks merge into a number that will be decoded by Gödel numbering.
