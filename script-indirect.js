//LMC Simulator - CPU and FDE Cycle by 101Computing.net 
var clock=50;
var timelapse = 10000;
var paused = true;
var lookupTable = {
  "ADD": "1",
  "SUB": "2",
  "LDA": "5",
  "STA": "3",
  "HLT": "000",
  "INP": "901",
  "OUT": "902",
  "BRA": "6",
  "BRZ": "7",
  "BRP": "8"
};

var labels = {};
var inp;
var carryOn, pc;
var cycles = 0;
var logOnOff = true;

function highlightCellOff(cellid) {
  document.getElementById(cellid).style.backgroundColor="transparent"; 
}

function highlightCell(cellid) {
  document.getElementById(cellid).style.backgroundColor="#FF33FF";
  var tmp = setTimeout(function() {highlightCellOff(cellid)}, timelapse/clock);
}
function log(txt,reset=false) {
  if (reset) {
  document.getElementById("liveFeed").innerHTML = txt.replace("   ","&nbsp;&nbsp;&nbsp;") + "<br/>";
  } else {
  document.getElementById("liveFeed").innerHTML = document.getElementById("liveFeed").innerHTML + txt.replace("   ","&nbsp;&nbsp;&nbsp;") + "<br/>";  
  }
  if (logOnOff) {
  document.getElementById("log").innerHTML = document.getElementById("log").innerHTML + txt.replace("   ","&nbsp;&nbsp;&nbsp;") + "<br/>";
  document.getElementById("log").scrollTop = document.getElementById("log").scrollHeight;
  }
}

function switchLogFile() {
	logOnOff = !logOnOff;
}

function scanCode() {
  labels={};
  var counter = 0
  var code = document.getElementById("codeListing").value.toUpperCase();
  var lines = code.split('\n');
  
  for(var i = 0;i < lines.length;i++){
    var line = lines[i].trim();
    if (line!="") {
    var instruction = line.split(/\s+/);
    if (instruction.length==2) {
      if (instruction[1]=="DAT") {
        labels[instruction[0]]=counter;
        document.getElementById("cell_"+counter).value=0;
      } else if (!(instruction[0] in lookupTable)) {
        labels[instruction[0]]=counter;
      }     
    }
    if (instruction.length==3) {
      if (instruction[1]=="DAT") {
        labels[instruction[0]]=counter;
        document.getElementById("cell_"+counter).value=instruction[2];
      } else if (!(instruction[0] in lookupTable)) {
        labels[instruction[0]]=counter;  
      }       
    }
    counter++;
  } 
  }
  
}

function resetRAM() {
  for (var i = 0; i <=99; i++) {
    document.getElementById("cell_"+i).value="000";
  }
}  

function load() {
  clearInterval(carryOn);
  paused=true;
  document.getElementById("pausebtn").innerHTML='<i class="fa fa-play"></i>';
  cycles=0;
  
  //Reset Registers
  document.getElementById("pc").value="00";
  document.getElementById("mar").value="00";
  document.getElementById("mdr").value="00";
  document.getElementById("cir").value="00";
  document.getElementById("acc").value="00";
  
  //Reset Input/Ouput
  document.getElementById("input").value="";
  document.getElementById("output").value="";
  document.getElementById("log").innerHTML="";
  document.getElementById("liveFeed").innerHTML="";
  
  //reset RAM
  resetRAM();
  //scan code for labels
  scanCode();

  //Load program in RAM
  var counter = 0
  var code = document.getElementById("codeListing").value.toUpperCase();
  var lines = code.split('\n');
  for(var i = 0;i < lines.length;i++){
    var line = lines[i].trim();
    if (line!="") {
    
		var instruction = line.split(/\s+/);
		if (instruction.length==3) {
		  var label = instruction[0];
		  var opcode = instruction[1];
		  var operand = instruction[2];
		  labels[label] = counter;
		  if (operand in labels) operand = labels[operand];
		  //Indirect Addressing
		  if (operand.length>1) {
		    if (operand.substring(0,1)=="@") {
				operand=operand.substring(1);
			    if (operand in labels) operand = "@" + labels[operand];
			}
		  }
					  
		  if (opcode in lookupTable) {
			var encode = lookupTable[opcode] + operand;
			document.getElementById("cell_"+counter).value = encode;
			counter++;
		  } else if (opcode=="DAT") {
			counter++;
		  } else {  
			log("Error at line " + counter + " - Instruction not recognised");
		  }
		
		} else if (instruction.length==2) {
		  if (instruction[0] in lookupTable) {
			var opcode = instruction[0];
			var operand = instruction[1];
			
			if (operand in labels) operand = labels[operand];
			//Indirect Addressing
			if (operand.length>1) {
				if (operand.substring(0,1)=="@") {
					operand=operand.substring(1);
					if (operand in labels) operand = "@" + labels[operand];
				}
			}
			
			
			var encode = lookupTable[opcode] + operand;
			document.getElementById("cell_"+counter).value = encode;
			counter++;
		  } else {
			labels[instruction[0]] = counter;
			var opcode = instruction[1];
			if (opcode in lookupTable) {
			  var encode = lookupTable[opcode]
			  document.getElementById("cell_"+counter).value = encode;
			counter++  
		  } else if (instruction[1]=="DAT") {
			counter++;          
			} else {
			  log("Error at line " + counter + " - Instruction not recognised");
			}
		  } 
		  
		} else {
		  if (line in lookupTable) {
			 document.getElementById("cell_"+counter).value = lookupTable[line];
			 counter++;
		  } else {  
			  log("Error at line " + counter + " - Instruction not recognised");
		  }
		}
	}
  }
}

