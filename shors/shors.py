from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
from qiskit.providers.aer import AerSimulator

shor = Shor()
qi = QuantumInstance(AerSimulator())
result = shor.factor(15, quantum_instance=qi)
print("Factors:", result.factors)