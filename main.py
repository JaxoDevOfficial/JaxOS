import betatxt, jaxos
try:
  beta = bool(open("beta.txt", "r").read())
except:
  beta = False
betatxt.show(beta)
jaxos.run()