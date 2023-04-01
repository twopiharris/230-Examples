
public class Jniac {

	//super-simple assembler
	static int[] memory = new int[100];

	public static void main(String[] args) {
		clearMemory();

		int[] program = {1, 3, 50, 1, 5, 51, 2, 50, 51, 52, 3, 52, 4};
		loadMemory(program);
		run();
		printMemory();	
		
	} // end main
	
	
	public static void clearMemory(){
		for (int i = 0; i < memory.length; i++){
			memory[i] = 0;
		} // end for loop
	}  // end clearMemory
	
	public static void loadMemory(int[] program){
		clearMemory();
		for (int i = 0; i < program.length; i++){
			memory[i] = program[i];
		} // end for loop
	} // end loadMemory
	
	public static void printMemory(){
		for (int i = 0; i < memory.length; i++){
			System.out.println(i + "\t" + memory[i]);
		} // end printMemory
	} // end printMemory
	
	public static void run(){
		boolean keepGoing = true;
		int pc = 0;
		while(keepGoing){
			int nextCell = memory[pc];
			if (nextCell == 1){
				// store value in address
				pc++;
				int value = memory[pc];
				pc++;
				int location = memory[pc];
				memory[location] = value;
				pc++;
				
			} else if (nextCell == 2) {
				// add values of next two addresses, store sum in third address
				pc++;
				int a = memory[pc];
				pc++;
				int b = memory[pc];
				pc++;
				int location = memory[pc];
				memory[location] = memory[a] + memory[b];
				pc++;
			
			} else if (nextCell == 3){
				//output value in address
				pc++;
				int location = memory[pc];
				System.out.println(memory[location]);
				pc++;
				
			} else if (nextCell == 4){
				//quit
				keepGoing = false;
				
			} else {
				System.out.println("Error");
				keepGoing = false;
			} // end if
			
		} // end loop
	} // end run

} // end class def
