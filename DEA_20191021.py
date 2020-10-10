import numpy as np
from gurobipy import *
f = open('d_{i,j}.txt','r')
print(f.read())
f.write(string)
try:
    # Create a new model
    no_input_factors=2;
    no_output_factors=2;
    no_units=6;
    m = Model('Practice DEA') #自己給定的模型名稱         
    # Create variables
    n = m.addVars(no_input_factors, vtype=GRB.CONTINUOUS, name='n')
    x = m.addVars(no_output_factors, vtype=GRB.CONTINUOUS,name='x')
    p = m.addVars(no_output_factors, vtype=GRB.CONTINUOUS,name='p')    
    # Integrate new variables
    m.update()
    # Set objective
    for i in I:
        m.setObjective(quicksum(x[i,j] for i,j in I,J), GRB.MINIMAN)
    ########################################################    
    # Set constraints
    constraint_1=0
    for s in range(no_input_factors):
        constraint_1+=x[j][s]*v[s]    
    m.addConstr(constraint_1==1)    
    ########################################################
    for k in range(no_units):
        rhs_const=lhs_const=0
        for r in range(no_output_factors):
            lhs_const+=y[k][r]*u[r]
        for s in range(no_input_factors):
            rhs_const+=x[k][s]*v[s]
        m.addConstr(lhs_const<=rhs_const)    
    ########################################################
    ########################################################
       
    m.optimize()
    m.write('mip1.lp')
 
    for uv in m.getVars():
        print(uv.varName,'=', uv.x)
    print('Obj=',  m.objVal)

except GurobiError:
    print('Encountered a Gurobi error')
