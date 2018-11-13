print ('Bonjour, marquez un nombre de 4 chiffres ')
chiffre = input("Entrez un nombre: ")
if len(chiffre) == 4 :


            l1 = sorted(chiffre)
            l2 = sorted(chiffre, reverse=True)

            chiffrel = l1 - l2

            print(chiffrel)
            while chiffrel != 6174 :
                if chiffrel < 0 :
                        chiffrel = -chiffrel

                        l1 = sorted(chiffree, reverse=False)
                        l2 = sorted(chiffree, reverse=True)

                    chiffrel = l1 - l2
                print(chiffrel)

                else :

                    print("voila c'est égale a 6174 a chaque fois")
                    print(chiffrel)
                    print(chiffrel)
                    print(chiffrel)
            #print (chain1)
            #print (chain2)
else :
        print('il faut 4 chiffres')
