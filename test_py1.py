import py1

# TESTES    
def test_nota_final():
    assert py1.nota_final(8,8,8) == 8 
 
def test_imc():
    assert py1.imc(100,100) == 0.01

def test_FtoC():
    assert py1.FtoC(122) == 50
