#criando a lista de afazeres
atividades = []

while True:
    #criando o menu
    print("""
         ________________________________________________
                                                          
                        LISTA DE AFAZERES                 
                                                          
               1- Inserir tarefas                         
               2- Listar tarefas                          
               3- Marcar como concluido                   
               4- Remover tarefa                          
               0- Sair                                    
         _________________________________________________ """)


    escolha = input("Qual opção da lista acima você deseja? ")
    
    
   
    if escolha == "1": #se a opção escolhida pela pessoa for = 1 insere tarefa
        print("Você escolheu inserir tarefas.")
        tarefa_inserir= input("Qual tarefa deseja inserir? ")
        atividades.append(tarefa_inserir)#append adiciona um item na lista
    
    if escolha == "2":#se a opção escolhida for = 2, lista as tarefas
        print("lista de tarefas: ")
        cont = 0   
        for tarefa in atividades:
            print (f"{cont} - {tarefa}")
            cont += 1 #acrescenta tarefas na lista
    
    if escolha == "3": #se a opção escolhida for = 3, a tarfa será marcada como concluida 
        print("Você escolheu marcar tarefa como concluida.")
        cont = 0  
        for tarefa in atividades:
            print (f"{cont} - {tarefa}")
            cont +=1
        tarefa_concluida = int(input("Qual tarefa deseja marcar como concluida?(escolha por número):"))
        atividades[tarefa_concluida] = atividades[tarefa_concluida] + "[X]"
            
        

    if escolha == "4": #se a opção escolhida pela pessoa for = 4, a tarefa será removida da lista
        print("Você escolheu remover tarefa.")
        item_remover = int(input("Oque você deseja remover da lista?(escolha por número): "))
        atividades.pop(item_remover) #removendo ítem da lista
    
    if escolha == "0":
        print(" Adeus! continue produtivo :) ")  #abrindo como arquivo escrito
        with open ("tarefas.txt", "w") as archive:
            for tarefa in atividades:
                archive.write(tarefa + "\n") #\n é como um enter para o computador, for e in é para percorrer a lista toda :)
                print("Lista de tarefas salva!!")
        break


   