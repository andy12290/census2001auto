import pdftables_api
c = pdftables_api.Client('e3j22hhxx0ic')

for i in range(1,5):
	if (i<10):
		string='0'+str(i) 
	else:
		string=str(i)
	c.xlsx('district'+string+'.pdf', 'output'+string+'.xlsx')

  
