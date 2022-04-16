# Fundamentos RSA
# Ricardo Ruiz

import rsa

(chave_pub, chave_priv) = rsa.newkeys(512)

mensagem = input("Digite a mensagem para criptografar: ").encode("utf8")
cripto = rsa.encrypt(mensagem, chave_pub)

print("\n> Mensagem Criptografada:\n%s" % cripto)
decripto = rsa.decrypt(cripto, chave_priv)
print("\n> Mensagem Decriptografada: \n%s" % decripto.decode("utf8"))