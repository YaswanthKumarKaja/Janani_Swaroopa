'''Taxation Woes
In a country, there are N slabs for Income tax which are common for all age groups and genders. As an income tax officer, investigating a case,
 you have the amount of tax paid by each employee of an organization.

Considering the income tax slabs and rebates offered, you need to find the total amount paid by the organization in salaries to the employees 
to match it with the amount reported by the organization in its filed Income tax Returns.

Information regarding the income tax slabs, rebate amount and the income tax paid by each employee of the organization will be provided.

Rebate amount is subtracted from the total salary of each employee. Tax is calculated on the remaining amount. You need to calculate the sum 
of total salary paid to the employees in that year.

Constraints
Number of tax slabs = Number of percentage on tax slabs
0<= Rebate, tax paid, slab <=1000000

Input Format
First Line will provide the Amount in each slab, separate by space (' ')
Second Line will provide the percentage of tax applied on each slab. Number of values in this line will be same as that in line one, separate by space (' ')
Third Line will provide the Rebate considered
Fourth line will provide the tax paid by each employee, separate by space (' ')

Output
Total Salary paid by the organization to its employees
Example Input

300000 600000 900000
10 20 30
100000
90000 150000 210000 300000

Output
5300000

Explanation
Slabs and tax percentage indicate that for salary:
Between 0 - 300000, tax is 0%
Between 300001 - 600000, tax is 10%
Between 600001 - 900000, tax is 20%
Greater than 900001, tax is 30%
First, we exclude the rebate from the salary of each employee. This will be the taxable component of salary. 
Upon, taxable salary apply the slab and tax percentage logic. Upon computation, one finds that employees 
are paid amounts 1000000, 1200000, 1400000, 1700000 respectively, as salaries
. So, the total salary paid to all employees in that year will be 5300000.'''

slab=list(map(int,input().split()))
per=list(map(int,input().split()))
rebate=int(input())
emp_intax=list(map(int,input().split()))
total=0
emp_sal=[0]*len(emp_intax)
for i in range(len(emp_intax)):
    emp_sal[i]+=slab[0]
    emp_tax=emp_intax[i]
    for j in range(1,len(slab)):
        max_slab_tax=(slab[j]-slab[j-1])*per[j-1]/100
        if max_slab_tax<=emp_tax:
            emp_sal[i]+=(slab[j]-slab[j-1])
            emp_tax-=max_slab_tax
        else:
            curr_slab = emp_tax*100/per[j-1]
            emp_sal[i]+=curr_slab
            emp_tax-=curr_slab
    if emp_tax>0:
        emp_sal[i]+=emp_tax*100/per[-1]
    total+=emp_sal[i]+rebate
print(int(total))

