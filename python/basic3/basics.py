<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<title>Working with data and files</title>
<!-- metadata -->
<meta name="generator" content="S5" />
<meta name="version" content="S5 1.1" />
<meta name="presdate" content="20050728" />
<meta name="author" content="Eric A. Meyer" />
<meta name="company" content="Complex Spiral Consulting" />
<!-- configuration parameters -->
<meta name="defaultView" content="slideshow" />
<meta name="controlVis" content="hidden" />
<!-- style sheet links -->
<link rel="stylesheet" href="ui/default/slides.css" type="text/css" media="projection" id="slideProj" />
<link rel="stylesheet" href="ui/default/outline.css" type="text/css" media="screen" id="outlineStyle" />
<link rel="stylesheet" href="ui/default/print.css" type="text/css" media="print" id="slidePrint" />
<link rel="stylesheet" href="ui/default/opera.css" type="text/css" media="projection" id="operaFix" />
<!-- S5 JS -->
<script src="ui/default/slides.js" type="text/javascript"></script>
</head>
<body>

<div class="layout">
<div id="controls"><!-- DO NOT EDIT --></div>
<div id="currentSlide"><!-- DO NOT EDIT --></div>
<div id="header"></div>
<div id="footer">
<h1>IUPUI Computer Science</h1>
<h2>Working with Data and Files</h2>
</div>

</div>


<div class="presentation">

<div class="slide">
<h1>Working with Data and Files</h1>
<h3>Andy Harris</h3>
<h4>IUPUI Computer Science</h4>
</div>

<div class="slide">
	<h1>Introducing Data</h1>
	<ul>
		<li>Increasingly complex programs are really about data</li>
		<li>Data is stored and loaded from files</li>
		<li>Sequential access data saves and loads text files</li>
		<li>External data is persistant</li>
		<li>Shared between applications</li>
		<li>Separates content from display</li>
	</ul>
</div>

<div class="slide">
	<h1>Writing to a text file</h1>
	<ul>
		<li>Load and run <a href="writeFile.py">writeFile.py</a> </li>
		<li>This program opens a text file</li>
		<li>It then writes code to the file</li>
		<li>Finally, it opens a previously created file</li>
		<li>The last item (chocolate) is appended to an existing file</li>
	</ul>
</div>

<div class="slide">
	<h1>File pointers</h1>
	<ul>
		<li>Opening a file creates a <em>file pointer</em></li>
		<li>This is a variable that refers to a file</li>
		<li>File pointers are used in subsequent file operations</li>
		<li>Use the <code>open()</code> command to get a file pointer</li>
		<li><code>open()</code>takes a file name and a mode</li>
	</ul>
</div>

<div class="slide">
	<h1>File Names</h1>
	<ul>
		<li>For now, work with text files in the current directory</li>
		<li>(same directory as the python program)</li>
		<li>Refer to a file with a relative reference</li>
		<li>Absolute references are not portable</li>
		<li>Different OSs use different path separation markers</li>
	</ul>
</div>

<div class="slide">
	<h1>File Open Modes</h1>
	<ul>
		<li>Read (r) - Read content from the file</li>
		<li>Write (w) - Write to the file</li>
		<li>Append (a) - Add contents to the end of the file</li>
		<li>Note - if you write to an existing file, you DESTROY the original</li>
		<li>Other nodes are available but not covered in this course</li>
	</ul>
</div>

<div class="slide">
	<h1>Writing to the text file</h1>
	<ul>
		<li>Use the <code>open()</code> function to create a file pointer</li>
		<li>Open the file "groceries.txt" for write access</li>
		<li>Write text to the file</li>
		<li>Note you'll need to include newlines yourself</li>
		<li>You can also use triple-quoted strings</li>
		<li>Close the file when finished</li>
	</ul>
</div>

<div class="slide">
	<h1>Why closing is important</h1>
	<ul>
		<li>Drives are much slower than memory</li>
		<li>Write commands don't always write to the physical disk</li>
		<li>Instead, they go to a memory buffer</li>
		<li>When the buffer is full, it writes to the hard drive</li>
		<li>Close finalizes the transfer, ensuring all content is on the drive</li>
	</ul>
