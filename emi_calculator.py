principal_amount = int(input("enter your total loan amount: "))
tenure = int(input("enter tour loan tenure: "))
rate_of_intererst_in_year = float(input("enter what percentage of interest are you paying: "))
																				#your_bank_name = input("enter your bank name: ")
rate_of_intererst_in_month = rate_of_intererst_in_year/12/100
																				#rate_of_intererst_in_month = 9/12/100
installments = tenure*12
																				#maintenance = 1500*12
																				#SBI_rate_of_interest = 7/12/100
																				#HDFC_bank_rate_of_interest = 7.5/12/100
																				#ICICI_bank_rate_of_interest = 8/12/100
																				#AXIS_bank_rate_of_interest = 8.10/12/100
																				#your_ROI = int(input("enter your interest rate:"))/12/100

emi_formula_1 = (principal_amount*rate_of_intererst_in_month*(1 + rate_of_intererst_in_month)**installments)
emi_formula_2 = ((1 + rate_of_intererst_in_month)**(installments)- 1)
emi = emi_formula_1/emi_formula_2

																			'''if (your_bank_name == ("SBI" or "sbi" or "Sbi")):
																				rate_of_intererst_in_month = SBI_rate_of_interest
																				print("Your bank name is: ",your_bank_name)
																				print("your monthly emi",emi)


																			elif (your_bank_name == ("HDFC" or "hdfc" or "Hdfc")):
																				rate_of_intererst_in_month = HDFC_bank_rate_of_interest
																				print("Your bank name is: ",your_bank_name)
																				print("your monthly emi",emi)

																			elif (your_bank_name == ("ICICI" or "icici" or "Icici")):
																				rate_of_intererst_in_month = ICICI_bank_rate_of_interest
																				print("Your bank name is: ",your_bank_name)
																				print("your monthly emi",emi)

																			elif (your_bank_name == ("AXIS" or "axis" or "Axis")):
																				rate_of_intererst_in_month = AXIS_bank_rate_of_interest
																				print("Your bank name is: ",your_bank_name)
																				print("your monthly emi",emi)

																			else:
																				print("you didn't enter your bank name")'''
print("your monthly emi",emi)
total_interest_you_paid = (emi * installments)- principal_amount
print("total interest you paid in your tenure",total_interest_you_paid)
processing_fees = 5000
print("Processing fees:",processing_fees)
total_amount_you_paid = principal_amount + total_interest_you_paid + processing_fees
print("your total money spend is:",total_amount_you_paid)
																						# total_amount_with_maintenance = total_amount_you_paid+ (maintenance*tenure)
																						# print("your total paid amount with maintenance:",total_amount_with_maintenance)