function processInstruction() {
  pc=parseInt(document.getElementById("pc").value);
  highlightCell("cell_"+pc);
  //Fetch Instruction
    log("----------------------------------------------",true);
    log("Fetching instruction...");
    var instruction = document.getElementById("cell_"+pc).value;
    log("   Set MAR to value held by Program Counter: " + pc);
    document.getElementById("mar").value = pc;
    log("   Increment Program Counter by 1");
    pc++;
    document.getElementById("pc").value = pc;
    log("   Fetch instruction from address stored in the MAR");
    log("   Fetched instruction: " + instruction + " stored in the MDR");
	log("   Copy instruction from the MDR to the CIR");
    document.getElementById("mdr").value = instruction;
    document.getElementById("cir").value = instruction;
	
    log("Decoding instruction stored in CIR...");
  
    // Halt instruction
    if (instruction=="000") {
      log("   HLT");
      log("Executing Instruction...");
      log("   Program stopped");
	  cycles++;
	  log("----------------------------------------------");
	  log("Program Executed in " + cycles + " FDE Cycles.");
	  cycles=0;
	  paused=true;
	  document.getElementById("pausebtn").innerHTML='<i class="fa fa-play"></i>';
      //carryOn=false;
      clearInterval(carryOn);
    } else if (instruction=="901") {
      //INPUT
      log("   INP");
      log("Executing Instruction...");
      log("   Waiting for user input");
      cycles++;
      //setTimeout(function() {inp = prompt("User Input:"); document.getElementById("input").value = //document.getElementById("input").value + inp + "\n"; document.getElementById("input").scrollTop = //document.getElementById("input").scrollHeight;
      //log("   Store user input in Accumulator: " + inp);
      //document.getElementById("acc").value = inp;},1);
	  inp = prompt("User Input:"); document.getElementById("input").value = document.getElementById("input").value + inp + "\n"; document.getElementById("input").scrollTop = document.getElementById("input").scrollHeight;
	  log("   Store user input in Accumulator: " + inp);
	  document.getElementById("acc").value = inp;
      
    } else if (instruction=="902") {
      //OUTPUT
      log("   OUT");
      log("Executing Instruction...");
      log("   Output value held in the Accumulator: " + document.getElementById("acc").value );
      cycles++;
	  document.getElementById("output").value = document.getElementById("output").value + document.getElementById("acc").value + "\n";
	  document.getElementById("output").scrollTop = document.getElementById("output").scrollHeight;
    } else {
      var opcode = instruction.substr(0,1);
      var operandAddress = instruction.substr(1);
	  var operand;
      if (operandAddress.substr(0,1)=="@") {  //Indirect Addressing
		  operand = document.getElementById("cell_"+operandAddress.substr(1)).value;
	  } else {
		  operand = operandAddress;
	  } 	  
	  
      var accumulator = parseInt(document.getElementById("acc").value)
      if (opcode=="1") {
        //ADD
        log("   ADD");
        log("Executing Instruction...");
        cycles++;
		var mdr = parseInt(document.getElementById("cell_"+operand).value);
        log("   Set MAR to the operand of the current instruction: " +operand);
        log("   Fetch data at the location held by the MAR and store it in the MDR: " + mdr);
        document.getElementById("mar").value = operand;
        document.getElementById("mdr").value = mdr;
        log("   Add MDR value to the Accumulator and store the result in the Accumulator: " + accumulator + "+" + mdr +"="+(accumulator+mdr) );
		accumulator += mdr;
        document.getElementById("acc").value = accumulator;      
      } else if (opcode=="2") {
        //SUB
        log("   SUB");
        log("Executing Instruction...");
        cycles++;
		var mdr = parseInt(document.getElementById("cell_"+operand).value);
        log("   Set MAR to the operand of the current instruction: " +operand);
        log("   Fetch data at the location held by the MAR and store it in the MDR: " + mdr);
        document.getElementById("mar").value = operand;
        document.getElementById("mdr").value = mdr;
        log("   Subtratct MDR value from the Accumulator and store the result in the Accumulator: " + accumulator + "-" + mdr +"="+(accumulator-mdr) );
        accumulator -= mdr;
		document.getElementById("acc").value = accumulator;      
      } else if (opcode=="5") {
        //LDA
        log("   LDA");
        log("Executing Instruction...");
        cycles++;
		var mdr = parseInt(document.getElementById("cell_"+operand).value);
        document.getElementById("mar").value = operand;
        document.getElementById("mdr").value = mdr;
        document.getElementById("acc").value = mdr;          
        log("   Set MAR to the operand of the current instruction: " +operand);
        log("   Fetch data at the location held by the MAR (" +operand +") and store it in the MDR: " + mdr);
        log("   Store the MDR value in the Accumulator: " + mdr);
        
        } else if (opcode=="3") {
        //STA
        log("   STA");
        log("Executing Instruction...");
        cycles++;
		log("   Set MAR to the operand of the current instruction: " +operand);
        var mdr = parseInt(document.getElementById("acc").value);
        log("   Set MDR to the value held in the Accumulator: " +mdr);
        log("   Store MDR value " +mdr+ " at the memory location held in the MAR: "+operand);
        document.getElementById("mar").value = operand;
        document.getElementById("mdr").value = mdr;
        document.getElementById("cell_"+operand).value = mdr;
        } else if (opcode=="6") {
        //BRA
        log("   BRA");
        log("Executing Instruction...");
        cycles++;
		document.getElementById("pc").value = operand;
        pc=parseInt(operand);
        log("   Set PC to the operand of the instruction: " +operand);
          
        
        } else if (opcode=="7") {
        //BRZ
        log("   BRZ");
        log("Executing Instruction...");
        cycles++;
		log("   Check if the value held in the accumulator is 0")
        if (accumulator==0) {
           log("   0==0 - true");
           log("   Set PC to the operand of the instruction: " +operand);
           document.getElementById("pc").value = operand;
           pc=parseInt(operand);
        } else {
          log("   " + accumulator + "==0 - false");
        }
        } else if (opcode=="8") {
        //BRP
        log("   BRP");
        log("Executing Instruction...");
        cycles++;
		log("   Check if the value held in the accumulator is postive (>=0)")
        if (accumulator>=0) {
           log("   " + accumulator + ">=0 - true");
           log("   Set PC to the operand of the instruction: " +operand);
           document.getElementById("pc").value = operand;
           pc=parseInt(operand);
        } else {
          log("   " + accumulator + ">=0 - false");
        }
        
        }
    }

}
function step() {
  clearInterval(carryOn);
  paused=true;
  document.getElementById("pausebtn").innerHTML='<i class="fa fa-play"></i>';
  processInstruction();
}