</div>

<div class="slide">
	<h1>Appending to a file</h1>
	<ul>
		<li>You can add to the end of a file with append mode</li>
		<li>The file must be closed</li>
		<li>Open with append mode</li>
		<li>Subsequent write commands write to the end of the file</li>
	</ul>
</div>

<div class="slide">
	<h1>File notes</h1>
	<ul>
		<li>Files are stored in plain text</li>
		<li>You can check or edit contents in any text editor</li>
		<li>The extension is optional, but 'txt' denotes plain text</li>
		<li>It's customary to tell the user something happened</li>
	</ul>
</div>

<div class="slide">
	<h1>Reading a file</h1>
	<ul>
		<li>It's also easy to read the contents of a text file</li>
		<li>Load and run <code>readFile.py</code></li>
		<li>Use the <code>open()</code> function to open the file</li>
		<li>Open in Read mode (r)</li>
	</ul>
</div>

<div class="slide">
	<h1>Working with file contents</h1>
	<ul>
		<li>Normally a file is read one line at a time</li>
		<li>Use a for loop to read in the current line</li>
		<li>Loop ends when there are no more lines</li>
		<li>Current line is in the variable <code>line</code></li>
		<li>Use <code>strip()</code> method to clean up spaces and newlines</li>
	</ul>
</div>

<div class="slide">
	<h1>Building a basic text editor</h1>
	<ul>
		<li>Load and run <a href="textEdit.py">textEdit.py</a></li>
		<li>Based on Tk Text widget</li>
		<li>Incorporate tkFileDialog</li>
		<li>Includes menus</li>
		<li>Standard commands:</li>
		<li>New, Open, Save As, Exit</li>
	</ul>
</div>

<div class="slide">
	<h1>Introducing tkFileDialog</h1>
	<ul>
		<li>Acts as a proxy to local file dialog</li>
		<li>Calls up a familiar screen</li>
		<li>Allows the user to pick one or more files</li>
		<li>Picks a file name</li>
		<li>Alternately opens a file with the appropriate mode</li>
	</ul>
</div>

<div class="slide">
	<h1>Building the menu system</h1>
	<ul>
		<li>Begin by creating an instance of the <code>Menu</code> widget</li>
		<li>Use <code>self.config()</code> to attach the menubar to the app</li>
		<li>Build one or more drop-down menus in the same way</li>
		<li>Use <code>add_command</code> to add elements to the menus</li>
		<li>Each command has a label and a command</li>
	</ul>
</div>

<div class="slide">
	<h1>The New and Exit functions</h1>
	<ul>
		<li>The new command clears the text area</li>
		<li>Use <code>delete</code> to clear the current contents</li>
		<li>1.0 is the beginning of the text, END is the end</li>
		<li><code>quit</code> is a built-in method inherited from Tk</li>
		<li>There's no need to write it</li>
	</ul>
</div>

<div class="slide">
	<h1>The Save As function</h1>
	<ul>
		<li>Use the TkFileDialog to open a save as file dialog</li>
		<li>This returns a reference to a file opened for write access</li>
		<li>Extract text content from the text element</li>
		<li>Write it to the file</li>
		<li>Close the file</li>
	</ul>
</div>

<div class="slide">
	<h1>The Open function</h1>
	<ul>
		<li>Use tkFileDialog to open an input file</li>
		<li>This returns a reference to a file opened for read access</li>
		<li>Initialize text to empty</li>
		<li>Read in each line of text</li>
		<li>append to the text variable</li>
		<li>Clear the Text area and insert the text</li>
		<li>close the file</li>
	</ul>
</div>

<div class="slide">
	<h1>Introducing CSV files</h1>
	<ul>
		<li>Sometimes you need a bit more formatting</li>
		<li>Comma - Separated Files are one technique</li>
		<li>Each line is a record</li>
		<li>Each field separated by a comma (or other character)</li>
		<li>Can be used by spreadsheets, databases, and other tools</li>
		<li>look at <a href="contacts.csv">contacts.csv</a>
	</ul>
