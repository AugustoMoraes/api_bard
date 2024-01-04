import bardapi


# set your __Secure-1PSID value to key
token = 'bgjFDLQj1CVeKadn8uVBvL03OCe7yLwEL5IRfgoaFnt3G6HaYw9ortKWwhKMjtANvYuRcw.'
#token = 'bghcLiS7BdQwCEyLzrv3iKlmGyUjS_bYs6WcPStwCiInAf_tvYiuBGpumZlah6jTyCtM3A.' # CHAVE DO NAVEGADOR BRAVE COM O EMAIL devaugusto.moraes@gmail.com
#token = 'AIzaSyAwH_yWBH5UPdCq2rHu5Ijpf2a5h-5EA2U'
# set your input text
# input_text = "exemplo de tipos de dados em java"
#
# # Send an API request and get a response.
# response = bardapi.core.Bard(token).get_answer(input_text)
#
# print(response['content'])

bard = bardapi.Bard()

pergunta = 'Qual a capital do Brasil?'

response = bard.get_answer()

print(response)