function run() {
  clearInterval(carryOn);
  cycles=0;
  
  //Reset Registers
  document.getElementById("pc").value="00";
  document.getElementById("mar").value="00";
  document.getElementById("mdr").value="00";
  document.getElementById("acc").value="00";
  document.getElementById("log").innerHTML="";
  
  //Reset Input/Ouput
  document.getElementById("input").value="";
  document.getElementById("output").value="";
  
  //scan code for labels
  scanCode();
  
  clock = document.getElementById("clock").value;
  paused=false;
  document.getElementById("pausebtn").innerHTML='<i class="fa fa-pause"></i>';
  carryOn = setInterval(processInstruction, parseInt(timelapse/clock));
   
}

function pause() {
	if (!paused) {
	clearInterval(carryOn);
	paused=true;
	document.getElementById("pausebtn").innerHTML='<i class="fa fa-play"></i>';
	} else {
		paused=false;
		document.getElementById("pausebtn").innerHTML='<i class="fa fa-pause"></i>';
		if (cycles==0) {
			run();
		} else {
			clock = document.getElementById("clock").value;
			carryOn = setInterval(processInstruction, parseInt(timelapse/clock));
		}
	}
}

function selectProgram() {
  if (confirm("This operation will overwrite your current program. Are you sure you want to continue?")) {
	var option = document.getElementById("files").options[document.getElementById("files").selectedIndex].value;
	document.getElementById("codeListing").value = document.getElementById("code"+option).value;
	load();
  }
}


document.getElementById("codeListing").addEventListener('keydown',function(e) {
		if(e.keyCode === 9) { // tab was pressed
			// get caret position/selection
			var start = this.selectionStart;
			var end = this.selectionEnd;

			var target = e.target;
			var value = target.value;

			// set textarea value to: text before caret + tab + text after caret
			target.value = value.substring(0, start)
						+ "\t"
						+ value.substring(end);

			// put caret at right position again (add one for the tab)
			this.selectionStart = this.selectionEnd = start + 1;

			// prevent the focus lose
			e.preventDefault();
		}
	},false);