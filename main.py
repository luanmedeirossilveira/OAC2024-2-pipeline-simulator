from src.pipeline_simulator import PipelineSimulator
from src.register_file import RegisterFile
from src.memory_loader import load_program
from src.performance import calculate_performance

def main():
    program = load_program('instructions.txt')
    registers = RegisterFile()
    simulator = PipelineSimulator(program, registers)
    simulator.run()
    simulator.run_without_prediction()

    print("CICLO COM PREDIÇÃO: ", simulator.cycles_with_prediction, " CICLO SEM PREDIÇÃO: ", simulator.cycles_without_prediction)
    
    performance = calculate_performance(simulator.cycles_with_prediction, simulator.cycles_without_prediction)

    print(f"Melhoria de performance: {performance:.2f}%")

if __name__ == "__main__":
    main()
