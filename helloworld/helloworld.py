from qiskit import QuantumCircuit, Aer, transpile, assemble

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = Aer.get_backend('qasm_simulator')
qobj = assemble(transpile(qc, simulator))
result = simulator.run(qobj).result()

print(result.get_counts())