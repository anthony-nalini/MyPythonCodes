nota1=float(input("informe a primeira nota"))
nota2=float(input("informe a segunda nota"))
nota3=float(input("informe a terceira nota"))
nota4=float(input("informe a quarta nota"))
media=(nota1+nota2+nota3+nota4)/4
if media>=7:
    print("aprovado com media: ",{media})
elif media<7 and media>=4:
    print ("recuperação")
else:
    print("reprovado")