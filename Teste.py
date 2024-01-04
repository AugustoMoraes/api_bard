from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="cAjbhUI5FM3hNY0LR_1TKyqAu2eIIH0fuQARk59YOHCEmS-V-4698VGvILzk04Pso2MNCA."
input_text = "Qual a capital do Brasil?"
bard_output = Bard().get_answer(input_text)['content']
print(bard_output)