</div>

<div class="slide">
	<h1>Reading a CSV file</h1>
	<ul>
		<li>load and run <a href="csvDemo.py">csvDemo.py</a></li>
		<li>Open csv file in read mode</li>
		<li>Read in one line at a time</li>
		<li>Split each line into an array</li>
		<li>Assign array elements to scalar variables</li>
		<li>Work with the data and close the file</li>
	</ul>
</div>

<div class="slide">
	<h1>Saving a class at a time</h1>
	<ul>
		<li>It's very common to store data in classes</li>
		<li>It would be very nice to store an entire class with one line</li>
		<li>Python has a <em>pickle</em> function for exactly that purpose</li>
		<li>Look over <a href="pickleDemo.py">pickleDemo.py</a></li>
	</ul>
</div>

<div class="slide">
	<h1>Storing classes with Pickle</h1>
	<ul>
		<li>import <code>cPickle</code></li>
		<li>Define a class and create an instance</li>
		<li>Open a file for write access</li>
		<li>Use the <code>cPickle.dump()</code> method to store the class to the file</li>
		<li>Close the file</li>
	</ul>
</div>

<div class="slide">
	<h1>Loading a pickled file</h1>
	<ul>
		<li>Open a file for read access</li>
		<li>Use <code>cPickle.load()</code> to load an object</li>
		<li>Store it in a variable</li>
		<li>Lists are objects</li>
		<li>You can store and load an entire list with one <code>pickle</code> command</li>
	</ul>
</div>

<div class="slide">
	<h1>Exception Handling</h1>
	<ul>
		<li>Programs will have errors</li>
		<li>Up to now, errors always crashed your programs</li>
		<li>You can interrupt an error and save things (sometimes)</li>
		<li>This is called <em>exception handling</em></li>
	</ul>
</div>

