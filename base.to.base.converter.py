'''Base to Base Number Converter
CREATOR: Tjimi Moana Cole
VERSION: 1.0
This program accepts as input an:
	Input value
	Input base
	Output base
and transparently converts the Input Value to an Output Value based on the Input Base and Output Base.'''
def get_decimal(in_value,in_base,out_base):
	decimal=0
	print()
#	print('INPUT VALUE\t',in_value)
#	print('INPUT BASE\t',in_base)
#	print('OUTPUT BASE\t'+out_base)						#input, input base.
	print()
	in_value=in_value[::-1]											#read input from right to left.
	print('INDEX','BASE '+in_base,'BASE '+out_base,sep='\t\t')
	for index in range(len(in_value)):								#for index in input...
		if ord(in_value[index])-55>9:								    	#if index is a letter...
			base10=ord(in_value[index])-55									#get its number as 10 plus how far past A it is (using ASCII code).
		else:                               								#else...
			base10=int(in_value[index])       								#get its number.
		decimal+=int(base10)*int(in_base)**int(index)      								#get in-base^index; mult by base-10 digit; add to total.
		                                								#repeat for all digits in input.
		print(index,in_value[index],int(base10)*int(in_base)**int(index),sep='\t\t')
	print('---------------------------------------')
	print('TOTAL          ',in_value,'            ',decimal)
	return decimal#return decimal value

def main():
	in_value=input('Input Value:\t')
	in_base=input('Input Base:\t')
	out_base=input('Output Base:\t')										#get in-value,in-base,out-base
	in_value=in_value.upper()
	decimal=get_decimal(in_value,in_base,out_base)								#get decimal value for in-value
	total=''
	print('\nOUTPUT VALUE in BASE',out_base)
	while decimal>0:             										#while decimal greater than 0...
		quotient=int(decimal)/int(out_base)										#get decimal divided by out base
		remainder=int(decimal)%int(out_base)    										#get remainder of decimal divided by out base
		total=str(remainder)+total    										#place remainder to left of total
		decimal=quotient			  										#replace decimal value with decimal divided by out base
								 											#repeat until decimal is 0
		print(total)													#output out-value
			
main()