<div class="slide">
	<h1>Handling an error</h1>
	<ul>
		<li>consider this code:</li>
		<li><code>x = int(raw_input("enter a number: ")</code></li>
		<li>It will crash if the user enters "three"<li>
		<li>Python reports a ValueError</li>
	</ul>
</div>

<div class="slide">
	<h1>Adding a basic try block</h1>
	<ul>
		<li>Now look at this variation:</li>
		<li><pre>
try:
	x = int(raw_input("enter a number: "))
except:
	print "there was an error"
		</pre></li>
		<li><code>try</code> indicates risky code is coming</li>
		<li><code>except</code> tells what to do if an error happens</li>
	</ul>
</div>

<div class="slide">
	<h1>Handling Specific Errors</h1>
	<ul>
		<li>look over <a href="exceptions.py">exceptions.py</a></li>
		<li>You can specify a particular error type</li>
		<li>This allows you to catch multiple errors</li>
		<li>Generally you'll try to set values so program can continue</li>
		<li>last clause handles unspecified errors</li>
		<li>use <code>sys.exc_info()</code> for information about what happened</li>
	</ul>
</div>

<div class="slide">
	<h1>Using a Loop with exception-handling</h1>
	<ul>
		<li>Sometimes you'll want to keep going until input is correct</li>
		<li>The <code>loopedInput()</code> function illustrates how</li>
		<li>Set <code>keepGoing</code> to false inside loop</li>
		<li>Normal (non-error) behavior should exit the loop</li>
		<li>If an exception happens, set <code>keepGoing</code>True</li>
		<li>This will force another pass of the loop</li>
	</ul>
</div>

<div class="slide">
	<h1>Using a relational database</h1>
	<ul>
		<li>More sophisticated data can require specialized software</li>
		<li>Relational databases are one way to store data</li>
		<li><a href="http://www.sqlite.org/">SQLite</a> is a powerful and relatively easy choice</li>
		<li><a href="https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/">
			  sqlite manager</a> is a firefox extension that simplifies sqlite</li>
		<li>SQLite is small and efficient, installed with many versions of Python</li>
	</ul>
</div>

<div class="slide">
	<h1>Overview of SQL</h1>
	<ul>
		<li>Data Definition Language: defines data structures</li>
		<li>Data Query Language: asks questions of data</li>
		<li>Structure: Database -> Table -> Record -> Field</li>
		<li>Each record/field is a fixed-length</li>
		<li>Data types strictly enforced</li>
	</ul>
</div>

<div class="slide">
	<h1>Creating a table</h1>
	<ul>
		<li>Examine this code:</li>
		<li><pre>
CREATE TABLE contacts (
  id INTEGER PRIMARY KEY,
	name VARCHAR(20),
	company VARCHAR(20),
	email VARCHAR(20)
);
		</pre></li>
		<li>Builds a table with four records</li>
	</ul>
</div>

<div class="slide">
	<h1>SQL Variable types</h1>
	<ul>
		<li>Strings are fixed-length</li>
		<li>You must specify length</li>
		<li>VARCHAR abridges trailing spaces</li>
		<li>Numeric types have an automatic length</li>
		<li>Other types include dates, BLOB, text</li>
	</ul>
</div>

<div class="slide">
	<h1>Creating a Primary Key</h1>
	<ul>
		<li>Each table must have a field designated as <em>primary key</em></li>
		<li>This field is guaranteed to be unique and non-null</li>
		<li>Primary keys aid in searching and indexing</li>
		<li>Frequently primary keys are auto-numbered integers</li>
		<li>This is automatic in SQLite</li>
	</ul>
</div>

<div class="slide">
	<h1>Inserting contents into a table</h1>
	<ul>
		<li>Add data to a table with code like this</li>
		<li><pre>
INSERT INTO contacts VALUES(
  null, 'Guido Von Rossum', 'Google', 'guido@python.org'
)
		</pre></li>
		<li>null provides automatic index value</li>
		<li>String values in <em>single quotes</em></li>
		<li>You must include a value for each field in the right order</li>
	</ul>
</div>

<div class="slide">
	<h1>Viewing the contents of a table</h1>
	<ul>
		<li>Look over the following code</li>
		<li><pre>SELECT * FROM contacts</pre></li>
		<li>This displays the entire contacts table</li>
		<li><pre>SELECT name, email FROM contacts</pre></li>
		<li>displays only the name and email</li>
	</ul>
</div>

<div class="slide">
	<h1>Narrowing the search</h1>
	<ul>
		<li>Exact match:</li>
		<li><pre>SELECT * FROM contacts WHERE name == 'andy'</pre></li>
		<li>Begins with a letter</li>
		<li><pre>SELECT * FROM contacts WHERE name LIKE 'a%'</li>
		<li>Ends with a letter</li>
		<li><pre>SELECT * FROM contacts WHERE name LIKE '%a'</li>
		<li>Contains a letter</li>
		<li><pre>SELECT * FROM contacts WHERE name LIKE '%a%'</li>
	</ul>
</div>

<div class="slide">
	<h1>Connecting to a database with Python</h1>
	<ul>
		<li>import sqlite3 library (may need to be installed)</li>
		<li>Make a connection to a data file (can be a new file)</li>
		<li>Create a <em>cursor</em> to control access to data</li>
		<li><code>c.execute()</code> sends an SQL command to the database</li>
		<li>Some commands return a value that can be manipulated</li>
	</ul>
</div>

<div class="slide">
	<h1>Parsing a query result</h1>
	<ul>
		<li>SELECT queries return data in a 2D array</li>
		<li>Use one loop to iterate through records</li>
		<li>Use a nested loop to iterate through fields</li>
	</ul>
</div>

<div class="slide">
	<h1>Making changes permanent</h1>
	<ul>
		<li>Database operations are in <em>transactions</em></li>
		<li>A transaction is temporary until it is committed</li>
		<li>Use the <code>commit()</code> function to finalize</li>
		<li>Close the data connection with <code>c.close()</code></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<div class="slide">
	<h1></h1>
	<ul>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ul>
</div>

<!-- div.slide>h1+ul>li*5 -->

</div> <!-- end slide show -->

</body>
</html>